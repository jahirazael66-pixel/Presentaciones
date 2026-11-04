from pathlib import Path
import json,math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from fontTools.ttLib import TTFont as Font
R=Path(__file__).resolve().parents[1];D=json.loads((R/'scripts/pdf-data.json').read_text());T=R.parent/'tmp/adex-pdf';T.mkdir(parents=True,exist_ok=True)
for name,family,weight in [('Body','manrope',400),('Bold','manrope',700),('Display','space-grotesk',500)]:
 f=Font(R/f'node_modules/@fontsource/{family}/files/{family}-latin-{weight}-normal.woff');f.flavor=None;f.save(T/(name+'.ttf'));pdfmetrics.registerFont(TTFont(name,str(T/(name+'.ttf'))))
W,H=841.89,595.28;M=30;CW=W-60;OUT=R/'public/ADEX-Revision-CV-IA.pdf';c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1);c.setTitle('ADEX | Revisión de CV con IA');c.setAuthor(' · '.join(D['team']));C={'blue':'#1465ff','navy':'#0b2245','ink':'#142944','muted':'#52647c','line':'#d9e2ef','pale':'#edf4ff','mint':'#c7eee8','amber':'#efbf65'};fg=C['ink'];bg='#ffffff';page=0;bounds=[]
def rect(x,y,w,h,col,r=0,stroke=None):
 c.setFillColor(HexColor(C.get(col,col)));c.setStrokeColor(HexColor(C.get(stroke or col,stroke or col)));c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=bool(stroke))
def text(s,x,y,w,size=14,font='Body',color=None,align=0,leading=None):
 s=str(s).replace('→',' > ').replace('≥','mín. ').replace('−','-').replace('≠','no equivale a').replace('–','-').replace('\n','<br/>')
 p=Paragraph(s,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.3,textColor=HexColor(C.get(color,color) if color else fg),alignment=align));_,h=p.wrap(w,10000);p.drawOn(c,x,H-y-h);bounds.append([page,s[:60],x,y,w,h]);assert y+h<H-14,(page,s[:50],y+h);return h
def line(x,y,xx,yy,color='line',width=.7):
 c.setStrokeColor(HexColor(C.get(color,color)));c.setLineWidth(width);c.line(x,H-y,xx,H-yy)
def begin(i,dark=False):
 global fg,bg,page
 page=i+1;fg='#ffffff'if dark else C['ink'];bg=C['navy']if dark else '#ffffff';rect(0,0,W,H,bg)
 text(D['slides'][i]['chapter'].upper(),M,20,650,10,'Bold','pale'if dark else 'muted');text(f'{page:02d} / 08',W-85,20,55,10,'Body','pale'if dark else 'muted',align=2);line(M,48,W-M,48,'#ffffff35'if dark else 'line')
 if i>0:text(D['slides'][i]['title'],M,65,CW,32,'Display')
 return 128
def footer(s):
 line(M,542,W-M,542,'#ffffff40'if bg==C['navy']else'line');text(s,M,553,CW,10.5,'Body','pale'if bg==C['navy']else'muted',leading=13.3);c.showPage()
def card(title,body,x,y,w,h,fill='pale',color=None):
 rect(x,y,w,h,fill,8);used=text(title,x+15,y+15,w-30,17,'Display',color);bh=text(body,x+15,y+used+25,w-30,13,'Body',color);assert used+bh+40<=h,(page,title,'card overflow',used+bh+40,h)
def arrow(x,y,xx,yy,col='blue'):
 line(x,y,xx,yy,col,1.5);a=math.atan2(yy-y,xx-x)
 for d in [-.45,.45]:line(xx,yy,xx-6*math.cos(a+d),yy-6*math.sin(a+d),col,1.5)
def logo(x,y):
 c.saveState();p=c.beginPath();p.rect(x,H-y-38,105,38);c.clipPath(p,stroke=0,fill=0);c.drawImage(str(R/'public/assets/adex.png'),x-15,H-(y-52)-130,130,130);c.restoreState()
