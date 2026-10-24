from pathlib import Path
import json,re,math,io
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from fontTools.ttLib import TTFont as FTFont
from PIL import Image
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/Fundas-textiles-peruanas.pdf';OUT.parent.mkdir(exist_ok=True)
TMP=ROOT.parent/'tmp/pdfs';TMP.mkdir(parents=True,exist_ok=True)
for name,p in [('Sans','dm-sans/files/dm-sans-latin-400-normal.woff'),('Bold','dm-sans/files/dm-sans-latin-700-normal.woff'),('Serif','cormorant-garamond/files/cormorant-garamond-latin-600-normal.woff')]:
 font=FTFont(ROOT/'node_modules/@fontsource'/p);font.flavor=None;font.save(TMP/(name+'.ttf'));pdfmetrics.registerFont(TTFont(name,str(TMP/(name+'.ttf'))))
W,H=841.89,595.28;M=32;CW=W-2*M
C={'linen':'#F4EEDD','wine':'#8F2942','orange':'#C45224','gold':'#D4A448','teal':'#79A7A1','purple':'#44304E','ink':'#2A2425','sand':'#E7DBC3'}
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1);c.setTitle('Fundas textiles peruanas | Propuesta de negocio para Nueva York');c.setAuthor('Presentación de propuesta de negocio')
fg=C['ink'];bg=C['linen'];accent=C['wine'];page=0
bounds=[]
def rect(x,y,w,h,color,r=0,stroke=None):
 c.setFillColor(HexColor(color));c.setStrokeColor(HexColor(stroke or color));c.roundRect(x,H-y-h,w,h,r,stroke=bool(stroke),fill=1)
def line(x1,y1,x2,y2,color=None,width=1,dash=None):
 c.setStrokeColor(HexColor(color or fg));c.setLineWidth(width);c.setDash(dash or []);c.line(x1,H-y1,x2,H-y2);c.setDash([])
def text(t,x,y,w,size=11.5,font='Sans',color=None,leading=None,align=0):
 t=t.replace('−','-').replace('–','-').replace('—','-').replace('≤','hasta ').replace('≥','al menos ').replace('→',' > ').replace('\n','<br/>')
 original_size=size
 if font=='Sans' and 9.5<=size<=15:size=max(12.6,size*1.18)
 elif font=='Sans' and size<9.5:size=max(8.5,size*1.17)
 elif font=='Bold' and size<=15:size=max(11,size*1.15)
 elif font=='Serif' and size<10:size=9.5
 st=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading or size*1.22,textColor=HexColor(color or fg),alignment=align,spaceAfter=0)
 p=Paragraph(t,st);_,h=p.wrap(w,10000);p.drawOn(c,x,H-y-h);bounds.append((page,t[:50],x,y,w,h));assert y+h<=H-16,(page,t[:80],y+h);return h

def title(t,eyebrow=None,theme='linen',index=None):
 global fg,bg,accent,page
 page+=1;bg=C[theme];fg=C['linen'] if theme in ['wine','purple'] else C['ink'];accent=C['gold'] if theme in ['wine','purple'] else C['wine'];rect(0,0,W,H,bg)
 text('FUNDAS TEXTILES · PERÚ / NUEVA YORK',M,21,500,8,'Bold',accent)
 text(f'{index or page:02d} / 20',W-95,21,63,8,'Sans',fg,align=2)
 line(M,42,W-M,42,fg,.5);text(t,M,53,CW,32,'Serif',leading=36)
 if eyebrow:text(eyebrow,M,94,CW,10,'Sans',fg)
 return 123 if eyebrow else 108

def foot(t=''):
 line(M,H-39,W-M,H-39,fg,.4)
 if t:text(t,M,H-31,CW-45,7.4,'Sans',fg,leading=9)
 text(str(page),W-M-26,H-30,26,8,'Sans',fg,align=2);c.showPage()
def card(t,b,x,y,w,h=None,color=None):
 if h:rect(x,y,w,h,color or bg,3,stroke=accent)
 pad=10 if h else 0;th=text(t,x+pad,y+pad,w-2*pad,12,'Bold',accent);bh=text(b,x+pad,y+pad+th+7,w-2*pad,10.8)
 if h:assert th+bh+2*pad+7<=h,(page,t,'card overflow',th+bh+2*pad+7,h)
 return pad+th+7+bh+pad

