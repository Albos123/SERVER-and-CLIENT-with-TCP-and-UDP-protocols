import socket               #importimi i modulit socket per mundesimin e thirrjes se komandave te nevojshme per krijimin e soketave

#validimi i IP adreses ku lejohet te shkruajme "localhost" ose numra te plote nga 0.0.0.0 deri ne 255.255.255.255
while 1:
    serverName = input("Ju lutem jepeni emrin ose IP adresen e serverit:")
    if (serverName==""):
        serverName = "localhost"
    if (serverName=="localhost" or serverName=="127.0.0.1"):
        break
    else:
        serverName1 = serverName.split(".")
        k=0
        for i in range (0, len(serverName1)):
            serverName1[i]=str(serverName1[i])
            if (serverName1[i].lstrip("-").isnumeric()):        #pythoni nuk ka funksion te gatshem qe mund t'i detektoje edhe numrat negative nese jane numra, andaj ia heqim shenjen negative me lstrip("-") dhe pastaj pyesim a eshte numer me isnumeric()
                k=k+1
            else:
                break
        if(k==4):       #IP adresa duhet te permbaje vetem nga 4 numra te ndare me pike dhe jo me shume ose me pak
            k=0
            for i in range (0 , len(serverName1)):
                if (int(serverName1[i]) <=255 and int(serverName1[i])>=0):
                    k=k+1
                else:
                    break
            if(k==4):
                break
            else:
                print("Numrat duhet te jene brenda intervalit [0-255].")
        else:
            print("Duhet ta shkruani IP adresen me 4 numra te ndare me pike.")

#validimi i numrit te portir ku lejohet te ipen vetem numra te plote brenda intervalit [1024,65535]
while 1:
    serverPort = input("Ju lutem jepeni numrin e portit te serverit:")
    if (serverPort==""):
        serverPort = 11000
        serverPort = str(serverPort)
    if (serverPort.lstrip("-").isnumeric()):
        serverPort= int(serverPort)
        if (serverPort>=1024 and serverPort<= 65535):
            break
        else:
            print("Ju nuk guxoni te zgjedhni porte jashte intervalit [1024,65535]")
    else:
        print("Ju duhet te shkruani nje numer te plote!")

print("Ju lutem zgjedheni njeren prej metodave:")
metodat = "\n1.IPADDR\n2.PORTNR\n3.ZANORE {hapesire} tekst\n4.PRINTO {hapesire} tekst\n5.HOST\n6.TIME\n7.LOJA\n8.FIBONACCI {hapesire} numer i plote\n9.KONVERTO {hapesire} OPSIONI {hapesire} numer\n10.GUESS {hapesire} nje numer brenda intervalit [0-99]\n11.NXITIMI {hapesire} shpejtesia1(m) {hapesire} shpejtesia2(m) {hapsire} koha(s)12.EXIT"
print (metodat)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #krijimi i soketes ne protokollin TCP
s.connect((serverName, serverPort))
print ("Klienti u lidh me serverin ",serverName," ne portin " , serverPort, " .")
while 1:        #kjo unaze "infinit" eshte qe klienti te mund te dergoje shume kerkesa dhe te pranoje shume pergjigje brenda nje ekzekutimi
    while 1:        #kjo unaze "infinit" eshte fillimi i validimit te kerkesave, sa here qe kerkesat shkruhen gabim, ato nuk dergohen por programi kthehet prap ne fillim te kesaj unaze, nese kerkesa eshte e shkruar sakte atehere eshte perdorur komanda break
        var = input("Ju lutem shkruajeni kerkesen: ")
        if(len(str.encode(var))>128):       #nese kerkesa eshte me e madhe se 128 byte, ajo nuk duhet te dergohet, funksioni len() si parameter mund te pranoje vetem stringje
            print("Ju e keni shkruar kerkesen shume te gjate (me gjate se 128 bytes)")
        else:
            if (var==""):               
                print ("Ju duhet te shkruani diqka!")
            else:
                var0 = var
                var0 = var0.split()         #me kete e kam ndare variablen hyrese dhe e kam shendrruar ne liste ku e trajtoj qdo anetare te listes ne menyre te veqante
                if(len(var0)==1):

                    #nese e kemi shkruar vetem nje fjale atehere ajo duhet t'i takoje gjithsesi njeres prej ketyre metodave me poshte:
                    if (var0[0] == "IPADDR" or var0[0]=="PORTNR" or var0[0]=="HOST" or var0[0]=="TIME" or var0[0]=="LOJA" or var0[0]=="EXIT"):
                        break
                    else:
                        print ("Ju duhet te shkruani njeren prej metodave!")
                #nese kemi shkruar dy fjale, atehere kerkesa duhet t'i takoje gjithsesi njeres prej ketyre metodave me poshte:
                elif (len(var0)==2):
                    if(var0[0] == "FIBONACCI" or var0[0]=="GUESS"):
                        var0 = var0[1]
                        if(var0[0]=="-"):
                            if(var0.lstrip("-").isnumeric()):
                                print ("Nuk guxoni te shkruani numer negativ!")
                            else:
                                print ("Duhet te shkruani nje numer te plote!")
                        else:
                            if(var0.isnumeric()):
                                break
                            else:
                                print ("Duhet te shkruani nje numer te plote!")
                    elif(var0[0] =="ZANORE" or var0[0] == "PRINTO"):
                        break