# 1
begin(0);logo(M,71);text('Revisión de<br/>CV con IA.',M,146,430,59,'Display','blue',leading=61);text('Del PDF a una ficha organizada.<br/>Más tiempo para evaluar personas.',M,302,400,21)
rect(493,112,315,326,'pale',15);rect(521,143,258,263,'#ffffff',10,stroke='line');text('POSTULACIÓN / AGRO-01',541,163,220,10,'Bold','muted');text('Ficha del postulante',541,201,220,22,'Display');
for j,s in enumerate(['Datos organizados','Evidencia vinculada','Revisión humana']):text('• '+s,541,253+j*36,220,15,'Body','blue')
text('Forms > Drive > Make > GPT > Sheets',493,462,315,13,'Bold','blue',align=1)
text('INTEGRANTES',M,427,430,10,'Bold','muted');text('<br/>'.join(D['team']),M,449,440,12.1,leading=18)
footer('Pitch de 12 minutos · problema, solución, demostración y resultados del piloto.')
# 2
Y=begin(1);rect(M,Y,232,341,'#fff6e3',10);text('BASE DE COMPARACIÓN',M+18,Y+20,196,10.5,'Bold','#805516');text('8 min',M+18,Y+71,196,63,'Display',leading=70);text('por CV',M+18,Y+155,196,27,'Display');text('Lectura, búsqueda y registro manual.',M+18,Y+212,196,17);text('Tiempo humano estimado',M+18,Y+288,196,11,'Bold','#805516')
for j,(a,b)in enumerate([('Recibir','Formatos distintos.'),('Buscar','Información dispersa.'),('Comprobar','Requisitos y datos.'),('Registrar','Copiar a la base.')]):
 xx=294+j*130;line(xx,Y+32,xx+111,Y+32,'amber',2);text(f'0{j+1}',xx,Y+49,111,11,'Bold','muted');text(a,xx,Y+87,111,17,'Display');text(b,xx,Y+121,111,14)
card('El problema','La misma información se vuelve a leer y copiar.',294,348,246,133,'#fff6e3');card('La oportunidad','Organizarla antes de la evaluación del analista.',558,348,254,133,'pale')
footer('8 minutos por CV es un supuesto de comparación, no una medición del proceso real de ADEX.')
# 3
Y=begin(2);text('Una entrada. Dos rutas documentales. Una decisión humana.',M,Y,CW,16)
coords=[(102,212),(285,212),(468,212),(653,212),(653,347),(468,347),(285,347)]
for j in range(3):arrow(coords[j][0]+72,212,coords[j+1][0]-72,212)
arrow(653,257,653,310);arrow(581,347,540,347);arrow(396,347,357,347)
for j,(x,y)in enumerate(coords):
 if j==3:
  p=c.beginPath();p.moveTo(x,H-y+45);p.lineTo(x+73,H-y);p.lineTo(x,H-y-45);p.lineTo(x-73,H-y);p.close();c.setFillColor(HexColor('#fff0c8'));c.drawPath(p,fill=1,stroke=0)
 else:rect(x-72,y-35,144,70,'mint'if j==6 else'pale',24 if j==6 else 8)
 text(str(j+1).zfill(2),x-65,y-27,130,9,'Bold','muted',align=1);text('¿Plantilla válida?'if j==3 else D['flow'][j]['title'],x-67,y-8,134,13.5,'Display',align=1);text(''if j==3 else D['flow'][j]['short'],x-67,y+13,134,10,'Body','muted',align=1)
