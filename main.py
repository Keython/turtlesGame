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


#laikapstākļu ģenerators
import random
apstakli=["slikti", "labi"]
laikapstakli = random.choice(apstakli)

punkti=0

#aprēķina akumulatora izlādi atkarībā no laikapstākļiem
akumulators_sakuma = 100
cels = 140       #uztaisīt, lai reālus km var mainīt 
if laikapstakli == "labi" and cels<=140:
    akumulators_izteretais= cels*100/140 
    print(akumulators_izteretais)
if laikapstakli=="labi" and cels>140:
    akumulators_izteretais=akumulators_sakuma
    print("Akumulators izlādējies")
if laikapstakli == "slikti" and cels<=80:
    akumulators_izteretais= cels*100/80 
    print(akumulators_izteretais)
if laikapstakli=="slikti" and cels>80:
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

#kontrolpunktu faila nolasīšana
with open('faili/kontrolpunkti.txt') as f:
    contents = f.read()
    print(contents)

#kontrolpunktu tabula

#kontrolpunkts muzejs
print("Kādā krāsā ir Liepājas muzejs?\na:zils \nb:rozā\nc:zaļš")
muzejs = input()
if muzejs == "c":
  print("Pareizi!")
else:
  print("Mēģini vēlreiz!")
  print("Kādā krāsā ir Liepājas muzejs?\na:zils \nb:rozā\nc:zaļš")
  muzejs= input()
  if muzejs == "c":
    print("Pareizi!")
  else:
    print("Nepareizi!")

#kontrolpunkts katedrāle
#7.uzd
print("Kāda ticība ir Karostas katedrālē?\na:luterānisms \nb:pareizticība \nc:kristietība")
ticība = input()
if ticība == "b":
    print("Pareizi!")
else:
    print("Mēģini vēlreiz!")
    print("Kāda ticība ir Karostas katedrālē?\na:luterānisms \nb:pareizticība \nc:kristietība")
    ticība = input()
    if ticība == "b":
        print("Pareizi!")
else:
    print("Nepareizi!")

               
               
#indentifikatora atbilstības pārbaude


#akumolatora uzskaite, a0=100%, vienmēr var uzspiest


#laikapstākļu faktors mašīnas nobraukumam


#uzlādes līmeņa, km nolasīšana jebkurā laikā


#10 kotrolpunkti, uzlādes stacija, uzdevumi


#bonusa punkti auto uzlādei par atrisinātu uzdevumu


#evakuators


#spēles beigas, rezultātu izvade


#pavadītais laiks spēlē
import timeit

start = timeit.default_timer()

# All the program statements
stop = timeit.default_timer()
execution_time = stop - start
time = round(execution_time, 2)

print("Program Executed in "+str(time)) # It returns time in seconds

#bildes, uzlabot, lai randoma atveras un pazūd 
from PIL import Image
im = Image.open(r"prezidenti/vaira.jpg")
im.show()
print("Kā sauc šo prezidentu(-i)?") 
atbilde =input()

