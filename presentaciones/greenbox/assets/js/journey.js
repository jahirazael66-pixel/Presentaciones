/* Native vertical journey. Content follows normal document scrolling. */
(function(){'use strict';
const sections=[...document.querySelectorAll('section.scene')],media=matchMedia('(prefers-reduced-motion: reduce)'),$=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
let current=0,saved=null;try{saved=localStorage.getItem('greenbox-motion')}catch(e){}
let motion=saved===null?!media.matches:saved==='on',explicit=saved!==null,activeTimeline=null,scrollFrame=0,programScroll=false,scrollTimer=0,scrollTween=null;
const points=sections.map(s=>Math.max(1,...$$('[data-step]',s).map(b=>Number(b.dataset.step)+1))),seen=new Set();
function hint(text){const e=$('#screen-hint');e.textContent=text;e.hidden=false;setTimeout(()=>e.hidden=true,4000)}
function controls(){const s=sections[current],p=Number(s.dataset.point);$('#position').textContent=`${current+1} / ${sections.length}`;$('#current-topic').textContent=s.dataset.title;$('#prev').disabled=current===0&&p===0;$('#next').disabled=current===sections.length-1&&p===points[current]-1;$$('.chapter-rail [data-jump]').forEach(b=>b.setAttribute('aria-current',Number(b.dataset.jump)===current));$$('.chapters [data-jump]').forEach(b=>{const h=Number(b.dataset.jump);b.setAttribute('aria-current',current>=h&&current<(h===1?3:h===3?4:h===4?8:h===8?10:13))});$('#notes-title').textContent=s.dataset.title;$('#notes-text').textContent=$('.notes',s).textContent}
function animate(s,entry=false){if(activeTimeline){activeTimeline.progress(1).kill();activeTimeline=null}if(!motion)return;const tl=gsap.timeline({defaults:{duration:.55,ease:'power2.out'}});activeTimeline=tl;
const panel=$('.topic-panel:not([hidden])',s),copies=$$('.story-copy:not([hidden])',s);if(panel)tl.fromTo(panel,{opacity:.45,y:12},{opacity:1,y:0},0);else if(copies.length)tl.fromTo(copies,{opacity:.45,y:12},{opacity:1,y:0},0);
if(entry){const heading=$('.chapter-heading',s);if(heading)tl.fromTo(heading,{opacity:.4,y:14},{opacity:1,y:0},0);}
if(window.GB_LEARNING)GB_LEARNING.animate(s,tl,entry);
const figures=$$('.big-figures>div,.product-photo-set:not([hidden]) figure,.market-dot',panel||s);if(figures.length)tl.fromTo(figures,{opacity:.5,y:15},{opacity:1,y:0,stagger:.07},.05);
if(s.dataset.scene==='relationships')tl.fromTo($('.relation-line',s),{strokeDasharray:260,strokeDashoffset:260},{strokeDashoffset:0,duration:.9},0);
}
function hash(s,p){history.replaceState(null,'',`#${s.id}/${p}`)}
function setStep(h,p,entry=false){h=Math.max(0,Math.min(sections.length-1,h));p=Math.max(0,Math.min(points[h]-1,p));const s=sections[h];current=h;s.dataset.point=p;$$('[data-step]',s).forEach(b=>b.setAttribute('aria-pressed',Number(b.dataset.step)===p));$$('[data-panel]',s).forEach(e=>e.hidden=Number(e.dataset.panel)!==p);$$('[data-copy]',s).forEach(e=>e.hidden=Number(e.dataset.copy)!==p);if(window.GB_LEARNING)GB_LEARNING.sync(s,p);fit(s);controls();hash(s,p);animate(s,entry);seen.add(s);document.dispatchEvent(new CustomEvent('gb:state',{detail:{h,p}}))}
function fit(s){
 if(!s)return;
 if(innerWidth<=760||s.id==='cover'){s.style.removeProperty('--frame-scale');return}
 const shell=$('.chapter-shell',s),room=innerHeight-$('.site-header').getBoundingClientRect().height-8;
 s.style.setProperty('--frame-scale',1);
 const scale=Math.min(1,room/shell.offsetHeight);
 s.style.setProperty('--frame-scale',Math.max(.2,scale));
 // Zoom can change the available line width. Measure the final box, not stale geometry.
 const actual=shell.offsetHeight*Number(s.style.getPropertyValue('--frame-scale'));if(actual>room)s.style.setProperty('--frame-scale',Math.max(.2,scale*room/actual));
}
function stopScroll(){if(scrollTween){scrollTween.kill();scrollTween=null}clearTimeout(scrollTimer);programScroll=false}
function frame(s,smooth=true){
 stopScroll();fit(s);programScroll=true;
 const header=$('.site-header').getBoundingClientRect().height;
 const target=Math.max(0,Math.min(document.documentElement.scrollHeight-innerHeight,scrollY+s.getBoundingClientRect().top-header));
 if(motion&&smooth){const pos={y:scrollY};scrollTween=gsap.to(pos,{y:target,duration:.7,ease:'power2.inOut',onUpdate:()=>window.scrollTo(0,pos.y),onComplete:()=>{window.scrollTo(0,target);scrollTween=null;programScroll=false}})}
 else {window.scrollTo(0,target);scrollTimer=setTimeout(()=>programScroll=false,30)}
}
function go(h,p=0,scroll=true){h=Math.max(0,Math.min(sections.length-1,h));setStep(h,p,!seen.has(sections[h]));if(scroll)frame(sections[h])}
function move(n){const p=Number(sections[current].dataset.point),next=p+n;if(next>=0&&next<points[current]){setStep(current,next);frame(sections[current])}else if(current+n>=0&&current+n<sections.length)go(current+n,n<0?points[current+n]-1:0)}
function detect(){scrollFrame=0;if(programScroll)return;const anchor=innerHeight*.35;let best=0;sections.forEach((s,i)=>{const r=s.getBoundingClientRect();if(r.top<=anchor&&r.bottom>anchor)best=i});if(best!==current){const s=sections[best];setStep(best,Number(s.dataset.point),!seen.has(s))}}
window.GB_DECK={isReady:()=>true,getIndices:()=>({h:current,f:Number(sections[current].dataset.point)-1}),getCurrentSlide:()=>sections[current],slide:(h,v=0,f=-1)=>go(h,f+1),navigateFragment:f=>setStep(current,f+1),prev:()=>move(-1),next:()=>move(1)};
window.GB_MOTION={isMotion:()=>motion,enter:()=>animate(sections[current],true),cancel:()=>activeTimeline?.progress(1).kill()};
function configure(){document.body.classList.toggle('motion-on',motion);document.body.classList.toggle('motion-off',!motion);$('#motion-toggle').textContent='Animación: '+(motion?'sí':'no');$('#motion-toggle').setAttribute('aria-pressed',motion);if(!motion){gsap.globalTimeline.getChildren().forEach(t=>{if(t.targets?.().some(e=>e?.closest?.('.scene')))t.progress(1);});}setStep(current,Number(sections[current].dataset.point));}
function closePanels(){$$('dialog[open]').forEach(d=>d.close());$('#menu-button').setAttribute('aria-expanded',false);$('#notes-toggle').setAttribute('aria-expanded',false)}
function openPanel(id,button){closePanels();$('#options-panel').hidden=true;$('#options-toggle').setAttribute('aria-expanded',false);const d=$('#'+id);d.showModal();button.setAttribute('aria-expanded',true);$('[data-close-panel]',d).focus()}
sections.forEach((s,h)=>{const b=document.createElement('button');b.textContent=`${String(h+1).padStart(2,'0')} · ${s.dataset.title}`;b.onclick=()=>{closePanels();go(h)};$('#index-list').append(b);$$('[data-step]',s).forEach(b=>b.onclick=()=>{setStep(h,Number(b.dataset.step));frame(s);});});
$$('[data-jump]').forEach(b=>b.onclick=()=>{closePanels();go(Number(b.dataset.jump))});$('#prev').onclick=()=>move(-1);$('#next').onclick=()=>move(1);
$('#menu-button').onclick=()=>openPanel('index-panel',$('#menu-button'));$('#notes-toggle').onclick=()=>openPanel('notes-panel',$('#notes-toggle'));$$('[data-close-panel]').forEach(b=>b.onclick=closePanels);$$('dialog').forEach(d=>{d.addEventListener('cancel',()=>{$('#menu-button').setAttribute('aria-expanded',false);$('#notes-toggle').setAttribute('aria-expanded',false)});d.addEventListener('click',e=>{if(e.target===d){const r=d.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)closePanels()}})});
$('#options-toggle').onclick=()=>{const p=$('#options-panel');p.hidden=!p.hidden;$('#options-toggle').setAttribute('aria-expanded',!p.hidden)};
$('#motion-toggle').onclick=()=>{explicit=true;motion=!motion;try{localStorage.setItem('greenbox-motion',motion?'on':'off')}catch(e){}configure()};$('#replay').onclick=()=>motion?animate(sections[current],true):hint('Activa Animación: sí para repetir el movimiento.');
$('#fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen()}catch(e){hint('Puedes usar F11 para pantalla completa.')}};
media.addEventListener('change',()=>{if(!explicit){motion=!media.matches;configure()}});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){$('#options-panel').hidden=true;$('#options-toggle').setAttribute('aria-expanded',false);closePanels();return}if($('dialog[open]')||(e.target.closest('button,a,input,select,textarea,[role=button]')&&!e.target.closest('.toolbar')))return;if(['ArrowRight','PageDown'].includes(e.key)){e.preventDefault();move(1)}if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();move(-1)}if(e.key==='Home'){e.preventDefault();go(0)}if(e.key==='End'){e.preventDefault();go(sections.length-1)}});
window.addEventListener('scroll',()=>{if(!scrollFrame)scrollFrame=requestAnimationFrame(detect)},{passive:true});
function readHash(){const value=location.hash.slice(1);if(!value)return{h:0,p:0};if(value[0]==='/'){const v=value.split('/');return{h:Number(v[1])||0,p:Math.max(0,(v[2]===undefined?-1:Number(v[2]))+1)}}const [id,point]=value.split('/');const h=sections.findIndex(s=>s.id===id);return{h:h<0?0:h,p:Number(point)||0}}
const start=readHash();current=Math.min(sections.length-1,start.h);configure();go(current,start.p,current!==0||start.p!==0);
window.addEventListener('hashchange',()=>{const target=readHash();go(target.h,target.p)});
window.GB_JOURNEY={go,setStep,points:()=>points.slice(),current:()=>current,reframe:fit};
sections.forEach(fit);frame(sections[current],false);
let resizeTimer=0;window.addEventListener('resize',()=>{clearTimeout(resizeTimer);resizeTimer=setTimeout(()=>{sections.forEach(fit);frame(sections[current],false)},100)});
if(document.fonts)document.fonts.ready.then(()=>{sections.forEach(fit);frame(sections[current],false)});
$$('img').forEach(img=>img.addEventListener('load',()=>{fit(img.closest('.scene'));if(img.closest('.scene')===sections[current]&&!programScroll)frame(sections[current],false)}));
['wheel','touchstart'].forEach(type=>window.addEventListener(type,()=>{if(programScroll)stopScroll()},{passive:true}));

})();
