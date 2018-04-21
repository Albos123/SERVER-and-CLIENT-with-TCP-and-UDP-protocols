import socket
from _thread import *
import threading
import datetime
import random

def PORTNR(adresa):
    return "Klienti eshte duke perdorur portin: " + str(adresa[1])
def IPADDR(adresa):
    return "IP Adresa e klientit eshte: " + str(adresa[0])

def ZANORE(fjalia):
    if(len(fjalia)>1):
        zanoret = "aeëiouyAEËIOUY"
        numrator = 0
        for i in range (1 , len(fjalia)):   #arsyeja pse ketu unaza fillon nga 1 (e jo nga 0) eshte sepse fjala e pare e metodes ZANORE eshte vete fjala ZANORE
            fjala = str(fjalia[i].split())
            for j in range (0 , len(fjala)):            #ne keto dy unaza poshte behet krahasimi i qdo shkronje te qdo fjale te tekstit me shkronjat qe jane zanore
                for k in range (0 , len(zanoret)):
                    if(fjala[j]==zanoret[k]):
                        numrator=numrator+1
        fjalia = "Teksti i pranuar permban " +str(numrator)+ " zanore."
    else:
        fjalia = "GABIM"        #ketu ka mund te perdoret edhe nje variabel e tipit boolean
    return fjalia
def PRINTO(fjalia):
    fjalia = fjalia.replace("\\t", "    ")  #kur fjalia pranohet nga klienti tek serveri , qdo hapesire me tastin TAB qe e kemi shkruajtur shendrrohet ne \t dhe kesisoji teksti nuk ka kuptim, andaj e kam zevendesuar qdo hapesire TAB me 4 hapesira SPACE
#logjika ne 4 komandat me poshte eshte qe se pari te hiqen te gjitha hapesirat nga e majta ne te djathte
#pastaj te hiqen 6 karaktere e qe eshte fjala PRINTO
#pastaj te hiqen edhe hapesirat tjera nga e majta ne te djathte e teksit te targetuar per printim
#dhe ne fund te hiqen te gjitha hapesirat nga e djathta ne te majte deri ne karakterin e pare qe hasim
    fjalia = fjalia.lstrip(" ")
    fjalia = fjalia[6:]
    fjalia = fjalia.lstrip(" ")
    fjalia = fjalia.rstrip(" ")
#ne qofte se teksti i targetuar per printim ka qene i perbere vetem nga hapesirat atehere ai do mbetet ne fund i zbrazet, andaj kemi validimin:
    if(len(fjalia)==0):
        fjalia = "GABIM"
    return fjalia
def HOST():
    try:
        HOSTNAME = gethostname()
        return "Emri I klientit eshte: " + str(HOSTNAME)
    except:
        return "Na vie keq, nuk kemi mundur ta gjejme emrin e HOST-it." 
def TIME():
    koha = datetime.datetime.now()
    koha = str(koha)
#ketu jane hequr nga e djathta ne te majte 6 shifra per mikrosekondat dhe karakteri i pikes qe eshte e 7-ta 
    koha = koha[:-7]
    return ("Viti-muaji-dita ora:minutat:sekondat   \n"+koha)
def LOJA():
    numrat=random.sample(range(1,100), 20) #gjenerohen numra 20 te rastesishem nga 1 deri ne 99
    numrat=sorted(numrat)
    numrat=str(numrat)
    return "20 numra te rastesishem nga vargu [1-99] jane: " + numrat
def FIBONACCI(numri):
    numri = str(numri)
    if(numri[0]!="-" and numri.isnumeric()): #nje validim nqs eshte numer i plote dhe jo negativ (ne rast se validimi nga ana e klientit deshton)
        numri=int(numri)
        numri1=0
        numri2=1
        for i in range (1 , numri):
            numri3=numri1+numri2
            numri1=numri2
            numri2=numri3
    else:
        numri3 = "GABIM"
    return str(numri3)
def KONVERTO(OPSIONI, vlera):
    if(vlera.lstrip("-").replace(".","").isnumeric()):  
        vlera = float(vlera)        #arsyeja pse vlera eshte shendrruar ne float eshte ngase konvertimi neper temperatura e masa nuk behet vetem me numra te plote
        OPSIONI = str(OPSIONI)
        if (OPSIONI=="CelsiusToKelvin"):
            vlera = vlera+273.15
        elif(OPSIONI=="CelsiusToFahrenheit"):
            vlera = vlera*9/5 +32
        elif(OPSIONI=="KelvinToFahrenheit"):
            vlera = (vlera-273.15)*9/5 +32
        elif(OPSIONI=="KelvinToCelsius"):
            vlera = vlera*9/5 +32
        elif(OPSIONI=="FahrenheitToCelsius"):
            vlera = (vlera-32)*5/9
        elif(OPSIONI=="FahrenheitToKelvin"):
            vlera = (vlera+459.67)*5/9
        elif(OPSIONI=="PoundToKilogram"):
            vlera = str(vlera)          #eshte shendrruar ne string ne menyre qe ta pyesim se a e permban shenjen e minusit ne fillim te numrit a po jo
            if(vlera[0]!="-"):
                vlera = float(vlera)     #kthehet prap ne float per llogarite 
                vlera = vlera/2.2046226218
            else:
                vlera = "GABIM"
        #procedura e njejt sikurse per PoundToKilogram
        elif(OPSIONI=="KilogramToPound"):
            vlera = str(vlera)
            if(vlera[0]!="-"):
                vlera = float(vlera)
                vlera = vlera*2.2046226218
            else:
                vlera = "GABIM"
        else:
            vlera="GABIM"
    else:
        vlera="GABIM"
    return str(vlera)