#metoda konverto realisht i ka 3 parametra por nese e harrojme parametrin e fundit atehere klienti duhet ta dije qe ka gabuar pjeserisht ne shkrimin e sakte te kerkeses
                    elif(var0[0]=="KONVERTO"):
                        if(var0[1]=="CelsiusToKelvin" or var0[1]=="CelsiusToFahrenheit" or var0[1]=="KelvinToFahrenheit" or var0[1]=="KelvinToCelsius" or var0[1]=="FahrenheitToCelsius" or var0[1]=="FahrenheitToKelvin" or var0[1]=="KilogramToPound" or var0[1]=="PoundToKilogram"):
                            print ("Ju duhet ta shkruani edhe nje numer me pastaj.")
                        else:
                            print ("Ju duhet te shkruani njeren prej opsioneve!")
#ne qofte se klienti ka harruar se cilat metodat mund t'i therrase:
                    elif(var0[0]=="SHIKO" and var0[1]=="METODAT"):
                        print (metodat)
                    else:
                        print ("Ju duhet te shkruani njeren prej metodave!")
#nqs klienti i ka shkruar 3 fjale atehere gjithsesi metoda duhet te jete KONVERTO, ngase nuk ka metoda tjera me nga 3 fjale:
                elif(len(var0)==3):
                    if(var0[0]=="KONVERTO"):
                        if (var0[1]=="CelsiusToKelvin" or var0[1]=="CelsiusToFahrenheit" or var0[1]=="KelvinToFahrenheit" or var0[1]=="KelvinToCelsius" or var0[1]=="FahrenheitToCelsius" or var0[1]=="FahrenheitToKelvin"):
                            var0 = var0[2]
#pythoni gjithashtu nuk ka ndonje metode te gatshme qe e njeh nese nje variabel eshte numer decimal andaj me replace(".","") e heqim piken dhe pyesim se a eshte numer
                            if(var0.lstrip("-").replace("." , "").isnumeric()):
                                break
                            else:
                                 print ("Duhet te konvertoni numer!")
                        elif(var0[1]=="PoundToKilogram" or var0[1] =="KilogramToPound"):
                            var0 = var0[2]      #eshte marre vetem parametri i trete, ne kete rast numri (me qellim qe me vone ta pyesim se a eshte negativ apo jo)
#nuk guxojme te konvertojme mase negative, andaj kemi kete pjese te kodit:
                            if(var0[0]=="-"):   #stringjet siq duket jane te numrueshme
                                if(var0.lstrip("-").replace("." , "").isnumeric()):
                                    print ("Nuk guxoni te konvertoni mase negative!")
                                else:
                                    print ("Duhet te konvertoni numer!")
                            else:
#ka mundesi qe ndonje string te filloje me shenjen e minusit por mos te jete fare numer, psh -ABC, andaj behet ky validim
                                if(var0.replace("." , "").isnumeric()):
                                    break
                                else:
                                    print ("Duhet te konvertoni numer!")
                        else:
                            print ("Ju duhet te shkruani njeren prej opsioneve!")
                    elif(var0[0] =="ZANORE" or var0[0] == "PRINTO"):
                        break
                    else:
                        print ("Ju duhet te shkruani njeren prej metodave!")
#nese klienti i ka shkruar 4 fjale atehere metoda e zgjedhur gjithsesi duhet te jete NXITIMI
                elif (len(var0)==4):
                    if (var0[0]=="NXITIMI"):
                        if (var0[1].lstrip("-").replace("." , "").isnumeric() and var0[2].lstrip("-").replace("." , "").isnumeric() and var0[3].lstrip("-").replace("." , "").isnumeric()):
                            if (float(var0[3])==0):
                                print("Koha nuk guxon te jete zero!")
                            elif (float(var0[3])<0):
                                print("Koha nuk guxon te jete negative!")
                            else:
                                break
                        else:
                            print ("Te tre parametrat duhet te jene numra, pra\nshpejtesia1 (m), shpejtesia2 (m) dhe koha (s)")
                    elif(var0[0]=="PRINTO" or var0[0]=="ZANORE"):
                        break
                    else:
                        print ("Ju duhet te shkruani njeren prej metodave!")
                else:
                    if(var0[0]=="PRINTO" or var0[0]=="ZANORE"):
                        break
                    else:
                        print ("Keni shkruar me shume tekst se qe duhet. Ju duhet te shkruani njeren prej\nmetodave!")
#qdo break qe ka qene me larte deri ne kete rresht ka qene per unazen e brendshme
#tash pasi qe mesazhi i ka kaluar ato "pengesa", ai eshte i gatshem te dergohet tek serveri
#perveq nese eshte zgjedhur "metoda" EXIT e cila e perfundon unazen e jashtme duke mos e lejuar qe komandat e dergimit dhe pranimit te mesazhit te ekzekutohen
    
    if (var == "EXIT"):
        break
    s.sendall(str.encode(var , encoding="ASCII"))        #dergimi i mesazhit i enkoduar ne bytes
    data = s.recv(128)      #pranimi i mesazhit nga serveri i cili gjithashtu eshte i enkoduar ne bytes
    data = str(data)        #konvertimi nga bytes ne string

     #pasi qe mesazhi i pranuar nga serveri ka qene ne bytes, ne fillim te pergjigjes i shtohen dy karaktere b' dhe ne fund i shtohet '
    #andaj per ta larguar kete "papasterti" nga pergjigjeja, duhet te fshihen 2 karakteret e para nga e djathta e cila behet permes komandes me poshte:

    data = data[2:]

#dhe duhet te fshihet edhe karakteri i fundit nga e majta e cila behet permes komandes me poshte:
    data = data[:-1]
    data = data.replace("\\n" , "\n")
    print(data)

#nese eshte shkruar EXIT atehere unaza e jashtme pasi qe te terminohet, soketa eshte mire te mbyllet
s.close()