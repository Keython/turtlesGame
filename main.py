print("TURTLES' RALLY LIEPĀJA")
#vārdi, sākums

print("Spēles izstrādātāji: Paula Lībeka, Loreta Aleksejeva, Keita Laimiņa")
print("SPIED 'SPACE', LAI SĀKTU SPĒLI")
#taustiņu pārbaude
import keyboard
while True:
    if keyboard.is_pressed("space"):
        print("STARTS")
        break

#laikapstākļu ģenerators
import random
apstakli=["slikti", "labi"]
laikapstakli = random.choice(apstakli)

#kontrolpunktu faila nolasīšana
with open('kontrolpunkti.txt') as f:
    contents = f.read()
    print(contents)

#kontrolpunktu tabula


#indentifikatora atbilstības pārbaude


#akumolatora uzskaite, a0=100%, vienmēr var uzspiest
akumulators_sakuma = 100
cels = 140
if laikapstakli == "labi":
    akumulators_izteretais= cels*100/140 
    print(akumulators_izteretais)
akumulators=50

print("Ja vēlies pārbaudīt akumulatora stāvokli, spied taustiņu 'a'")
while True:
    if keyboard.is_pressed("a"):
        print("Uzlādes līmenis ir: "+str(akumulators)+"%")
        break


#laikapstākļu faktors mašīnas nobraukumam



#uzlādes līmeņa, km nolasīšana jebkurā laikā


#10 kotrolpunkti, uzlādes stacija, uzdevumi


#bonusa punkti auto uzlādei par atrisinātu uzdevumu


#evakuators


#spēles beigas, rezultātu izvade