numriRand=random.sample(range(100), 1)      #gjenerimi i nje numri random nga 0 deri 99 per metoden shtese GUESS
def GUESS(numri):
    if(int(numri)<int(numriRand[0])):
        fjalia = "Numrin qe keni zgjedhur eshte me i vogel se numri i sakte."
    elif(int(numri)>int(numriRand[0])):
        fjalia = "Numrin qe keni zgjedhur eshte me i madh se numri i sakte."
    else:
        fjalia = "Numrin qe keni zgjedhur eshte i sakte."
    return fjalia
def NXITIMI(shpejtesia1, shpejtesia2, koha):
    nxitimi = (float(shpejtesia2)-float(shpejtesia1))/float(koha)
    nxitimi = str(nxitimi)
    return nxitimi
#arsyeja pse ne fund te qdo metode e kam konvertuar variablen kryesore ne string eshte sepse ajo me pas duhet te enkodohet ne bytes, dhe metoda e gatshme encode mund te enkodoje vetem stringje
def threaded(s,serverPort):     #funksioni i threadit, parameter eshte soketa s ngase permes saj e pranojme kerkesen dhe e dergojme pergjigjen, dhe gjithashtu parameter eshte edhe numri i portit ne menyre qe te dihet se ku te operoje threadi 
    while True:
        try:
            d = s.recvfrom(128)
            data = d[0]         #ketu ruhen kerkesat
            addr = d[1]         #ketu ruhet IP adresa dhe numri i portit (pra variabla d eshte liste e cila ne vete permban nje liste tjeter)
            var0 = str(data)
        except:
            break
        var0 = str(var0)
        var0 = var0[2:]     #hiqet b' ne fillim te tekstit
        var0 = var0[:-1]    #hiqet ' ne fund te tekstit
 #arsyeja pse tutje me poshte eshte vazhduar me variablen var e jo var0 eshte ngase var0 nevojitet tek metoda PRINTO ku var0 nuk duhet te perpunohet me tej, pra teksti duhet te mbetet origjinal
        var = var0             
        var = var.replace("\\t", "")

 #var eshte nje string ku duhet te hiqen te gjitha hapesirat e teperta, andaj me split() var shendrrohet ne liste ku neper anetare mirren vetem karakteret dhe jo hapesirat:
        var = var.split()
        if(len(var)>0 and var[0]!=""):
            if (var[0] == "PORTNR"):
                mesazhi = PORTNR(adresa = addr)
            elif (var[0] == "IPADDR"):
                mesazhi = IPADDR(adresa = addr)
            elif (var[0]=="ZANORE"):
                mesazhi = ZANORE(fjalia = var)
            elif (var[0]=="PRINTO"):
                mesazhi = PRINTO(fjalia = var0)
            elif (var[0]=="HOST"):
                mesazhi = HOST()
            elif (var[0]=="TIME"):
                mesazhi = TIME()
            elif (var[0]=="LOJA"):
                mesazhi = LOJA()
            elif (var[0]=="FIBONACCI"):
                if(len(var)==2):
                    mesazhi = FIBONACCI(numri = var[1])
                else:
                    mesazhi = "GABIM"
            elif (var[0]=="KONVERTO"):
                if(len(var)==3):
                    mesazhi = KONVERTO(OPSIONI = var[1], vlera = var[2])
                else:
                    mesazhi = "GABIM"
            elif (var[0]=="GUESS"):
                mesazhi = GUESS(numri = var[1])
            elif (var[0]=="NXITIMI"):
                mesazhi = NXITIMI(shpejtesia1= var[1] , shpejtesia2=var[2], koha=var[3])
            else:
                mesazhi = "Ju lutem zgjidheni njeren metode."
        else:
            mesazhi = "GABIM"
        mesazhi = str(mesazhi)
 #edhe pse nga ana e klientit e kam kufizuar qe mos te mirret pergjigjeja me e gjate se 128 bytes, me mire eshte qe ajo mos te dergohet fare nga serveri
        if(len(str.encode(mesazhi))>128):
            mesazhi = "Na falni por pergjigjeja e serverit ka qene me e gjate se 128 bytes."
        if(mesazhi!="GABIM"):
            s.sendto(str.encode(mesazhi) , addr)       
#nese rasisht ndodh ndonje gabim dhe serveri nuk mund t'a pranoje kerkesen nga klienti 
#(shiko me larte komanda e pare tek try) apo edhe nqs nuk do mund te ekzekutohen 3 komandat tjera te ardhshme per qfaredo arsye
#perjashtimi e ben qe kjo unaze te terminohet, dhe pasi qe nuk kemi per te kthyer kurfar pergjigje, eshte mire qe soketa te mbyllet
    s.close()
def Main():
    serverPort = 11000
    serverIP= "127.0.0.1"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    #krijimi i soketes ne protokollin UDP
    s.bind((serverIP, serverPort))      #lidhja e serverit per IP adresen e hostit dhe portin e caktuar
    
    while True:         #therret shume threada
        start_new_thread(threaded, (s,serverPort))
    s.close()

if __name__ == '__main__':
    Main()          #thirret funksioni main