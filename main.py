print("TURTLES' RALLY LIEPĀJA")
#vārdi, sākums

print("Spēles izstrādātāji: Paula Lībeka, Loreta Aleksejeva, Keita Laimiņa")
print("SPIED 'ENTER', LAI SĀKTU SPĒLI")

#taustiņu pārbaude
input() 
print("starts")
#import keyboard
#while True:
    #if keyboard.is_pressed("space"):
        #print("STARTS")
        #break
# Reading an excel file using Python
import xlrd
 
# Give the location of the file
loc = ("faili/kontrolpunktu tabula (bez km).xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))
 
# For row 0 and column 0
ab =sheet.cell_value(2, 1)
ac = sheet.cell_value(3, 1)
ad = sheet.cell_value(4, 1)
ae = sheet.cell_value(5, 1)
af = sheet.cell_value(6, 1)
ag = sheet.cell_value(7, 1)
ah = sheet.cell_value(8, 1)
ai = sheet.cell_value(9, 1)
aj = sheet.cell_value(10, 1)
a1 = sheet.cell_value(11, 1)
a2 = sheet.cell_value(12, 1)
a3 = sheet.cell_value(13, 1)
print(ab,ac,ad,ae,af,ag,ah,ai,aj,a1,a2,a3)

ba =sheet.cell_value(1, 2)
bc =sheet.cell_value(3, 2)
bd = sheet.cell_value(4, 2)
be = sheet.cell_value(5, 2)
bf = sheet.cell_value(6, 2)
bg = sheet.cell_value(7, 2)
bh = sheet.cell_value(8, 2)
bi = sheet.cell_value(9, 2)
bj = sheet.cell_value(10, 2)
b1 = sheet.cell_value(11, 2)
b2 = sheet.cell_value(12, 2)
b3 = sheet.cell_value(13, 2)

ca =sheet.cell_value(1, 3)
cb =sheet.cell_value(2, 3)
cd = sheet.cell_value(4, 3)
ce = sheet.cell_value(5, 3)
cf = sheet.cell_value(6, 3)
cg = sheet.cell_value(7, 3)
ch = sheet.cell_value(8, 3)
ci = sheet.cell_value(9, 3)
cj = sheet.cell_value(10, 3)
c1 = sheet.cell_value(11, 3)
c2 = sheet.cell_value(12, 3)
c3 = sheet.cell_value(13, 3)

da =sheet.cell_value(1, 4)
db =sheet.cell_value(2, 4)
dc = sheet.cell_value(3, 4)
de = sheet.cell_value(5, 4)
df = sheet.cell_value(6, 4)
dg = sheet.cell_value(7, 4)
dh = sheet.cell_value(8, 4)
di = sheet.cell_value(9, 4)
dj = sheet.cell_value(10, 4)
d1 = sheet.cell_value(11, 4)
d2 = sheet.cell_value(12, 4)
d3 = sheet.cell_value(13, 4)

ea =sheet.cell_value(1, 5)
eb =sheet.cell_value(2, 5)
ec = sheet.cell_value(3, 5)
ed = sheet.cell_value(4, 5)
ef = sheet.cell_value(6, 5)
eg = sheet.cell_value(7, 5)
eh = sheet.cell_value(8, 5)
ei = sheet.cell_value(9, 5)
ej = sheet.cell_value(10, 5)
e1 = sheet.cell_value(11, 5)
e2 = sheet.cell_value(12, 5)
e3 = sheet.cell_value(13, 5)

fa =sheet.cell_value(1, 6)
fb =sheet.cell_value(2, 6)
fc = sheet.cell_value(3, 6)
fd = sheet.cell_value(4, 6)
fe = sheet.cell_value(5, 6)
fg = sheet.cell_value(7, 6)
fh = sheet.cell_value(8, 6)
fi = sheet.cell_value(9, 6)
fj = sheet.cell_value(10, 6)
f1 = sheet.cell_value(11, 6)
f2 = sheet.cell_value(12, 6)
f3 = sheet.cell_value(13, 6)

ga =sheet.cell_value(1, 7)
gb =sheet.cell_value(2, 7)
gc = sheet.cell_value(3, 7)
gd = sheet.cell_value(4, 7)
ge = sheet.cell_value(5, 7)
gf = sheet.cell_value(6, 7)
gh = sheet.cell_value(8, 7)
gi = sheet.cell_value(9, 7)
gj = sheet.cell_value(10, 7)
g1 = sheet.cell_value(11, 7)
g2 = sheet.cell_value(12, 7)
g3 = sheet.cell_value(13, 7)

ha =sheet.cell_value(1, 8)
hb =sheet.cell_value(2, 8)
hc = sheet.cell_value(3, 8)
hd = sheet.cell_value(4, 8)
he = sheet.cell_value(5, 8)
hf = sheet.cell_value(6, 8)
hg = sheet.cell_value(7, 8)
hi = sheet.cell_value(9, 8)
hj = sheet.cell_value(10, 8)
h1 = sheet.cell_value(11, 8)
h2 = sheet.cell_value(12, 8)
h3 = sheet.cell_value(13, 8)

ia =sheet.cell_value(1, 9)
ib =sheet.cell_value(2, 9)
ic = sheet.cell_value(3, 9)
id = sheet.cell_value(4, 9)
ie = sheet.cell_value(5, 9)
ig = sheet.cell_value(7, 9)
ih = sheet.cell_value(8, 9)
ij = sheet.cell_value(10, 9)
i1 = sheet.cell_value(11, 9)
i2 = sheet.cell_value(12, 9)
i3 = sheet.cell_value(13, 9)

ja =sheet.cell_value(1, 10)
jb =sheet.cell_value(2, 10)
jc = sheet.cell_value(3, 10)
jd = sheet.cell_value(4, 10)
je = sheet.cell_value(5, 10)
jf = sheet.cell_value(6, 10)
jg = sheet.cell_value(7, 10)
jh = sheet.cell_value(8, 10)
ji = sheet.cell_value(9, 10)
j1 = sheet.cell_value(11, 10)
j2 = sheet.cell_value(12, 10)
j3 = sheet.cell_value(13, 10)

1a =sheet.cell_value(1, 11)
1b =sheet.cell_value(2, 11)
1c = sheet.cell_value(3, 11)
1d = sheet.cell_value(4, 11)
1e = sheet.cell_value(5, 11)
1f = sheet.cell_value(6, 11)
1g = sheet.cell_value(7, 11)
1h = sheet.cell_value(8, 11)
1i = sheet.cell_value(9, 11)
1j = sheet.cell_value(10, 11)

2a =sheet.cell_value(1, 12)
2b =sheet.cell_value(2, 12)
2c = sheet.cell_value(3, 12)
2d = sheet.cell_value(4, 12)
2e = sheet.cell_value(5, 12)
2f = sheet.cell_value(6, 12)
2g = sheet.cell_value(7, 12)
2h = sheet.cell_value(8, 12)
2i = sheet.cell_value(9, 12)
2j = sheet.cell_value(10, 12)

3a =sheet.cell_value(1, 13)
3b =sheet.cell_value(2, 13)
3c = sheet.cell_value(3, 13)
3d = sheet.cell_value(4, 13)
3e = sheet.cell_value(5, 13)
3f = sheet.cell_value(6, 13)
3g = sheet.cell_value(7, 13)
3h = sheet.cell_value(8, 13)
3i = sheet.cell_value(9, 13)
3j = sheet.cell_value(10, 13)
#kontrolpunktu faila nolasīšana
with open('faili/kontrolpunkti.txt') as f:
    contents = f.read()
    print(contents)
#import docx
#doc = docx.Document('..\\Sample_File_DOCX.docx')
#paras = [p.text for p in doc.paragraphs if p.text]   
#word faila nolasīšana
#import docx
#doc = docx.Document('demo.docx')
#len(doc.paragraphs)
#doc.paragraphs[0].text
#'Kontrolpunkts_dzintars'
#doc.paragraphs[1].text
#'A plain paragraph with some bold and some italic'
#len(doc.paragraphs[1].runs)
#doc.paragraphs[1].runs[0].text
#'A plain paragraph with some '
#doc.paragraphs[1].runs[1].text
#'bold'
#doc.paragraphs[1].runs[2].text
#' and some '
#doc.paragraphs[1].runs[3].text
#'italic'
#import textract
#text = textract.process("faili/Kontrolpunkts_muzejs.docx")
#print(text)
#text = textract.process('faili/Kontrolpunkts_muzejs.docx', extension='docx')

#laikapstākļu ģenerators
import random
apstakli=[2, 1]
laikapstakli = random.choice(apstakli)
if laikapstakli ==1:
  print("Laikapstākļi ir labi")
if laikapstakli == 2:
  print("Laikapstākļi ir slikti")

punkti=10 
#open excel
import pandas as pd
df = pd.read_excel (r'faili/kontrolpunktu tabula (bez km).xlsx')
data=pd.read_excel (r'faili/kontrolpunktu tabula (bez km).xlsx')
dklk = pd.DataFrame(data, columns= ['a','b'])
print (df)
identifikators = input("Ievadi kontorpukta identifikatoru: ")
if identifikators == "ab":
  cels = ab



#aprēķina akumulatora izlādi atkarībā no laikapstākļiem
akumulators_sakuma = 100
      #uztaisīt, lai reālus km var mainīt 
if laikapstakli == 1 and int(cels)<=140:
    akumulators_izteretais= cels*100/140 
    print(akumulators_izteretais)
if laikapstakli==1 and int(cels)>140:
    akumulators_izteretais=akumulators_sakuma
    print("Akumulators izlādējies")
if laikapstakli == 2 and int(cels)<=80:
    akumulators_izteretais= cels*100/80 
    print(akumulators_izteretais)
if laikapstakli==2 and int(cels)>80:
    akumulators_izteretais=akumulators_sakuma
    print("Akumulators izlādējies")

akumulators = akumulators_sakuma-akumulators_izteretais
kilometri = 140*akumulators/100
print("uzlādes līmenis ir "+str(akumulators)+"%\nvēl var nobraukt "+str(kilometri)+" km")


#jāuzlabo, lai vienmēr var paskatīties stāvokli
print("Ja vēlies pārbaudīt akumulatora stāvokli, spied taustiņu 'a'")
if input()=="a":
    print("Uzlādes līmenis ir: "+str(akumulators)+"%")
#while True:
    #if keyboard.is_pressed("a"):
        #print("Uzlādes līmenis ir: "+str(akumulators)+"%")
        #break

#kontrolpunktu tabula

#kontrolpunkts muzejs
print("Kādā krāsā ir Liepājas muzejs?\na:zils \nb:rozā\nc:zaļš")
muzejs = input()
if muzejs == "c":
  print("Pareizi!")
  punkti = punkti +10
else:
  print("Mēģini vēlreiz!")
  print("Kādā krāsā ir Liepājas muzejs?\na:zils \nb:rozā\nc:zaļš")
  muzejs= input()
  if muzejs == "c":
    print("Pareizi!")
    punkti = punkti +5
  else:
    print("Nepareizi!")

#kontrolpunkts dzintars
print("Kurš ir koncertzāles'Lielais Dzintars' arhitekts?\na:Folkers Gīnke \nb:Gunars Birkerts\nc:Pauls Makss Berči")
dzintars = input()
if dzintars == "a":
  print("Pareizi!")
  punkti = punkti+10
else:
  print("Mēģini vēlreiz!")
  print("Kurš ir koncertzāles'Lielais Dzintars' arhitekts?\na:Folkers Gīnke \nb:Gunars Birkerts\nc:Pauls Makss Berči")
  dzintars= input()
  if dzintars == "a":
    print("Pareizi!")
    punkti=punkti+5
  else:
    print("Nepareizi!")
               
#kontrolpunkts tirgus
print("Kā vārdos ir nosaukti Liepājas tirgi?\na:Katrīnas un Jāņa \nb:Annas un Pētera\nc:Marijas un Jāņa")
tirgus = input()
if tirgus == "b":
  print("Pareizi!")
  punkti=punkti+10
else:
  print("Mēģini vēlreiz!")
  print("Kā vārdos ir nosaukti Liepājas tirgi?\na:Katrīnas un Jāņa \nb:Annas un Pētera\nc:Marijas un Jāņa")
  tirgus= input()
  if tirgus == "b":
    print("Pareizi!")
    punkti=punkti+5
  else:
    print("Nepareizi!")         

#kontrolpunkts karosta
print("Kādas ticības baznīca atrodas Karostā?\na:katoļu \nb:luterāņu\nc:pareizticīgo")
karosta = input()
if karosta == "c":
  print("Pareizi!")
  punkti=punkti+10
else:
  print("Mēģini vēlreiz!")
  print("Kādas ticības baznīca atrodas Karostā?\na:katoļu \nb:luterāņu\nc:pareizticīgo")
  karosta= input()
  if karosta == "c":
    print("Pareizi!")
    punkti=punkti+5
  else:
    print("Nepareizi!")

#kontrolpunkts grobiņa
print("Kura ir Grobiņas lielākā iela?\na:Brīvības iela \nb:Lielā iela\nc:Saules iela")
grobiņa = input()
if grobiņa == "b":
  print("Pareizi!")
  punkti=punkti+10
else:
  print("Mēģini vēlreiz!")
  print("Kura ir Grobiņas lielākā iela?\na:Brīvības iela \nb:Lielā iela\nc:Saules iela")
  grobiņa= input()
  if grobiņa == "b":
    print("Pareizi!")
    punkti=punkti+5
  else:
    print("Nepareizi!")  

#kontrolpunkts zirgu sala
print("Kādus dzīvniekus var novērot zirgu salā?\na:putnus \nb:zirgus\nc:roņus")
zirgusala = input()
if zirgusala == "a":
  print("Pareizi!")
  punkti=punkti+10
else:
  print("Mēģini vēlreiz!")
  print("Kādus dzīvniekus var novērot zirgu salā?\na:putnus \nb:zirgus\nc:roņus")
  zirgusala= input()
  if zirgusala == "a":
    print("Pareizi!")
    punkti=punkti+5
  else:
    print("Nepareizi!")

#kontrolpunkts slimnīca
print("Kādā secībā jāveic pirmā palīdzība?(atbilžu burtus atdali ar komatu)\na:sauc palīgā \nb:pārliecinies par savu un apkārtējo drošību.\nc:pārbaudi cietušā stāvokli")
slimnīca = input()
if slimnīca == "b,c,a":
  print("Pareizi!")
  punkti=punkti+10
else:
  print("Mēģini vēlreiz!")
  print("Kādā secībā jāveic pirmā palīdzība?(atbilžu burtus atdali ar komatu)\na:sauc palīgā \nb:pārliecinies par savu un apkārtējo drošību.\nc:pārbaudi cietušā stāvokli")
  slimnīca= input()
  if slimnīca == "b,c,a":
    print("Pareizi!")
    punkti=punkti+5
  else:
    print("Nepareizi!")
#indentifikatora atbilstības pārbaude
print("Tev ir bonusa punkti:",str(punkti))


#akumolatora uzskaite, a0=100%, vienmēr var uzspiest


#laikapstākļu faktors mašīnas nobraukumam


#uzlādes līmeņa, km nolasīšana jebkurā laikā


#10 kotrolpunkti, uzlādes stacija, uzdevumi


#bonusa punkti auto uzlādei par atrisinātu uzdevumu


#evakuators
if akumulators == 0:
  print("Akumulators ir izlādējies! Nepieciešams evakuators! Ievadi uzlādes stacijas identifikatoru!")
  uzlades_stacija = input()
  punkti = punkti-20
#spēles beigas, rezultātu izvade


#pavadītais laiks spēlē

#bildes, uzlabot, lai randoma atveras un pazūd
# kontrolpunkts Čakstes laukums 
print("Kā sauc šo prezidentu(-i)?") 
from PIL import Image
im = Image.open(r"prezidenti/vaira.jpg")
im.show()
atbilde =input()
pareizi=["Vaira Vīķe Freiberga","Vaira Vīķe-Freiberga","Vaira Vīķe - Freiberga","vaira vīķe freiberga","vaira vīķe-freiberga", "vaira vīķe - freiberga"]
if atbilde in pareizi:
    punkti=punkti+10
    print("Pareizi!")
else:
    print("Mēģini vēlreiz!")
    from PIL import Image 
    im = Image.open(r"prezidenti/Zemgals.jpg")
    im.show()
    print("Kā sauc šo prezidentu(-i)?") 
    atbilde=input()
    if atbilde== "Gustavs Zemgals" or atbilde=="gustavs zemgals":
        punkti=punkti+5
        print("Pareizi!")
    else:
        print("Mēģini vēlreiz!")
        from PIL import Image
        im = Image.open(r"prezidenti/kviesis.png")
        im.show()
        print("Kā sauc šo prezidentu(-i)?") 
        atbilde=input()
        if atbilde=="Alberts Kviesis"or atbilde=="alberts kviesis":
            print("Pareizi!")#VAJAG BONUSA PUNKTUS VĒL?
        else:
            print("Nepareizi!")

#kontrolpunkts Kursa
print("Kā sauc šo zivi?\na:plekste\nb:menca\nc:līdaka")
from PIL import Image
im = Image.open(r"zivis/plekste.jpg")
im.show()
zivs=input()
if zivs=="a":
    punkti=punkti+10
    print("Pareizi!")
else:
    print("Mēģini vēlreiz!")
    print("Kā sauc šo zivi?\na:asaris\nb:lasis\nc:rauda")
    from PIL import Image
    im = Image.open(r"zivis/lasis.jpg")
    im.show() 
    zivs=input()
    if zivs=="b":
        punkti=punkti+5
        print("Pareizi!")
    else:
        print("Nepareizi!")

#kontrolpunkts Juliannas pagalms PABEIGT?padomāt kā var vairākas reizes bez tik daudz koda(loop)
for i in range(4):
  gads=random.randrange(1990,2031)
  menesis=random.randrange(1,13)
  if menesis in range(1,10):
      menesis2="0"+str(menesis)
  if menesis in range(10,13):
      menesis2=menesis
  if menesis==2:
      diena=random.randrange(1,29)
  elif menesis==4 or menesis==6 or menesis==9 or menesis==11:
      diena=random.randrange(1,31)
  else:
      diena=random.randrange(1,32)
  if diena in range(1,10):
      diena1="0"+str(diena)
  if diena in range(10,32):
      diena1=diena
  
  gads2=random.randrange(1990, gads+1)
  menesis3=random.randrange(1,menesis+1)
  if menesis3 in range(1,10):
      menesis4="0"+str(menesis3)
  if menesis3 in range(10,13):
      menesis4=menesis3
  else:
      menesis=menesis3 
  if menesis3==2:
      diena2=random.randrange(1,diena+1)
  elif menesis3==4 or menesis3==6 or menesis3==9 or menesis3==11:
      diena2=random.randrange(1,diena+1)
  else:
      diena2=random.randrange(1,diena+1)
  if diena2 in range(1,10):
      diena="0"+str(diena2)
  else:
      diena=diena2
  print("Tu esi bāra apsargs. Šodien ir šāds datums: "+str(diena1)+"."+str(menesis2)+"."+str(gads))
  print("Vai tu drīksti bārā ielaist cilvēku, kura dzimšanas datums: "+str(diena)+"."+str(menesis4)+"."+str(gads2))
  print("a:drīkst ielaist\nb:nedrīkst ielaist")
  apsargs = input()
  if gads - gads2>18:
    if apsargs=="a":
      punkti=punkti+10
      print("Pareizi!")
    else:
      print("Nepareizi!")
  if gads - gads2<18:
    if apsargs=="b":
      punkti=punkti+10
      print("Pareizi!")
    else:
      print("Nepareizi!")
  if gads - gads2==18 and diena1 - diena>0 and menesis2 - menesis>=0 :
    if apsargs=="a":
      punkti=punkti+10
      print("Pareizi!")
    else:
      print("Nepareizi!")
print(punkti)
    


