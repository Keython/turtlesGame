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

#aprēķina akumulatora izlādi atkarībā no laikapstākļiem
akumulators_sakuma = 100
cels = 140       #uztaisīt, lai reālus km var mainīt 
if laikapstakli == "labi":
    akumulators_izteretais= cels*100/140 
    print(akumulators_izteretais)
if laikapstakli == "slikti" and cels<=80:
    akumulators_izteretais= cels*100/80 
    print(akumulators_izteretais)
elif laikapstakli=="slikti" and cels>80:
    akumulators_izteretais=akumulators_sakuma
    print("Akumulators izlādējies")

akumulators = akumulators_sakuma-akumulators_izteretais
print("uzlādes līmenis ir "+str(akumulators)+"%")


#jāuzlabo, lai vienmēr var paskatīties stāvokli
print("Ja vēlies pārbaudīt akumulatora stāvokli, spied taustiņu 'a'")
while True:
    if keyboard.is_pressed("a"):
        print("Uzlādes līmenis ir: "+str(akumulators)+"%")
        break

#kontrolpunktu faila nolasīšana
with open('kontrolpunkti.txt') as f:
    contents = f.read()
    print(contents)

#kontrolpunktu tabula


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