window.GB_CHART=null;
window.drawEmployment=function(replay=false,motion=true){
 const el=document.getElementById('employment-chart');
 if(!window.echarts){el.innerHTML='<div class="fallback-chart"><div style="height:55px">40 · Antes</div><div style="height:230px">240 · Después</div></div>';return;}
 if(!GB_CHART) window.GB_CHART=echarts.init(el,null,{renderer:'svg'});
 if(replay)GB_CHART.clear();
 GB_CHART.setOption({animation:motion&&(window.GB_MOTION?GB_MOTION.isMotion():!matchMedia('(prefers-reduced-motion: reduce)').matches),animationDuration:1100,animationDurationUpdate:900,textStyle:{fontFamily:'Inter',color:'#163d2c'},grid:{left:45,right:20,top:25,bottom:45},tooltip:{trigger:'axis',axisPointer:{type:'shadow'},formatter:p=>`${p[0].name}: <b>${p[0].value} trabajadores</b><br>NESsT · enero 2026`},xAxis:{type:'category',data:['Antes del crecimiento','Después del crecimiento'],axisTick:{show:false},axisLine:{lineStyle:{color:'#afcabb'}},axisLabel:{fontSize:12,interval:0}},yAxis:{type:'value',min:0,max:250,splitLine:{lineStyle:{color:'#e3ede5'}},axisLabel:{fontSize:12}},series:[{type:'bar',data:[{value:40,itemStyle:{color:'#bedcca'}},{value:240,itemStyle:{color:'#2ad386'}}],barWidth:70,itemStyle:{borderRadius:[10,10,0,0]},label:{show:true,position:'top',fontSize:26,fontWeight:700,color:'#163d2c'}}]});GB_CHART.resize();
};
