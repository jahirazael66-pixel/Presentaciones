(function(){'use strict';
const slides=[...document.querySelectorAll('.scene')],media=matchMedia('(prefers-reduced-motion: reduce)');
let saved=null;try{saved=localStorage.getItem('greenbox-motion');}catch(e){}
let motion=saved===null?!media.matches:saved==='on',explicit=saved!==null,context=null,lastSlide=null,lastPoint=-1,frame=null;
gsap.registerPlugin(MotionPathPlugin,DrawSVGPlugin,MorphSVGPlugin);
const deck=new Reveal({width:1280,height:720,margin:.035,minScale:.1,maxScale:1.6,center:false,scrollActivationWidth:null,hash:true,controls:false,progress:true,transition:motion?'fade':'none',transitionSpeed:'default',autoAnimate:motion,autoAnimateDuration:.9,autoAnimateEasing:'ease-in-out',keyboard:true,touch:true});window.GB_DECK=deck;
const $=(s,root=document)=>root.querySelector(s),$$=(s,root=document)=>[...root.querySelectorAll(s)];
function stop(){if(context){context.revert();context=null;}if(frame){cancelAnimationFrame(frame);frame=null;}}
function show(selector,p,root){$$(selector,root).forEach(x=>{const n=Number(Object.values(x.dataset)[0]);x.hidden=n!==p;});}
function counts(root,tl){$$('[data-count]',root).forEach(el=>{const value=Number(el.dataset.count),suffix=el.dataset.suffix||'';if(!motion){el.textContent=value+suffix;return;}const data={n:0};tl.to(data,{n:value,duration:1,ease:'power2.out',onUpdate:()=>el.textContent=Math.round(data.n)+suffix},.1);});}
function chapter(i){return i<3?1:i===3?3:i<8?4:i<10?8:i<13?10:13;}
function controls(){const i=deck.getIndices().h,s=deck.getCurrentSlide(),p=$$('.scene-marker.visible',s).length,n=$$('.scene-steps button',s).length;
 $('#position').textContent=`${i+1} / ${slides.length}`;$('#prev').disabled=i===0&&p===0;$('#next').disabled=i===slides.length-1&&p>=Math.max(0,n-1);
 $$('[data-jump]',document.querySelector('.chapters')).forEach(b=>b.setAttribute('aria-current',Number(b.dataset.jump)===chapter(i)));
 $('#notes-title').textContent=s.dataset.title;$('#notes-text').textContent=$('.notes',s).textContent;
 document.body.style.background=s.classList.contains('theme-white')?'#fff':s.classList.contains('theme-mint')?'#e4f4e9':'#f7f3e8';
}
function state(s,p){
 s.dataset.point=p;$$('.scene-steps button',s).forEach((b,j)=>b.setAttribute('aria-pressed',j===p));
 $$('[data-copy]',s).forEach(el=>el.hidden=Number(el.dataset.copy)!==p);
 $$('[data-node]',s).forEach(el=>el.classList.toggle('active',Number(el.dataset.node)===p));
 show('[data-product]',p,s);show('[data-farm]',p,s);show('[data-cert-copy]',p,s);show('[data-network-copy]',p,s);show('[data-rationale]',p,s);
 if(s.dataset.scene==='identity')show('[data-identity]',p,s);
 if(s.dataset.scene==='workers'){$('.employment-chart',s).hidden=p!==0;$('.work-emblem',s).hidden=p===0;$('.work-caption',s).hidden=p!==0;const em=$('.work-emblem',s);const icons=['','M50 23Q25 9 8 18V84Q29 74 50 88Q71 74 92 84V18Q75 9 50 23ZM50 23V88','M17 92V74Q17 54 36 54Q55 54 55 74V92M36 45A15 15 0 1 0 36 15A15 15 0 0 0 36 45M65 91V73Q65 56 81 56Q97 56 97 73V91M81 47A12 12 0 1 0 81 23A12 12 0 0 0 81 47','M50 40A15 15 0 1 0 50 10A15 15 0 0 0 50 40M25 94V73Q25 48 50 48Q75 48 75 73V94M35 72V94M65 72V94'];if(p){$('path',em).setAttribute('d',icons[p]);$('span',em).textContent=['','CAPACITACIÓN','IGUALDAD LABORAL','GUARDERÍA'][p];}$$('[data-link]',s).forEach(x=>x.classList.toggle('active',Number(x.dataset.link)===p));}
 $$('[data-family]',s).forEach(x=>x.classList.toggle('active',Number(x.dataset.family)===p));
 $$('[data-gate]',s).forEach(x=>x.classList.toggle('active',Number(x.dataset.gate)===p));
 $$('[data-group]',s).forEach(x=>x.classList.toggle('active',Number(x.dataset.group)===p));
 $$('[data-quad]',s).forEach(x=>x.classList.toggle('active',Number(x.dataset.quad)===p));
 if(s.dataset.scene==='chain'){$('.chain-fruit',s).style.left=`calc(${12.5+p*25}% - 23px)`;}
 if(window.GB_LEARNING)window.GB_LEARNING.sync(s,p);
 if(s.dataset.scene==='products'){
 const path=$('.fruit-illustration path',s);const d=['M48 27C33 13 14 26 17 52C20 76 38 90 54 84C79 74 91 38 72 25C65 20 55 22 48 27ZM48 27Q47 14 60 8M53 19Q71 5 80 12Q73 25 53 19','M50 8C15 17 12 78 50 94C88 78 85 17 50 8ZM50 8V94M50 8C32 30 32 73 50 94M50 8C68 30 68 73 50 94','M50 7C46 27 17 48 17 69C17 108 83 108 83 69C83 48 54 27 50 7Z'];path.dataset.target=d[p];if(!motion)path.setAttribute('d',d[p]);
 }
}
function run(replay=false){if(!deck.isReady())return;const s=deck.getCurrentSlide(),p=$$('.scene-marker.visible',s).length,changed=s!==lastSlide;if(!replay&&!changed&&p===lastPoint)return;const previousPoint=lastPoint;stop();state(s,p);controls();lastSlide=s;lastPoint=p;
 if(!motion){counts(s,{to:()=>{}});if(s.dataset.scene==='products')$('.fruit-illustration path',s).setAttribute('d',$('.fruit-illustration path',s).dataset.target);return;}
 context=gsap.context(()=>{
  const tl=gsap.timeline({defaults:{ease:'power3.out',duration:.75}});if(window.GB_LEARNING)window.GB_LEARNING.animate(s,tl,changed||replay);if(changed||replay)tl.fromTo($('.scene-heading',s),{y:20,opacity:0},{y:0,opacity:1},0);
  const copy=$('.story-copy:not([hidden])',s);if(copy)tl.fromTo(copy,{y:25,opacity:0},{y:0,opacity:1},.12);
  counts(s,tl);const kind=s.dataset.scene;
  if(kind==='cover'){tl.fromTo($('.cover-heading',s),{y:30,opacity:0},{y:0,opacity:1},.05).fromTo($$('.cover-island',s),{scale:.75,opacity:0},{scale:1,opacity:1,stagger:.18},.15).fromTo($('.draw-path',s),{drawSVG:'0%'},{drawSVG:'100%',duration:1.8},.1).to($('.travel-fruit',s),{motionPath:{path:$('.draw-path',s),align:$('.draw-path',s),alignOrigin:[.5,.5]},duration:2,ease:'power1.inOut'},.15);}
  if(kind==='identity'){tl.fromTo($('.identity-type',s),{x:-25,opacity:0},{x:0,opacity:1},.05).fromTo($('.identity-facts>span:not([hidden])',s),{y:12,opacity:0},{y:0,opacity:1},.2);}
  if(kind==='products'){const path=$('.fruit-illustration path',s);tl.to(path,{morphSVG:path.dataset.target,duration:.9},.05).fromTo($('.product-halo',s),{scale:.86},{scale:1},0).fromTo($('.product-names:not([hidden])',s),{y:12,opacity:0},{y:0,opacity:1},.2);const chips=$$('.product-shapes span',s);tl.set(chips,{opacity:p===0?1:0}).fromTo(chips,{y:-30,scale:.3},{y:65,scale:1,stagger:.1},.2);}
  if(kind==='chain'){tl.to($$('.chain-node',s),{scale:(j)=>j===p?1.06:.94,y:(j)=>j===p?-3:0,duration:.7},0);const from=changed||replay?0:Math.max(0,previousPoint);tl.fromTo($('.chain-fruit',s),{left:`calc(${12.5+from*25}% - 23px)`},{left:`calc(${12.5+p*25}% - 23px)`,duration:1,ease:'power2.inOut'},0).fromTo($('.track-progress',s),{drawSVG:`0% ${from*100/3}%`},{drawSVG:`0% ${p*100/3}%`,duration:1},0).fromTo($('.chain-node.active .node-art',s),{scale:.8},{scale:1},.1);}
  if(kind==='farm'){tl.fromTo($('.exchange-lines path',s),{drawSVG:'0%'},{drawSVG:'100%',duration:1.1},.05).fromTo($('.exchange-metric:not([hidden])',s),{scale:.88,opacity:0},{scale:1,opacity:1},.05).fromTo($$('.exchange-party',s),{y:20,opacity:0},{y:0,opacity:1,stagger:.12},0);}
  if(kind==='workers'){if(p===0)tl.fromTo($$('.employment-bar i',s),{scaleY:0},{scaleY:1,duration:1.1,stagger:.15},.05);else tl.fromTo($('.work-emblem',s),{scale:.82,opacity:0},{scale:1,opacity:1},.05);}
  if(kind==='environment'||kind==='ods'||kind==='relationships'){tl.fromTo($('.draw-path',s),{drawSVG:'0%'},{drawSVG:'100%',duration:1.25},.05).fromTo($('[data-node].active',s),{scale:.88},{scale:1},.1);}
  if(kind==='certifications'){const families=$$('.cert-family',s);tl.to(families,{flexGrow:(j)=>p===0?1:j+1===p?1.6:.7,duration:.8,ease:'power2.inOut'},0);tl.to(families,{opacity:(j)=>p===0||j+1===p?1:.72,duration:.5},0).fromTo($('[data-cert-copy]:not([hidden])',s),{y:12,opacity:0},{y:0,opacity:1},.15);if(p)tl.fromTo($$('.cert-family.active .cert-item',s),{y:10,opacity:0},{y:0,opacity:1,stagger:.09},.05);else tl.fromTo(families,{y:20,opacity:0},{y:0,opacity:1,stagger:.12},0);}
  if(kind==='iso')tl.fromTo($('.evidence-gates>div.active',s),{y:18,opacity:.4},{y:0,opacity:1},.05);
  if(kind==='network'){tl.fromTo($('.network-branches path',s),{drawSVG:'0%'},{drawSVG:'100%',duration:1.1},0);tl.to($$('.network-group',s),{opacity:(j)=>p===0||j+1===p?1:.7,duration:.45},0).fromTo($('[data-network-copy]:not([hidden])',s),{y:12,opacity:0},{y:0,opacity:1},.1);if(changed||replay)tl.fromTo($$('.network-group .stake-token',s),{y:12,opacity:0},{y:0,opacity:1,stagger:.025},.15);}
  if(kind==='matrix'){tl.to($$('.value-quadrant',s),{opacity:(j,el)=>p===0||Number(el.dataset.quad)===p?1:.72,duration:.45},0).fromTo($('[data-rationale]:not([hidden])',s),{x:15,opacity:0},{x:0,opacity:1},.1);if(changed||replay)tl.fromTo($$('.value-quadrant',s),{y:20},{y:0,stagger:.07},.1);}
  if(kind==='closing'){tl.fromTo($('[data-node].active',s),{scale:.9},{scale:1},.05);}
  if(kind==='sources')tl.fromTo($$('.sources a',s),{y:16,opacity:0},{y:0,opacity:1,stagger:.055},.05);
 },s);
}
function configure(){stop();document.body.classList.toggle('motion-on',motion);document.body.classList.toggle('motion-off',!motion);$('#motion-toggle').textContent='Animación: '+(motion?'sí':'no');$('#motion-toggle').setAttribute('aria-pressed',motion);deck.configure({transition:motion?'fade':'none',autoAnimate:motion,backgroundTransition:motion?'fade':'none'});lastPoint=-1;run(true);}
function closePanels(){$$('.utility-panel').forEach(p=>p.hidden=true);$('#index-toggle').setAttribute('aria-expanded',false);$('#notes-toggle').setAttribute('aria-expanded',false);deck.configure({keyboard:true});}
function panel(id,button){const el=$('#'+id),open=el.hidden;closePanels();el.hidden=!open;button.setAttribute('aria-expanded',open);deck.configure({keyboard:!open});if(open)$('[data-close-panel]',el).focus();}
$$('[data-jump]').forEach(b=>b.onclick=()=>{closePanels();deck.slide(Number(b.dataset.jump),0,-1);});
slides.forEach((s,i)=>{const b=document.createElement('button');b.textContent=`${String(i+1).padStart(2,'0')} · ${s.dataset.title}`;b.onclick=()=>{closePanels();deck.slide(i,0,-1);};$('#index-list').append(b);$$('[data-step]',s).forEach(b=>b.onclick=()=>{deck.navigateFragment(Number(b.dataset.step)-1);run();});});
$('#prev').onclick=()=>deck.prev();$('#next').onclick=()=>deck.next();$('#index-toggle').onclick=()=>panel('index-panel',$('#index-toggle'));$('#notes-toggle').onclick=()=>panel('notes-panel',$('#notes-toggle'));$$('[data-close-panel]').forEach(b=>b.onclick=closePanels);
$('#motion-toggle').onclick=()=>{explicit=true;motion=!motion;try{localStorage.setItem('greenbox-motion',motion?'on':'off');}catch(e){}configure();};
$('#replay').onclick=()=>{if(motion)run(true);else{const el=$('#screen-hint');el.textContent='Activa «Animación: sí» y pulsa «Repetir ↻» para ver la secuencia.';el.hidden=false;setTimeout(()=>el.hidden=true,4500);}};
$('#fullscreen').onclick=async()=>{try{if(document.fullscreenElement)await document.exitFullscreen();else await document.documentElement.requestFullscreen();}catch(e){$('#fullscreen').textContent='Utiliza F11';}};
document.addEventListener('keydown',e=>{if(e.key==='Escape')closePanels();});media.addEventListener('change',()=>{if(!explicit){motion=!media.matches;configure();}});
deck.on('slidechanged',()=>run());deck.on('fragmentshown',()=>run());deck.on('fragmenthidden',()=>run());deck.on('overviewshown',stop);deck.on('overviewhidden',()=>run(true));deck.on('ready',()=>configure());deck.initialize();
window.GB_MOTION={isMotion:()=>motion,enter:()=>run(true),cancel:stop};
})();