line(726,212,780,212,'#b86d4e',1);arrow(780,212,780,275,'#b86d4e');text('No',748,190,48,11,'Bold','#9f5c3f');rect(722,280,92,100,'#fff0e9',12);text('Rechazados',729,295,78,11,'Bold',align=1);text('Motivo + correo.<br/>Puede corregirse.',729,320,78,10.5,align=1);text('Sí',668,279,35,11,'Bold','blue')
for j,(a,b)in enumerate([('Validación previa','Marcador, etiquetas, orden y campos; cruza nombre, correo y vacante.'),('IA con fuentes','Organiza evidencia sobre estudios, habilidades y disponibilidad; conserva el PDF.'),('Revisión humana','RR. HH. contrasta la ficha y decide quién continúa a entrevista.')]):card(a,b,M+j*265,408,250,117,'pale')
footer('Admitidos y Rechazados son estados documentales. El sistema no contrata ni descarta personas por su cuenta.')
# 4
Y=begin(3);card('El sistema','Comprueba estructura y campos.<br/><br/>Cruza datos con el formulario.<br/><br/>Prepara la ficha con fuentes.',M,Y,245,300,'pale');card('Ficha de ejemplo','Origen: PDF y Forms.<br/><br/>Datos: nombre, correo y vacante.<br/><br/>Evidencia: estudios, Excel, inglés y experiencia.',296,Y,245,300,'#f5f7fb');card('Recursos Humanos','Contrasta la ficha con el PDF.<br/><br/>Verifica requisitos y competencias.<br/><br/>Decide quién continúa.',562,Y,250,300,'navy','#ffffff')
text('Plantilla de una columna · 23 campos · PDF con texto · hasta 1 MB',M,461,CW,16,'Bold','blue');text('La IA apoya la revisión. La decisión laboral sigue en Recursos Humanos.',M,497,CW,15)
footer('La validación textual no acredita títulos, habilidades o identidad. La ficha se comprueba frente a sus fuentes.')
# 5
Y=begin(4,True);text('DEMOSTRACIÓN / JAHIR',M,Y,280,11,'Bold','mint');text('04:00',M,Y+34,280,71,'Display',leading=76);text('Un PDF entra.<br/>La ficha queda registrada.',M,Y+137,280,20)
for j,(label,key)in enumerate([('Abrir formulario','form'),('Abrir resultados','sheet')]):
 yy=Y+239+j*58;rect(M,yy,280,46,'#17365f',7);text(label+' >',M+16,yy+12,248,15,'Bold','#ffffff');c.linkURL(D['links'][key],(M,H-yy-46,M+280,H-yy),relative=0,thickness=0)
for j,(a,b)in enumerate([('01 · Enviar un documento válido','Usar la plantilla completa y comprobar el registro del envío.'),('02 · Revisar ficha y fuentes','Abrir Admitidos y comparar la información con el PDF original.'),('03 · Mostrar un rechazo documental','Enviar la variante sin marcador. Revisar motivo y correo; permite corregir.')]):
 yy=Y+j*111;text(a,356,yy,456,20,'Display');text(b,356,yy+38,456,14,'Body','pale');line(356,yy+93,812,yy+93,'#ffffff30')
text('69,36 s',356,475,165,30,'Display','mint');text('Último envío válido registrado en Make. Durante la espera, explicar la validación.',523,476,289,13,'Body','pale')
footer('Usar la cuenta con acceso. Si falla la conexión, mostrar registros previos identificados como pruebas anteriores.')
# 6
Y=begin(5);text('ESCENARIO: 500 CV AL MES',M,Y,460,12,'Bold','blue')
for j,(label,hours,width,col)in enumerate([('Proceso manual','66 h 40 min',432,'amber'),('Con apoyo de IA','26 h',432*26/(500*8/60),'blue')]):
 yy=Y+53+j*99;text(label,M,yy,270,15);text(hours,311,yy,151,17,'Display',align=2);rect(M,yy+31,432,32,'#edf0f5',5);rect(M,yy+31,width,32,col,5)
rect(498,Y,314,155,'blue',11);text('CAPACIDAD LIBERADA / MES',516,Y+18,278,10.5,'Bold','#d4e4ff');text('40 h 40 min',516,Y+51,278,38,'Display','#ffffff');text('Para verificar, entrevistar y atender otras tareas.',516,Y+109,278,13,'Body','#ffffff')
text('S/ 45,60',498,Y+181,314,32,'Display','blue');text('Core de referencia · paquete completo.<br/>5.330 créditos estimados para 500 CV.',498,Y+225,314,12.8)
text('8 > 3 min por CV · reducción estimada de 62,5%. Se incluye 1 h mensual de mantenimiento.',M,405,CW,12.8)
headers=['CV / mes','Créditos','Horas netas liberadas','Software de referencia'];xs=[M,185,363,591];ws=[140,160,213,221]
for j,h in enumerate(headers):text(h,xs[j],440,ws[j],11,'Bold','muted')
for i,row in enumerate([['80','852,80','5 h 40 min','Free · S/ 0'],['500','5.330','40 h 40 min','Core · S/ 45,60'],['2.000','21.320','165 h 40 min','Cotizar paquete mayor']]):
 for j,t in enumerate(row):text(t,xs[j],466+i*23,ws[j],12.4)
