from pathlib import Path
import json,math,io
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from fontTools.ttLib import TTFont as Font
from PIL import Image
R=Path(__file__).resolve().parents[1];D=json.loads((R/'scripts/pdf-data.json').read_text());TMP=R.parent/'tmp/greenbox/pdf';TMP.mkdir(parents=True,exist_ok=True)
for name,file in [('Sans','plus-jakarta-sans/files/plus-jakarta-sans-latin-400-normal.woff'),('Bold','plus-jakarta-sans/files/plus-jakarta-sans-latin-700-normal.woff'),('Serif','fraunces/files/fraunces-latin-500-normal.woff')]:
 f=Font(R/'node_modules/@fontsource'/file);f.flavor=None;f.save(TMP/(name+'.ttf'));pdfmetrics.registerFont(TTFont(name,str(TMP/(name+'.ttf'))))
OUT=R/'public/Greenbox-Triple-Impacto-2027.pdf';W,H=841.89,595.28;M=32;CW=W-64
C={'forest':'#153e2f','ink':'#183b31','cream':'#f6f4ec','mint':'#c8e0b3','sage':'#e4eadc','gold':'#d6a547','coral':'#be6c52','blue':'#8fb4ba','sand':'#eee7d8'}
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1);c.setTitle('Greenbox | Plan de exportación a Alemania | Triple impacto 2027');c.setAuthor(' · '.join(D['team']));page=0;fg=C['ink'];bg=C['cream'];accent=C['forest'];bounds=[]
def rect(x,y,w,h,color,r=0,stroke=None):
 c.setFillColor(HexColor(color));c.setStrokeColor(HexColor(stroke or color));c.roundRect(x,H-y-h,w,h,r,fill=1,stroke=bool(stroke))
def line(x,y,xx,yy,color=None,width=.6,dash=None):
 c.setStrokeColor(HexColor(color or fg));c.setLineWidth(width);c.setDash(dash or []);c.line(x,H-y,xx,H-yy);c.setDash([])
def text(t,x,y,w,size=12.7,font='Sans',color=None,lead=None,align=0):
 t=str(t).replace('→',' > ').replace('−','-').replace('–','-').replace('—','-').replace('≥','mín. ').replace('≤','máx. ').replace('₀','0').replace('₁','1').replace('\n','<br/>')
 p=Paragraph(t,ParagraphStyle('p',fontName=font,fontSize=size,leading=lead or size*1.23,textColor=HexColor(color or fg),alignment=align));_,h=p.wrap(w,10000);p.drawOn(c,x,H-y-h);bounds.append([page,t[:60],x,y,w,h]);assert y+h<H-16,(page,t[:70],y+h);return h

def begin(i,theme='cream',subtitle=None):
 global page,bg,fg,accent
 page=i+1;bg=C[theme];fg=C['cream'] if theme=='forest' else C['ink'];accent=C['mint'] if theme=='forest' else C['forest'];rect(0,0,W,H,bg)
 ch=D['chapters'][D['scenes'][i][1]];text(ch,M,20,CW-60,7.7,'Bold',accent);text(f"{page:02d} / {len(D['scenes'])}",W-84,20,52,8,'Sans',fg,align=2);line(M,47,W-M,47,fg,.4)
 if i>0:text(D['scenes'][i][0],M,61,CW,30,'Serif',lead=35)
 if subtitle:text(subtitle,M,103,CW,11.3)
 return 128 if subtitle else 117

def footer(t=''):
 line(M,H-38,W-M,H-38,fg,.35)
 if t:text(t,M,H-30,CW-45,8.2,'Sans',fg,lead=10)
 text(str(page),W-M-23,H-29,23,8,'Sans',fg,align=2);c.showPage()
def card(title,body,x,y,w,h=None,fill=None):
 pad=12 if h else 0
 if h:rect(x,y,w,h,fill or bg,5,stroke=accent)
 hh=text(title,x+pad,y+pad,w-2*pad,14,'Bold',accent)
 bh=text(body,x+pad,y+pad+hh+9,w-2*pad,12.4)
 if h:assert 2*pad+hh+bh+9<=h,(page,title,'card overflow',2*pad+hh+bh+9,h)
 return 2*pad+hh+bh+9