def grid(cards,y,cols=3,h=136,gap=16):
 w=(CW-gap*(cols-1))/cols
 for i,(a,b) in enumerate(cards):card(a,b,M+(i%cols)*(w+gap),y+(i//cols)*(h+gap),w,h)
 return y+math.ceil(len(cards)/cols)*(h+gap)
def photo(n,x,y,w,h,cap=True):
 im=Image.open(ROOT/f'public/images/amahi-{n}.webp').convert('RGB');iw,ih=im.size;scale=max(w/iw,h/ih);cropw=w/scale;croph=h/scale;left=(iw-cropw)/2;top=(ih-croph)/2;im=im.crop((left,top,left+cropw,top+croph));im.thumbnail((round(w*2.2),round(h*2.2)));b=io.BytesIO();im.save(b,format='JPEG',quality=85);b.seek(0);c.drawImage(ImageReader(b),x,H-y-h,w,h)
 if cap:text('AMAHÍ · referencia visual; no producto propio',x,y+h+5,w,7,'Sans')
def stats(items,y,h=85):
 w=CW/len(items)
 for i,(a,b) in enumerate(items):text(a,M+i*w,y,w-12,31,'Serif',accent,leading=34);text(b,M+i*w,y+40,w-15,10)
 line(M,y+h,W-M,y+h,fg,.5)
def table(rows,x,y,width,rowh=29,left=.68):
 for i,(a,b) in enumerate(rows):
  yy=y+i*rowh;line(x,yy+rowh-3,x+width,yy+rowh-3,fg,.3);text(a,x,yy,width*left,10.6);text(b,x+width*(left+.01),yy,width*(.99-left),10.6,'Bold',accent,align=2)
 return y+len(rows)*rowh

def arrows(points,color=None):
 for (x1,y1),(x2,y2) in zip(points,points[1:]):line(x1,y1,x2,y2,color,1)
 x1,y1=points[-2];x2,y2=points[-1];a=math.atan2(y2-y1,x2-x1);length=5
 line(x2,y2,x2-length*math.cos(a-.5),y2-length*math.sin(a-.5),color);line(x2,y2,x2-length*math.cos(a+.5),y2-length*math.sin(a+.5),color)

# 01
pagey=title('Fundas textiles peruanas',theme='linen')
text('Diseño, calidad y una ruta<br/>comercial completa.',M,125,390,32,'Serif',accent)
text('Propuesta de negocio: una colección de fundas decorativas interiores para tiendas y estudios de Nueva York.',M,235,350,14)
photo(1,443,117,365,345)
for i,(a,b) in enumerate([('18 × 18 in','45,72 × 45,72 cm'),('B2B','venta por lote'),('Lima / NYC','producción tercerizada')]):
 text(a,M+i*127,369,120,22,'Serif',accent);text(b,M+i*127,408,120,9)
text('Integrantes',M,448,375,12,'Bold',accent)
text('Maria Fernanda Ruiz Luna<br/>Jahir Azael Castillo Paucas<br/>Jostin Chavez Estela',M,470,375,11.5,leading=18)
foot('Producto propuesto sin relleno. Colección propia por desarrollar. Fotografías de referencia identificadas.')
# 02
Y=title('Resumen ejecutivo','1 · Qué se ofrece, a quién y bajo qué condiciones')
grid([('Producto','Fundas de algodón propuesto, con cierre, sin relleno. Tres diseños coordinados en un lote piloto de 60.'),('Cliente','Tiendas independientes y estudios que compran directamente en Nueva York. El usuario final no es el comprador inicial.'),('Operación','Microempresa en Lima: diseña, comercializa y controla calidad. Un taller tercero confecciona; no se instala fábrica.')],Y,h=170)
stats([('$28','precio B2B por funda'),('60','unidades por pedido'),('$7.000','capital inicial'),('2 pilotos','pagados en 90 días')],341)
text('Condición de avance: comprador pagado + producto apto + costo de llegada aceptado. Validar las tres antes de producir.',M,467,CW,14,'Bold',accent)
foot('Escenario de prefactibilidad: cifras y metas de planificación, no ventas contratadas.')
# 03
Y=title('Oportunidad de negocio',theme='wine')
text('Del textil<br/>al espacio.',M,Y,330,42,'Serif',accent,leading=46)
text('La oportunidad no depende solo del origen peruano: requiere una colección distinta, calidad repetible y reposición.',M,Y+115,330,15)
for j,(a,b) in enumerate([('Necesidad','Una colección con identidad, suministro confiable y margen para revender.'),('Respuesta','Tres diseños propios, ficha técnica, muestra aprobada y costos claros.'),('Prueba','Que una cuenta compre al precio completo y luego quiera reponer.')]):card(a,b,430,Y+j*117,378,104)
foot('No se cultiva algodón ni se instala fábrica. Diseño, venta y calidad se coordinan desde Lima.')
# 04
Y=title('Producto y ficha técnica','3 · Funda decorativa interior para adultos, sin relleno')
# own schematic
rect(58,170,238,238,C['wine'],14)
for row in range(7):
 for col in range(7):
  cx=75+col*32;cy=187+row*32
  p=c.beginPath();p.moveTo(cx,H-cy+11);p.lineTo(cx+11,H-cy);p.lineTo(cx,H-cy-11);p.lineTo(cx-11,H-cy);p.close();c.setFillColor(HexColor(C['gold'] if (row+col)%2 else C['teal']));c.drawPath(p,fill=1,stroke=0)
line(58,151,296,151,fg);text('18 in · 45,72 cm',62,130,238,12,'Bold',align=1)
text('Frente ilustrativo · patrón propio',55,420,250,10,align=1);text('Cierre en reverso. Tolerancia y ajuste al inserto se acuerdan tras la muestra.',55,446,250,10)
rows=[('Medida nominal','18 × 18 in = 45,72 × 45,72 cm'),('Colección piloto','3 diseños × 20 = 60 fundas'),('Material propuesto','Paneles de algodón y avíos documentados'),('Calidad objetivo','Encogimiento ≤3%; color, costura y cierre'),('Ensayo dimensional','ISO 6330: lavado / ISO 5077: cambio dimensional'),('Ensayo de color','ISO 105-X12: solidez al frote')]
for i,(a,b) in enumerate(rows):card(a,b,355,129+i*62,453)
foot('La meta ≤3% no es límite legal ni resultado logrado. Ensayos de referencia no equivalen a certificación. [E23–E24, E41–E43]')
# 05
Y=title('Propuesta de valor',theme='sand')
for i,(a,b) in enumerate([('Identidad','Colección coordinada y diseño propio. El origen peruano por sí solo ya existe en la oferta competidora.'),('Repetibilidad','Ficha, muestra y control de lote para reducir diferencias y facilitar la reposición.'),('Claridad','Precio, plazo, transporte y responsabilidades definidos antes de recibir el anticipo.')]):card(a,b,M,Y+i*116,365)
photo(3,430,110,378,166)
for i,n in enumerate([4,5,6]):photo(n,430+i*129,302,120,120,False)
text('Referencias de diseño AMAHÍ; no acreditan composición, técnica ni certificaciones del producto propuesto.',430,435,378,9)
text('Frente a un genérico: competir por colección y servicio, no por precio mínimo. Acordar derechos de diseño y exclusividad por zona, volumen y plazo.',430,478,378,10.5,'Bold',accent)
foot('[E05–E08, E11] La exclusividad y la reposición son condiciones a negociar, no compromisos automáticos.')
# 06
Y=title('Tendencias y comprador','4 · Consumer Trend Canvas y empatía',theme='purple')
grid([('Cambio observado','Oferta de textiles con identidad y colecciones coordinadas en canales de decoración.'),('Aplicación propuesta','Colores con carácter, ficha precisa y lotes pequeños planificados. Validar la aceptación en entrevistas.'),('Empatía del comprador','Piensa: “¿encaja en mi colección?”. Teme cambios de calidad y costos sorpresa. Necesita muestra, información y margen.')],Y,h=172)
grid([('Comprador B2B','Tienda o estudio que paga: evalúa margen, rotación, calidad y reposición.'),('Usuario final','Decora su espacio: valora combinación visual, tacto y facilidad de cuidado.'),('Prescriptor','Diseñador que recomienda sin comprar. Influye, pero no cuenta como cliente facturable.')],Y+191,h=148)
foot('Lectura cualitativa por contrastar; no encuesta realizada. [E06–E13]')
# 07
Y=title('Mercado y competencia','5 · EE. UU., categoría HS 630492; segmento inicial: Nueva York')
text('Importaciones de una categoría amplia',M,Y,370,12,'Bold',accent)
for i,(lab,val) in enumerate([('2023',161.7375),('2024',165.10541)]):
 x=85+i*155;h=val/180*166;rect(x,341-h,89,h,C['wine'] if i==0 else C['orange'],4);text(f'${val:.2f} M',x-15,341-h-24,119,12,'Bold',align=1);text(lab,x,350,89,11,align=1)
text('+2,08%',M,384,330,36,'Serif',accent);text('India + China: 79,13%. Perú: $11.730 en 2024. El plan de $40.320 = 3,44 veces esa referencia; no es participación confirmada.',M,434,355,11)
text('Competencia y acceso al canal',432,Y,376,14,'Bold',accent)
card('Canvastry','Genérico 18 × 18: $9 por 50–99; $8,75 por 100–199.',432,Y+37,376)
card('AMAHÍ / Aklla / Coterie','Diseño peruano y mayorista; Coterie presenta variantes desde $53 / $58. No son productos idénticos.',432,Y+113,376)
card('Segmento y cuentas potenciales','Tiendas y estudios con compra directa, estilo compatible e importador definido. The Primary Essentials y BEAM son ejemplos de canal; no clientes confirmados.',432,Y+205,376)
text('Home Deco Perú 2025: aprox. $7,2 M global; EE. UU. -12,1%. Es otra serie, distinta del HS 630492.',432,477,376,10)
foot('Datos y precios del informe, corte 23/10/2026, no cotizaciones actuales. Categoría amplia, no solo fundas. [E01–E10]')
# 08
Y=title('Validación y demanda','6 · Primero una venta pagada; después, una cartera que repita',theme='sand')
text('Piloto de 90 días',M,Y,260,15,'Bold',accent)
for i,(a,b) in enumerate([('30','cuentas calificadas'),('8–12','entrevistas útiles'),('3+','cuentas evalúan muestras'),('2','pilotos pagados')]):text(a,M,Y+43+i*65,90,29,'Serif',accent);text(b,128,Y+55+i*65,177,11.5)
text('12 compradores × 2 pedidos × 60 = 1.440 fundas/año',335,Y,473,19,'Serif',accent)
vals=[0,0,60,60,120,120,120,180,180,180,180,240]
for i,v in enumerate(vals):
 x=342+i*38;h=v/240*176;rect(x,368-h,25,max(h,1),C['wine'] if i%2==0 else C['orange'],2);text(str(v),x-5,368-h-18,35,8.7,'Bold',align=1);text(f'M{i+1}',x-5,380,35,8.7,align=1)
text('Capacidad objetivo 240/mes: utilización anual 50%. Rampa propuesta, no ventas contratadas.',335,415,473,11)
text('Embudo anual ilustrativo: 120 cuentas → 36 respuestas → 18 evaluaciones → 12 compradores, más 12 recompras.',335,466,473,11,'Bold',accent)
foot('Muestra dirigida, no representativa. Registrar objeciones, precio aceptado y voluntad de compra.')
# 09
Y=title('Modelo de negocio','7 · Business Model Canvas: nueve componentes',theme='wine')
bm=[('Socios','Taller, tela y avíos; laboratorio, operador y contador.'),('Actividades','Diseñar, aprobar muestras, vender, controlar y exportar.'),('Recursos','Diseños, ficha, muestra, proveedores y caja.'),('Propuesta de valor','Colección coordinada, calidad repetible y costo claro.'),('Relación','Atención directa y aprobación documentada; seguimiento.'),('Canales','Prospección, catálogo, muestras y transportista.'),('Clientes','Tiendas y estudios de Nueva York con compra directa.'),('Costos','Producto, cobro, incidencias, salida local y estructura.'),('Ingresos','Venta por lote; muestras y transporte bajo acuerdo.')]
grid(bm,Y,cols=3,h=124,gap=12)
foot('La calidad y la caja atraviesan los nueve bloques; no se supone fábrica propia. [E12]')
# 10
Y=title('Plan comercial','8 · Del primer contacto a la recompra')
j=[('Descubrir','Catálogo y contacto. Comercial: respuesta.'),('Evaluar','Ficha y muestras. Producto: muestra evaluada.'),('Negociar','Precio y llegada. Comercial: oferta aceptada.'),('Ordenar','50% anticipo. Finanzas: pago recibido.'),('Producir','Muestra y lote. Operaciones: conformidad.'),('Despachar','Saldo y FCA. Operaciones: entrega registrada.'),('Recibir','Incidencias. Comercial: recepción confirmada.'),('Recomprar','Reposición. Comercial: nuevo pedido.')]
grid([(str(i+1)+' · '+a,b)for i,(a,b)in enumerate(j)],Y,cols=4,h=112,gap=12)
card('Condiciones','50% al ordenar + 50% antes de FCA. Plazo propuesto 30–45 días desde aprobación y anticipo. Muestras, transporte, vigencia de oferta y exclusividad se acuerdan.',M,392,370)
card('Adquisición modelada','$4.200/año ÷ 12 compradores = $350 por comprador. Ya incluido en fijos. Dos pedidos de 60 aportan $1.492 antes de fijos; no deducir adquisición dos veces.',438,392,370)
foot('Recorrido del cliente y prospección comercial. Evitar consignación y crédito largo al inicio. [E13, E30]')
# 11
Y=title('Cadena de producción','9 · Flujograma completo: actividad, decisión y cierre',theme='purple')
nodes=[('Diseñar',85,158),('Abastecer',245,158),('Prototipar',405,158),('¿Aprobado?',565,158),('Ajustar',725,158),('Orden + anticipo',565,225),('Confeccionar',405,225),('Inspeccionar',245,225),('¿Conforme?',85,225),('Retener / corregir',85,292),('Etiquetar / empacar',245,292),('Cobrar saldo',405,292),('Entregar FCA',565,292),('Recepción / recompra',725,292)]
for a,b in [(0,1),(1,2),(2,3),(3,4),(3,5),(5,6),(6,7),(7,8),(8,9),(8,10),(10,11),(11,12),(12,13)]:
 A=nodes[a];B=nodes[b];same=A[2]==B[2];dx=1 if B[1]>A[1] else -1;arrows([(A[1]+(53*dx if same else 0),A[2]+(0 if same else 21)),(B[1]-(53*dx if same else 0),B[2]-(0 if same else 21))],fg)
for i,(t,x,y)in enumerate(nodes):
 if i in [3,8]:
  p=c.beginPath();p.moveTo(x,H-y+27);p.lineTo(x+56,H-y);p.lineTo(x,H-y-27);p.lineTo(x-56,H-y);p.close();c.setFillColor(HexColor(C['gold']));c.drawPath(p,fill=1,stroke=0)
 else:rect(x-53,y-20,106,40,C['linen'],18 if i==13 else 4)
 text(f'{i+1:02d} · {t}',x-49,y-9,98,7.9,'Bold',C['ink'],leading=10,align=1)
arrows([(725,138),(725,126),(405,126),(405,138)],C['gold']);arrows([(85,312),(85,327),(405,327),(405,245)],C['gold']);text('No',641,141,30,8,'Bold',C['gold']);text('Sí',573,188,30,8,'Bold',C['gold']);text('No',94,253,30,8,'Bold',C['gold']);text('Sí',153,255,30,8,'Bold',C['gold'])
shorts=[('1–3 · Preparar','Producto define ficha; operaciones compara materiales; calidad pretrata, confecciona y ensaya.'),('4–5 · Aprobar o ajustar','Comprador aprueba por escrito; producto corrige y vuelve a presentar la muestra.'),('6–7 · Ordenar y producir','Comercial registra orden y 50% de anticipo; taller confecciona contra muestra y lote.'),('8–10 · Controlar','Calidad inspecciona el 100% del piloto; retiene y corrige piezas no conformes antes de liberar.'),('11–12 · Preparar salida','Operaciones etiqueta y empaca; finanzas confirma el 50% de saldo antes de FCA.'),('13–14 · Entregar y aprender','Operaciones formaliza y entrega al transportista; comercial registra recepción y recompra.')]
for i,(a,b)in enumerate(shorts):card(a,b,M+(i%3)*263,345+(i//3)*92,247)
text('Cotizar 24 / 60 / 120 / 240 sin duplicar material y costura. Candidatos: Camila, Aracne, Mundo Puff, Calishop y Aklla. Camila declara 10% de encogimiento: pretratar y ensayar.',M,511,CW,9.2)
foot('Proveedor: calidad 30%, costo 25%, plazo/capacidad 20%, trazabilidad 15%, pago 10%. Falla crítica bloquea. [E07, E15–E18, E41–E43]')
# 12
Y=title('Exportación y costo de llegada','9 · FCA Lima: lugar y responsabilidades definidos')
rect(M,Y,CW,48,C['purple'],4);text('VENDEDOR: producto + exportación + entrega FCA',M+15,Y+10,370,10.5,'Bold',C['linen']);text('COMPRADOR: transporte principal + importación',430,Y+10,360,10.5,'Bold',C['linen'])
table([('Mercancía','60 × $28 = $1.680'),('Caja / peso','50 × 40 × 50 cm / 17 kg'),('Peso volumétrico','20 kg, divisor 5.000'),('Referencia flete','552,55 + 30% = $718,32'),('Entrada + seguro','$60 + $10 = $70')],M,195,350,rowh=35,left=.48)
card('Origen y etiqueta','HTS 6304.92.0000 candidato; revisar tejido e hilo de coser. Composición, país y responsable en inglés. Preferencia PE sujeta a verificación.',M,393,350)
rows=[('Objetivo de flete','$300,00'),('Llegada por funda','$37,67'),('Margen a PVP $78','51,7%'),('Referencia flete / llegada','$718,32 / $44,64'),('Margen con referencia','42,8%'),('Techo flete: margen 50%','$380 con PE; $274,16 sin PE')]
table(rows,432,195,376,rowh=34,left=.48)
text('Fórmula: $28 + tasa × $28 + (flete + $70)/60. Modelo: tasas 12,5% con PE o 18,8% sin PE. El techo es solo transporte; cargos $70 adicionales.',432,415,376,11)
text('Documentos: orden, factura, packing list, transporte, declaración y soporte de origen. Sin presumir franquicia de minimis.',432,484,376,10)
foot('Confirmar tasas, clasificación, origen y canal al despachar. FCA no es FOB aéreo. [E19–E29, E31–E33, E40, E44]')
# 13
Y=title('Organización y plan de 90 días','10 · Cinco funciones; no cinco sueldos a tiempo completo',theme='sand')
roles=[('Coordinación','Prioridades, acuerdos y aprobaciones.'),('Comercial','Prospección, oferta y seguimiento.'),('Producto / calidad','Ficha, muestras, pruebas e inspección.'),('Operaciones','Taller, materiales y despacho.'),('Finanzas','Caja, costos, pagos y registros.')]
w=(CW-4*12)/5
for i,(a,b)in enumerate(roles):card(a,b,M+i*(w+12),Y,w,130)
plan=[('Semanas 1–2','Ficha, directorio y dos proveedores alternativos.'),('Semanas 3–4','Entrevistas, cotizaciones y prototipo.'),('Semanas 5–6','Muestras, ensayos y oferta.'),('Semanas 7–8','Piloto pagado y logística aceptada.'),('Semanas 9–10','Producción e inspección.'),('Semanas 11–12','Despacho, recepción y aprendizaje.')]
grid(plan,279,cols=3,h=91,gap=12)
text('Trabajo parcial: $400 coordinación + $250 comercial/mes. Acordar aportes, pagos, propiedad del diseño y utilidades. Comparar SACS con SAC; empresa aún no constituida.',M,500,CW,10.5)
foot('Liberar capital por hitos. Sin comprador y condiciones aceptadas, no producir el volumen anual. [E36]')
# 14
Y=title('Costos y contribución','11 · Por unidad; moneda USD salvo detalle de confección')
vals=[(13.5,'Producto','$13,50',C['wine']),(2.0667,'Otros variables','$2,07',C['orange']),(12.4333,'Contribución','$12,43',C['teal'])];x=M
for v,lab,num,col in vals:
 ww=370/3;rect(x,155,ww-3,110,col);text(num,x+4,177,ww-11,19,'Serif',C['linen'] if col!=C['teal'] else C['ink'],align=1);text(lab,x+4,215,ww-11,8.5,'Sans',C['linen'] if col!=C['teal'] else C['ink'],align=1);x+=ww
text('$28 · 44,40%',M,291,370,35,'Serif',accent)
text('Venta B2B y margen de contribución. Variable total $15,57: salida local $0,67, cobro 3% ($0,84), incidencias 2% ($0,56), más producto $13,50.',M,340,365,12)
rows=[('Frente de diseño','S/22,00'),('Reverso: 0,40 m × S/8,50','S/3,40'),('Cierre, hilo y etiqueta','S/4,60'),('Corte, costura y acabado','S/12,00'),('Empaque','S/3,20'),('Control y merma','S/3,40'),('Total producto','S/48,60 = $13,50')]
table(rows,432,Y,376,rowh=36)
text('TC presupuestal S/3,60 por dólar. Costos netos bajo supuesto de IGV recuperable.',432,402,376,10.5)
rect(M,466,CW,65,C['purple'],4);text('Fijos: $950/mes',M+14,478,200,15,'Bold',C['linen']);text('Coordinación 400 · comercial 250 · contador 70 · herramientas 50 · promoción 100 · transporte local 80.',M+220,479,CW-235,10.5,'Sans',C['linen'])
foot('La contribución cubre estructura, depreciación y arranque; no equivale a utilidad neta.')
# 15
Y=title('Capital y flujo de caja','11 · La utilidad no reemplaza al efectivo',theme='wine')
stats([('$1.200','activos'),('$1.750','arranque'),('$4.050','caja operativa')],Y,78)
text('Capital inicial $7.000 · sin deuda',M,218,330,23,'Serif',accent)
text('Arranque: diseño/prototipo 450; ensayos 450; formalización 300; catálogo 250; muestras 300.',M,261,330,11)
card('Anticipo de un lote','$840 recibidos vs. producción con IGV $955,80: brecha de $115,80 si el taller cobra todo antes del saldo del cliente.',M,342,330)
text('Caja mensual: cobro pactado vs. saldo un mes tarde',400,224,408,11.5,'Bold',accent)
a=[3058.6,2067.2,1659.2,1251.2,1426.6,1602,1777.4,2536.2,3295,4053.8,4812.6,6154.8];q=[0,0,60,60,120,120,120,180,180,180,180,240];b=[v-q[i]*14 for i,v in enumerate(a)]
for dat,col in [(a,C['gold']),(b,C['teal'])]:
 pts=[(407+i*35,425-(v+500)/7500*150)for i,v in enumerate(dat)]
 for A,B in zip(pts,pts[1:]):line(*A,*B,col,2)
line(407,415,798,415,fg,.5)
for i in range(12):text(f'{i+1}',400+i*35,435,25,8,align=1)
text('Base: mínimo $1.251,20 en M4; cierre $6.154,80.<br/>Saldo tarde: -$253,40 en M5; cierre $2.794,80 + $3.360 por cobrar.',400,465,408,11,'Bold',accent)
foot('IGV: $3.996 no recuperado en caja del año. IR anticipado $403,20; regularización $32,20. [E37–E39]')
# 16
Y=title('Resultado y punto de equilibrio','11 · Año 1: 1.440 fundas')
rows=[('Ventas','$40.320,00'),('Producción','-$19.440,00'),('Salida local','-$960,00'),('Cobros e incidencias','-$2.016,00'),('Contribución','$17.904,00'),('Fijos','-$11.400,00'),('Depreciación + arranque','-$2.150,00'),('Antes de impuestos','$4.354,00'),('IR modelado 10%','-$435,40'),('Utilidad neta','$3.918,60')]
table(rows,M,Y,370,rowh=36)
for i,(a,b) in enumerate([('77','unidades/mes: cubren fijo de caja $950.'),('80','unidades/mes: fijo + depreciación recurrente.'),('1.090','unidades/año: incluye arranque. En lotes, 19 × 60 = 1.140.')]):text(a,438,Y+i*110,140,42,'Serif',accent);text(b,578,Y+10+i*110,230,12)
text('Margen neto 9,72%. Dos pedidos mensuales de 60 superan el umbral recurrente.',438,454,370,13,'Bold',accent)
foot('Precio mínimo contable $24,82 a 1.440 unidades; no retorno exigido ni margen minorista garantizado. IR simplificado. [E39]')
# 17
Y=title('Escenarios y sensibilidad','11 · Escenarios completos y recuperación del IGV',theme='sand')
grid([('Adverso: -$7.971,20','720 fundas · precio $25,20 · producto $15,525 · fijo $950/mes. No se aplica 10% de IR a una pérdida.'),('Base: $3.918,60','1.440 fundas · precio $28 · producto $13,50 · fijo $950/mes. Ventas $40.320; antes de IR $4.354.'),('Favorable: $10.355,40','2.160 fundas · precio $28 · producto $13,50 · fijo $1.100/mes. Antes de IR $11.506.')],Y,h=145)
card('VAN a tres años · descuento 20%','Con recuperación anual del IGV: <b>$7.904,34</b>.<br/>Flujos: -7.000 / 6.068,60 / 5.893,60 / 9.943,60.<br/><br/>Sin recuperación ni realización final del IGV: <b>-$513,16</b>.<br/>Flujos: -7.000 / 2.072,60 / 1.897,60 / 5.947,60.',M,293,365)
card('Sensibilidad antes de impuestos','+$1 de costo unitario: -$1.440/año.<br/>Absorber $5 de flete por funda: -$7.200; resultado -$2.846.<br/>TC S/3,24: producto $15; resultado $2.194.',435,293,373)
text('Sin crecimiento; capital operativo $4.050 liberado en año 3; rescate de equipos $0. La recuperación del IGV determina el resultado del VAN.',435,429,373,11)
foot('Flujos condicionados, no rentabilidad garantizada. IR modelado al 10% cuando hay utilidad. [E37–E39]')
# 18
Y=title('Riesgos y condiciones de avance','12 · Qué controlar antes de escalar',theme='purple')
risks=[('Diferenciación','Colección y servicio distintos; el origen por sí solo no basta.'),('Demanda','Señales de compra al precio completo; no solo interés.'),('Flete','Objetivo $300; techo $380 con PE y PVP $78.'),('Origen / entrada','Validar tejido, hilo, clasificación y cargos.'),('Encogimiento / color','Pretratar, ensayar y aprobar; objetivo ≤3%.'),('Proveedor','Repetibilidad, capacidad, costo y alternativa.'),('Liquidez','Reservar caja; cobrar saldo antes de FCA.'),('Pago','Verificar comprador y abono; no crédito abierto inicial.'),('Gravámenes','Actualizar costo ante cambios de tasa u origen.'),('Afirmaciones','Documentar material y origen; no certificados sin soporte.'),('Concentración','Diversificar cuentas y medir recompra.'),('Acuerdos','Definir aportes, diseño, pagos y reparto.')]
grid(risks,Y,cols=4,h=107,gap=12)
text('Avanzar solo con: comprador pagado + producto/proveedor aptos + costo de llegada aceptado.',M,491,CW,13,'Bold',accent)
foot('Revisar oferta tras 30 contactos y 8 entrevistas útiles sin señales de compra a precio viable. Criterio interno propuesto.')
# 19
Y=title('Conclusiones',theme='linen')
text('Primero, dos pedidos reales.',M,Y,475,44,'Serif',accent)
text('Un piloto pagado conecta ficha técnica, precio, transporte, caja y posibilidad de recompra.',M,227,440,16)
for i,(a,b) in enumerate([('Avanzar','Comprador paga, muestra cumple y llegada permite revender con margen.'),('Rediseñar','Existe interés, pero hay que ajustar producto, lote, flete o precio.'),('Descartar','No hay compra al precio viable o el riesgo no puede controlarse.')]):card(a,b,M,318+i*67,470)
photo(2,550,111,258,388)
foot('Encogimiento cambia costo; volumen cambia flete; anticipo cambia caja. No producir el año por adelantado ni endeudarse sin pedidos.')
# 20 + reference continuation. All source titles retained; hyperlinks do not hide the citation text.
sources=json.loads((ROOT.parent/'sources.json').read_text()) if (ROOT.parent/'sources.json').exists() else json.loads((ROOT/'src/sources.js').read_text().removeprefix('export default ').removesuffix(';'))
for offset in [0,18,36]:
 Y=title('Referencias' if not offset else 'Referencias · continuación','Fuentes externas del análisis; enlaces activos',index=20)
 chunk=sources[offset:offset+18];per_col=math.ceil(len(chunk)/2);row_h=min(78,414/per_col)
 for j,s in enumerate(chunk):
  col=j//per_col;row=j%per_col;x=M+col*397;yy=Y+row*row_h
  t=s['text'];t=re.sub(r'^\[E\d+\]\s*','',t)
  # Keep institution, date and the first bibliographic sentence; descriptive extraction notes are not separate sources.
  match=re.search(r'(?<=\))\.\s*',t)
  end=t.find('. ',match.end() if match else 0)
  short=t if end<0 else t[:end+1]
  if len(short)>170:short=short[:167].rsplit(' ',1)[0]+'…'
  h=text(f'<b>E{offset+j+1:02d}</b> · '+short,x,yy,380,10,leading=13.5)
  c.linkURL(s['url'],(x,H-yy-h,x+380,H-yy),relative=0,thickness=0)
 foot('Fotografías: AMAHÍ, referencias facilitadas por el usuario. Diagramas y gráficos propios. DM Sans + Cormorant Garamond (SIL OFL).')
c.save();(TMP/'pdf-layout-check.json').write_text(json.dumps({'pages':page,'blocks':len(bounds),'bounds':bounds},ensure_ascii=False));print(OUT,page,'páginas')