footer('Escenarios, no ahorro observado. Tiempo liberado no reduce automáticamente planilla. US$12 × S/3,80 como referencia.')
# 7
Y=begin(6);cw=(CW-32)/3
for j,(n,a,b)in enumerate([('4/4','envíos completados','Dos perfiles ficticios; tres admitidos y un rechazo.'),('61,95 s','promedio en Make','En los tres envíos admitidos; excluye trabajo humano.'),('5,01 s','rechazo sin GPT','Documento sin marcador; validación previa a la IA.')]):
 xx=M+j*(cw+16);text(n,xx,Y,cw,39,'Display','blue');text(a,xx,Y+56,cw,17,'Display');text(b,xx,Y+85,cw,12.5)
xs=[M,355,549,690];ws=[305,180,125,122]
for j,t in enumerate(['Envío','Salida','Make','Créditos']):text(t,xs[j],281,ws[j],11,'Bold','muted')
for i,t in enumerate(D['trials']):
 yy=307+i*28;line(M,yy-5,812,yy-5);vals=[t['name'],t['state'],f"{t['seconds']:.2f} s".replace('.',','),f"{t['credits']:.2f}".replace('.',',')]
 for j,v in enumerate(vals):text(v,xs[j],yy,ws[j],11.9)
for j,(n,label)in enumerate([('≥95%','Éxito técnico'),('≥98%','Fidelidad de lectura'),('≥30%','Menos tiempo humano')]):
 xx=M+j*(cw+16);rect(xx,444,cw,72,'pale',7);text(n,xx+13,453,cw-26,25,'Display','blue');text(label,xx+13,488,cw-26,12,'Bold')
footer('Metas iniciales: validar durante dos semanas con revisión humana de todas las fichas. Reservar un minuto para preguntas.')
# 8
Y=begin(7)
for i,(a,b)in enumerate(D['sources']):
 yy=Y+i*72;text(str(i+1).zfill(2),M,yy,42,17,'Display','blue');text(a,M+55,yy,520,18,'Display');text('Consultar fuente oficial'if b.startswith('http')else b,M+55,yy+29,520,13,'Body','muted')
 if b.startswith('http'):c.linkURL(b,(M+55,H-yy-52,M+575,H-yy),relative=0,thickness=0)
rect(635,Y,177,400,'pale',10);text('Evidencia del piloto',649,Y+18,149,22,'Display','blue');text('Medido: tiempos, estados y créditos.<br/><br/>Estimado: tiempo humano, mantenimiento y costos.<br/><br/>Por validar: desempeño sostenido con carga real.',649,Y+83,149,12.8);c.linkURL(D['links']['sheet'],(635,H-Y-400,812,H-Y),relative=0,thickness=0)
for label,url,yy in [('CV de Sofía','https://jahirazael66-pixel.github.io/Presentaciones/presentaciones/adex-cv/cv/CV_Sofia_Mendoza.pdf',407),('CV de Diego','https://jahirazael66-pixel.github.io/Presentaciones/presentaciones/adex-cv/cv/CV_Diego_Salazar.pdf',435),('Formulario de postulación',D['links']['form'],463)]:
 text(label,649,yy,149,12.5,'Bold','blue');c.linkURL(url,(649,H-yy-22,798,H-yy),relative=0,thickness=0)
footer('Pruebas del 3 de noviembre de 2026. Los perfiles finales son ficticios; los enlaces conservan sus permisos de acceso.')
c.save();(T/'layout.json').write_text(json.dumps(bounds));print(OUT,'8 páginas')