def photo(name,x,y,w,h):
 im=Image.open(R/'public/assets/images'/name).convert('RGB');iw,ih=im.size;s=max(w/iw,h/ih);cw=w/s;ch=h/s;im=im.crop(((iw-cw)/2,(ih-ch)/2,(iw+cw)/2,(ih+ch)/2));im.thumbnail((round(w*2.1),round(h*2.1)));b=io.BytesIO();im.save(b,'JPEG',quality=86);b.seek(0);c.drawImage(ImageReader(b),x,H-y-h,w,h)

def arrow(x,y,xx,yy,color=None):
 line(x,y,xx,yy,color,1);a=math.atan2(yy-y,xx-x)
 for d in [-.45,.45]:line(xx,yy,xx-5*math.cos(a+d),yy-5*math.sin(a+d),color,1)
def cols(cards,y,columns=3,h=150,gap=17):
 w=(CW-(columns-1)*gap)/columns
 for i,(a,b)in enumerate(cards):card(a,b,M+i%columns*(w+gap),y+i//columns*(h+gap),w,h)

def metric(v,label,x,y,w=180,color=None,size=36):
 text(v,x,y,w,size,'Serif',color or accent,lead=size*1.1);text(label,x,y+size+10,w,11.2)
# 1
begin(0);text('EXPORTACIÓN<br/>A ALEMANIA.',M,93,430,47,'Serif',accent,lead=53);text('Piña deshidratada peruana<br/>para el mercado alemán.',M,226,385,19,'Sans');text('TARMA / CALLAO / HAMBURGO',M,306,400,10,'Bold',accent)
text('Programa de internacionalización con triple impacto · 2027',M,347,375,13)
text('INTEGRANTES',M,407,390,9,'Bold');text('<br/>'.join(D['team']),M,430,390,11.4,lead=18)
photo('greenbox-empaque.jpg',455,92,355,410);footer('Greenbox S.A.C. · Fotografías de su actividad; cifras del programa propuestas para 2027.')
# 2
Y=begin(1);photo('greenbox-campo.jpg',M,Y,350,235);text('Greenbox transforma frutas peruanas en ingredientes para compradores internacionales.',416,Y,394,16,'Serif');text('Acobamba, Tarma · fundada en 2011 según su web. Presencia comercial declarada en Alemania.',416,203,394,12.7)
for i,(v,t)in enumerate([('4','embarques'),('5.000','kg por embarque'),('20 t','anuales')]):metric(v,t,416+i*132,292,125,size=29)
cols([('500+ agricultores','Red reportada por NESsT; no beneficiarios nuevos del programa.'),('40 → 240','Crecimiento de personal de planta reportado por NESsT.'),('Cajas de 10 kg','500 cajas por embarque; un distribuidor alemán propuesto.')],397,h=126)
text('543 t exportadas de piña deshidratada en enero-junio 2025; las 20 t equivalen al 3,68% de ese volumen [G18]. Reservar capacidad y confirmar pedido.',M,535,CW,9.4);footer('Empresa: Greenbox y NESsT [G01–G02]. Volúmenes, comprador y metas: programa propuesto.')
# 3
Y=begin(2,'forest');text('Misión de Greenbox',M,Y,377,16,'Bold',accent);text(D['companyStrategy']['mission'],M,Y+34,365,14.2)
text('Visión de Greenbox',M,265,377,16,'Bold',accent);text(D['companyStrategy']['vision'],M,299,365,14.2)
for i,(v,t)in enumerate([('≥15%','margen de contribución'),('≥95%','pagos oportunos'),('≥80%','residuos valorizados')]):metric(v,t,466,153+i*100,340,size=35)
text('METAS DEL PROGRAMA 2027',466,Y,340,10,'Bold',accent)
line(M,446,W-M,446,fg,.5)
for i,(label,meaning)in enumerate(D['companyStrategy']['connections']):
 xx=M+i*263;text(label,xx,465,246,12.5,'Bold',accent);text(meaning,xx,489,246,12)
footer('Paráfrasis de misión y visión oficiales [G01]. Triple impacto: interpretación. Metas: programa 2027; visión oficial sin año.')
# 4
Y=begin(3);text('Responsabilidad social en la exportación.',M,Y,CW,30,'Serif',lead=36)
cols([('Agricultores','Precio claro y pago puntual. Evidencia: acuerdos y comprobantes.'),('Producto','Inocuidad, origen y continuidad. Evidencia: muestra, análisis y trazabilidad.'),('Ambiente y negocio','Residuos y empaque, margen y liquidez. Evidencia: pesajes, ensayos, constancias y costos.')],192,h=180)
rect(M,412,CW,102,C['sage'],5);text('Condición orgánica',M+16,426,190,15,'Bold');text('Operador, actividad y producto cubiertos; certificado de inspección del envío y gestión en TRACES. Solo así se ofrece como orgánico.',M+220,427,CW-236,12.4)
footer('Reglamento (UE) 2018/848 y controles de importación [G04–G05, G10]. Cumplir no garantiza prima de precio.')
# 5
Y=begin(4,'sage','Actores internos y externos, con expectativas y relación con el programa')
text('Stakeholders internos',M,Y,340,20,'Serif');text('Stakeholders externos',420,Y,388,20,'Serif')
inside=[a for a in D['actors']if a['type']=='Interno'];outside=[a for a in D['actors']if a['type']=='Externo']
for group,xx in [(inside,M),(outside,429)]:
 for i,a in enumerate(group):
  yy=Y+46+i*84;line(xx,yy+74,xx+380,yy+74,fg,.3);text(a['id']+' · '+a['name'],xx,yy,376,12.2,'Bold');text(a['need'],xx,yy+33,376,12.1);text(a['relation']+' · '+a['process'],xx,yy+54,376,10.5)
footer('Internos de la cadena: agricultores, envases, dirección y personal. Externos: comprador, autoridades, NESsT y auditor.')
# 6
Y=begin(5);x=61;y=Y;w=365;h=335
for i,col in enumerate([C['sage'],C['mint'],C['cream'],C['sand']]):rect(x+i%2*w/2,y+i//2*h/2,w/2,h/2,col,0,stroke=C['forest'])
for t,xx,yy in [('Mantener satisfechos',x+10,y+12),('Administrar de cerca',x+w/2+60,y+h/2-40),('Monitorear',x+10,y+h-30),('Mantener informados',x+w/2+10,y+h-43)]:text(t,xx,yy,w/2-70 if t.startswith('Administrar') else w/2-20,9.1 if t.startswith('Administrar') else 10.2,'Bold')
for a in D['actors']:
 xx=x+a['x']/100*w;yy=y+h-a['y']/100*h;c.setFillColor(HexColor(C['forest'] if a['type']=='Interno' else C['gold']));c.circle(xx,H-yy,12,fill=1,stroke=0);text(a['id'],xx-10,yy-5.5,20,7.8,'Bold',C['cream'] if a['type']=='Interno' else C['forest'],align=1)
text('Interés bajo → alto',x,y+h+13,w,10,align=1);c.saveState();c.translate(x-19,H-y-h/2);c.rotate(90);c.setFillColor(HexColor(fg));c.setFont('Sans',9);c.drawCentredString(0,0,'Poder de influencia: bajo a alto');c.restoreState()
for i,a in enumerate(D['actors']):
 yy=Y+i*46;text(a['id'],460,yy,27,10,'Bold');text(a['name'],495,yy,313,10.8,'Bold');text(f"{a['type']} · {a['relation']} · poder {a['power'].lower()} / interés {a['interest'].lower()}",495,yy+17,313,9.2)
text('Niveles medios en las líneas centrales. Posiciones cualitativas, no puntajes medidos.',61,502,750,10.6)
footer('La estrategia depende de expectativas, capacidad de condicionar la operación y afectación por el programa.')
# 7
Y=begin(6,'forest');positions=[(100,164),(260,164),(420,164),(580,164),(740,164),(740,278),(580,278),(420,278),(260,278)]
for i,(x,y) in enumerate(positions[:-1]):
 xx,yy=positions[i+1];same=y==yy;dx=1 if xx>x else -1;arrow(x+(64*dx if same else 0),y+(0 if same else 28),xx-(64*dx if same else 0),yy-(0 if same else 28))
for i,((a,b,desc,ev),(x,y))in enumerate(zip(D['steps'],positions)):
 if i==4:
  p=c.beginPath();p.moveTo(x,H-y+36);p.lineTo(x+65,H-y);p.lineTo(x,H-y-36);p.lineTo(x-65,H-y);p.close();c.setFillColor(HexColor(C['gold']));c.drawPath(p,fill=1,stroke=0)
 else:rect(x-64,y-29,128,58,C['cream'],28 if i==8 else 5)
 text(str(i+1).zfill(2),x-56,y-22,112,7.8,'Bold',C['forest'],align=1);text(a,x-59,y-7,118,10.1,'Bold',C['forest'],lead=12,align=1)
arrow(740,128,740,113,C['gold']);line(740,113,420,113,C['gold'],1,dash=[4,3]);arrow(420,113,420,135,C['gold']);text('No: retener, corregir y reevaluar',472,98,230,8.5,'Sans',C['mint']);text('Sí: liberar',750,214,55,8.4,'Sans',C['mint'])
text('Recortes limpios → ingrediente  /  Cáscara y corazón → compostaje documentado',M,332,CW,10.7,'Bold',accent)
for i,(a,b,desc,ev)in enumerate(D['steps']):
 xx=M+i%3*263;yy=367+i//3*54;text(f'{i+1}. {b}',xx,yy,246,10.6,'Bold',accent);text(ev,xx,yy+17,246,10.3)
footer('Rectángulo: actividad; rombo: decisión; cápsula: cierre. No recuperar fruta deteriorada ni ocultar un rechazo sanitario.')
# 8
Y=begin(7);rect(74,139,185,190,C['mint'],10,stroke=C['forest']);text('GREENBOX',85,169,163,12,'Bold',align=1);text('PIÑA<br/>DESHIDRATADA',85,207,163,16,'Serif',lead=21,align=1);text('10 kg',85,277,163,15,'Bold',align=1)
rect(57,347,228,73,'#d8c49a',4,stroke='#9a815a');text('CAJA DE CARTÓN',65,361,212,10.5,'Bold',align=1);text('40 × 30 × 25 cm',65,385,212,13,align=1);rect(45,437,252,25,'#b9a276',2);text('Pallet 120 × 100 cm',49,475,244,11,align=1)
for i,(a,b)in enumerate([('Bolsa alimentaria','PE preferentemente monomaterial. Validar barrera, migración, sellado y vida útil; si no conserva el alimento, elegir otra barrera.'),('Caja y transporte','Cartón sin laminado; probar compresión, apilamiento y humedad. Estiba estable y madera con requisitos fitosanitarios.'),('Recuperación en Alemania','Definir productor responsable, registro LUCID y obligaciones con el importador. La reciclabilidad depende del diseño y recuperación real.')]):card(a,b,351,Y+i*125,457)
footer('Esquema propuesto. Contacto alimentario: CE 1935/2004 y UE 10/2011 [G03]; envases UE 2025/40 y LUCID [G06–G07].')
# 9
Y=begin(8,'sage');metric('1.000 kg','piña fresca recibida',M,Y,230,size=37)
flows=[('100 kg','producto alimentario','90 kg principales + 10 kg de recortes limpios.',C['gold']),('450 kg','cáscara y corazón','360 kg a compostaje acreditado + 90 kg pendientes.',C['mint']),('450 kg','agua retirada','Evaporación durante el secado; no es residuo valorizado.',C['blue'])]
for i,(a,b,desc,color)in enumerate(flows):
 yy=Y+i*111;arrow(250,162,360,yy+35,C['forest']);rect(365,yy,443,96,color,5);text(a,382,yy+12,150,27,'Serif',lead=30);text(b,540,yy+14,251,13,'Bold');text(desc,382,yy+53,409,11.6)
metric('80%','valorización orgánica',M,305,230,size=59);text('360 / 450 × 100',M,416,240,16,'Bold');text('1.000 = 100 + 450 + 450 kg',M,470,CW,16,'Serif');text('Para 20.000 kg principales: 222.222 kg frescos/año; 55.556 kg por embarque; 2.222 kg de recortes sin ingresos previstos. Rendimiento supuesto: 9%.',M,508,CW,10.4)
footer('Balance ilustrativo, no rendimiento medido de Greenbox. Harina de cáscara: evaluación futura, sin ingresos presupuestados. [G01]')
# 10
Y=begin(9);text('TARMA → CALLAO → HAMBURGO → DISTRIBUIDOR',M,Y,CW,13,'Bold',accent)
rect(58,181,300,250,'#ddcea7',4);boxes=[]
for rr in range(2):
 for cc in range(3):boxes.append((cc*40,rr*30,40,30))
for cc in range(4):boxes.append((cc*30,60,30,40))
for i,(x,y,w,h)in enumerate(boxes):rect(60+x*2.5,183+y*2.5,w*2.5-4,h*2.5-4,C['mint'],3,stroke='#78976a');text(str(i+1),60+x*2.5,183+y*2.5+h*1.25-7,w*2.5-4,10,align=1)
text('Vista superior: 10 cajas por nivel',58,447,300,11.5,align=1);text('Pallet 120 × 100 cm · 5 niveles · altura 1,40 m',58,477,300,10.6,align=1)
for i,(a,b)in enumerate([('5.000 kg','producto por embarque'),('500 cajas','10 kg por caja'),('10 pallets','50 cajas por pallet'),('16,8 m³','volumen paletizado')]):metric(a,b,414+i%2*197,177+i//2*109,180,size=29)
text('Intensidad = kg CO2e de Tarma al almacén alemán / kg principal entregado. Meta -5% frente al primer embarque, con alcance comparable y datos acordados con el comprador.',414,415,394,11.7)
footer('15 m³ en cajas, 16,8 m³ paletizados; no demuestra ocupación de contenedor. Validar peso bruto, resistencia y vida útil. [G08]')
# 11
Y=begin(10,'sand');text('Registros<br/>y responsables.',M,Y,330,39,'Serif',lead=46);text('Los compromisos se convierten en hábitos: formación, registros fiables y respuestas a tiempo.',M,256,330,15)
rows=[('Antes del primer lote','Inducción pagada y práctica aprobada sobre trazabilidad, segregación y registros.'),('Cada semana','Producción se reúne; finanzas revisa pagos. Señalización y registros por lote.'),('Cada mes','Dirección revisa seis metas y acuerda correcciones con responsables.'),('En cinco días hábiles','Respuesta inicial del canal reservado de reclamos; seguimiento sin represalias.')]
for i,(a,b)in enumerate(rows):card(a,b,409,Y+i*105,399)
footer('Responsables: calidad, producción, finanzas y dirección; participación de trabajadores y proveedores.')
# 12
Y=begin(11,'forest');cols([('Documentos para el distribuidor','Ficha técnica y análisis.<br/><br/>Trazabilidad y especificaciones del empaque.<br/><br/>Certificados aplicables y reporte trimestral de impacto.'),('Información para el consumidor','QR coordinado con la marca alemana que fracciona el producto.<br/><br/>Origen, lote y evidencia disponible.<br/><br/>El QR no reemplaza la información obligatoria.')],Y,columns=2,h=280,gap=30)
text('Comunicar resultados, no promesas absolutas.',M,444,CW,24,'Serif',accent);text('Calidad aprueba afirmaciones; finanzas valida pagos. Precisar período y alcance. Evitar «cero impacto».',M,486,CW,12.7)
footer('El operador responsable valida la información alimentaria conforme al Reglamento (UE) 1169/2011. [G09]')
# 13
Y=begin(12,subtitle='Tablero resumido: dos metas por dimensión, con responsables y evidencia')
colors=[C['gold'],C['mint'],'#efdbd1'];cw=(CW-34)/3
for i,k in enumerate(D['kpis']):
 xx=M+i*(cw+17);rect(xx,Y,cw,252,colors[i],5);text(k['dimension'],xx+16,Y+17,cw-32,15,'Bold')
 for j,(v,t,f,who)in enumerate(k['items']):text(v,xx+16,Y+59+j*94,cw-32,32,'Serif',lead=36);text(t,xx+16,Y+100+j*94,cw-32,12.4)
 lines=['Contribución / ventas; kg aceptados / 20.000. Finanzas: ventas, costos y recepción.','kg valorizados / residuos generados; reducción de kg de empaque/kg de producto. Calidad: pesajes, piloto y constancias.','Facturas puntuales / facturas vencidas de la misma población; personal que aprueba / asignado. Finanzas y RR. HH.']
for i,b in enumerate(lines):text(b,M+i*(cw+17),410,cw,11.3)
footer('Metas 2027, no resultados. Cierre mensual y anual; denominador cero: «no aplica». Empaque con protección equivalente.')
# 14
Y=begin(13,'sage');cols([('Inocuidad','BRCGS Food Safety: revisar vigencia, alcance, planta y organismo aprobado. SGS: candidata a cotizar.<br/><br/><b>Antes del primer embarque.</b>'),('Condición orgánica','Organismo reconocido para la UE; revisar operador, producto y certificado de inspección.<br/><br/><b>Cada envío.</b>'),('Ambiente e indicadores','Evaluar ISO 14001:2026 entre meses 12–24. Firma independiente revisa los KPIs.<br/><br/><b>Seguimiento y cierre anual.</b>')],Y,h=270)
text('Alcance de cada verificación',M,432,CW,25,'Serif');text('Inocuidad, pagos y emisiones requieren evidencias distintas. NESsT no reemplaza al auditor independiente.',M,477,CW,13)
footer('La ficha comercial no sustituye revisar certificados [G11–G13]. ISO 14001:2026 es una evaluación propuesta. [G14]')
# Certificaciones: todos los distintivos visibles, sin interacciones necesarias.
Y=begin(14,subtitle='Inocuidad, producción orgánica, requisitos alimentarios y comercio justo')
w=(CW-36)/4;h=178
for i,(file,name,category,detail)in enumerate(D['certificates']):
 xx=M+i%4*(w+12);yy=Y+i//4*(h+14);rect(xx,yy,w,h,'#ffffff',5,stroke=C['sage'])
 im=Image.open(R/'public/assets/images/aportadas'/file).convert('RGBA');iw,ih=im.size;scale=min((w-36)/iw,67/ih);dw,dh=iw*scale,ih*scale
 im.thumbnail((max(1,round(dw*2.5)),max(1,round(dh*2.5))));c.drawImage(ImageReader(im),xx+(w-dw)/2,H-yy-12-(67+dh)/2,dw,dh,mask='auto')
 text(category,xx+12,yy+88,w-24,8.7,'Bold','#52723f');text(name,xx+12,yy+108,w-24,13,'Bold');text(detail,xx+12,yy+133,w-24,10.6)
text('Greenbox declara BRCGS, USDA Organic, EU Organic, Bio Suisse, Kosher y Fairtrade [G16]. SIAL menciona HACCP+ [G13]. JAS: referencia para Japón [G17].',M,519,CW,9.1)
footer('Cada sello tiene un alcance distinto; revisar producto y actividad cubiertos en el certificado correspondiente.')
# 15
Y=begin(15,subtitle='20.000 kg principales · precio base FCA USD 8/kg · costo variable USD 6,40/kg')
for i,(label,value)in enumerate(D['variableCosts']):
 xx=M+i*(CW/5);text(label,xx,Y,CW/5-10,9.5,'Bold');text(f'USD {value:.2f}/kg',xx,Y+23,CW/5-10,12)
for i,(price,sales,cont,margin,title)in enumerate([(8,160000,32000,'20%','Escenario base'),(7.2,144000,16000,'11,1%','Precio -10%')]):
 xx=M+i*397;text(title,xx,Y+76,380,17,'Bold');text(f'USD {price:.2f} / kg',xx,Y+104,380,12)
 width=365;rect(xx,Y+136,width*128000/sales,42,'#b7c3a5',3);rect(xx+width*128000/sales,Y+136,width*cont/sales,42,C['gold']if i==0 else C['coral'],3)
 text(f'Ventas ${sales:,.0f} · variables $128.000',xx,Y+195,380,11.5);text(f'Contribución ${cont:,.0f} · margen {margin}',xx,Y+220,380,13,'Bold')
 text(f'Saldo tras adicionales: ${cont-10000:,.0f}',xx,Y+250,380,13,'Bold')
text('Adicionales anuales: USD 10.000',M,451,CW,16,'Bold');text('Gestión comercial $4.000 · piloto de empaque $3.000 · auditoría de KPIs $3.000.',M,481,CW,11.5)
text('A $8/kg: saldo $22.000; 6.250 kg cubren adicionales. Antes de financiación, impuestos y fijos existentes.',M,513,CW,10.8)
footer('Costos supuestos, no cotizaciones. No es utilidad neta. FCA: el comprador contrata el transporte principal [G15].')
# 16
Y=begin(16,'sand');rows=[('1 · Acordar','Muestra, precio y entrega.','Comercial + comprador','Muestra y condiciones aceptadas.'),('2 · Validar','Empaque, inocuidad y vida útil.','Calidad + proveedor','Piloto y especificación aprobados.'),('3 · Documentar','Residuos y responsabilidades.','Operaciones + importador','Aprovechamiento acreditado y roles definidos.'),('4 · Medir','Tablero y correcciones.','Finanzas + calidad + RR. HH.','Seis metas revisadas con evidencia.'),('5 · Revisar','Resultados del programa.','Dirección + actores clave','Revisión trimestral y verificación anual.')]
for i,(a,b,who,ev)in enumerate(rows):
 yy=Y+i*77;line(M,yy+66,W-M,yy+66,fg,.4);text(a,M,yy,155,15,'Bold');text(b,202,yy,270,12.4);text(who,202,yy+30,270,9.8);text(ev,502,yy,306,12)
footer('Confirmar pedido y capacidad. Comparar cuatro envíos de 5 t con dos de 10 t. Recortes y compostaje antes de harina.')
# 17
Y=begin(17,'forest');text('Rentabilidad,<br/>personas<br/>y ambiente.',M,Y,370,46,'Serif',accent,lead=52);text('Rentabilidad, personas y ambiente deben avanzar juntos.',M,345,340,17)
for i,(a,b)in enumerate([('Viabilidad comercial','Muestra aprobada, precio viable y condiciones de entrega claras.'),('Operación controlada','Producto seguro, empaque apto y trazabilidad de cada lote.'),('Impacto demostrable','Pagos oportunos, aprovechamiento acreditado y equipo formado.')]):card(a,b,430,Y+i*133,378,116)
footer('El margen debe sostener los compromisos sociales y ambientales del programa.')
# 18
Y=begin(18);per=9
for i,(id,t,u)in enumerate(D['sources']):
 xx=M+(i//per)*397;yy=Y+(i%per)*47;text(id,xx,yy,35,9.5,'Bold');hh=text(t,xx+41,yy,339,11.5);c.linkURL(u,(xx,H-yy-hh,xx+380,H-yy),relative=0,thickness=0)
footer('Fuentes externas enlazadas. Fotografías y logo: recursos de Greenbox y material facilitado por el usuario. Visualizaciones propias.')
c.save();(TMP/'layout.json').write_text(json.dumps({'pages':len(D['scenes']),'bounds':bounds},ensure_ascii=False));print(OUT,len(D['scenes']),'páginas')
