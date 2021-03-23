import socket 
import threading
import _thread
import math 
import random 
import sys


serverName = ''
serverPort = 13000 
serverAddress = (serverName, serverPort)
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serverSocket.bind(serverAddress)
    print('Serveri është startuar në localhost në portin: ' + str(serverPort))
    serverSocket.listen(5)
    print('Serveri është duke pritur për ndonjë kërkesë')
except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()
    #Metoda IPADRESS
def IPADRESS():
    return (str(address[0]))
    #MEtoda PORT
def PORT():
      return(str(address[1]))
    #Metoda COUNT
def COUNT(teksti):
   bashketingellore=0
   zanore=0
   for i in teksti:
      if(i=='b' or i=='c' or i=='d' or i=='f' or i=='g' or i=='h' or i=='j' 
         or i=='k' or i=='l' or i=='m' or i=='n' or i=='p'
         or i=='q' or i=='r' or i=='s' or i=='t' or i=='v' or i=='w' 
         or i=='x' or i=='z' or i=='B' or i=='C' or i=='D' 
         or i=='F' or i=='G' or i=='H' or i=='J' or i=='K' 
         or i=='L' or i=='M' or i=='N' or i=='P' or i=='Q' 
         or i=='R' or i=='S' or i=='T' or i=='U' or i=='V' or i=='W' or i=='X' or i=='Z' ):
            bashketingellore=bashketingellore+1
      elif(i =='a' or i =='e' or i=='ë' or i=='i' or i=='o' or i=='u' or
         i =='y'  or i =='A' or i =='E' or i=='Ë' or i=='I' or i=='O' or i=='U' or
         i =='Y' 
         ):
            zanore = zanore + 1

   return("Në këtë tekst janë " + str(bashketingellore) + " bashkëtingëllore dhe " + str(zanore) +" zanore")
    #Metoda REVERSE
def REVERSE(teksti):
    fjaliaReverse=""
    for i in teksti:
        fjaliaReverse=i+fjaliaReverse
    return fjaliaReverse
    #Metoda PALINDROME
def PALINDROME(teksti):  

    if(teksti==REVERSE(teksti)):
        return("Teksti është palindrom")
    else:
        return("Teksti i dhëne nuk është palindrom")
    #Metoda TIME
def TIME():
    from time import strftime
    Koha = strftime("%d.%m.%Y %I:%M:%S %p")
    return Koha
    #Metoda GAME
def GAME():
   randomN=[]
   f=0
   for i in range(36):
      number=random.randint(1,35)
      if f!=5:
          if number not in randomN:
              randomN.append(number)
              f=f+1
                  
      else:
        break
   randomN.sort()   
   str1 = ','.join(str(nr) for nr in randomN)
   return(str1)
    #Metoda CONVERT
def CONVERT(opsioni, numri):
    if(opsioni.lower().strip()== 'cmtofeets'):
        vlera = float(numri) * 0.032
    elif(opsioni.lower().strip() == 'feettocm'):
        vlera = float(numri) * 30.48
    elif(opsioni.lower().strip() == 'kmtomiles'):
        vlera = float(numri) * 0.6213
    elif(opsioni.lower().strip() == 'miletokm'):
        vlera = float(numri) * 1.609
    else:
        vlera = "Ky konvertim nuk mund të behet! Jepni një nga opsionet e mundshme të parapara për konvertim ."
    return vlera
    #Metoda GCF
def GCF(nr1,nr2):
    if nr1%nr2==0:
        return nr2
    return GCF(nr2,nr1%nr2)
    #Metoda MORSE
def MORSE(hyrja):
    code={' ':'/','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.'
          ,'o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-.','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','0': '-----','1':'.----','2':'..---'
          ,'3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.'}
    morseCode=""
    for x in hyrja:
        morseCode=morseCode+ code[x.lower()]
    return morseCode
    #Metoda BDAY
def bday(nrNjerezve):
    
    mostra = 1000 
    pershtatja = 0    

    for prova in range(mostra):
        ListaEdtl = []
        for i in range(nrNjerezve):
            dtl = random.randrange(365)
            ListaEdtl.append(dtl)

        dtlTeNjejta = False
        for num in ListaEdtl:
            if ListaEdtl.count(num) > 1:
               dtlTeNjejta = True

        if dtlTeNjejta == True:
            pershtatja += 1

    gjasa =float(pershtatja) / mostra
    return gjasa


def Pergjigjja(hyrja,adress):
   while True:
        try:
            data = hyrja.recv(128).decode()
        except socket.error:
            print("Klienti me IpAdresë " + address[0] + " u shkyq nga serveri ynë!")
            break
         
        listaEfjaleve = str(data).rsplit(" ")
        text = ""
        for fjalet in range(1, len(listaEfjaleve)):
            text += listaEfjaleve[fjalet]
            if(fjalet !=len(listaEfjaleve)):
                text += " "
        if not data:
            return
        elif(listaEfjaleve[0].lower().strip() =="ipadress"):
            data="IP Adresa e klientit është : " + IPADRESS()
        elif((listaEfjaleve[0].lower().strip() == "port")):
            data="Klienti është duke perdorur portin " + PORT()
        elif((listaEfjaleve[0].lower().strip() == "count")):
            data=str(COUNT(text)) 
        elif((listaEfjaleve[0].lower().strip() == "reverse")):
            data="Fjalia reverse: " + str(REVERSE(text))
        elif((listaEfjaleve[0].lower().strip() == "palindrome")):
            data=str(PALINDROME(listaEfjaleve[1])) 
        elif((listaEfjaleve[0].lower().strip() == "time")):
            data = TIME()
        elif((listaEfjaleve[0].lower().strip() == "game")):
            data="5 numrat e gjeneruar rastësisht nga 35 janë : " + GAME()
        elif((listaEfjaleve[0].lower().strip() == "convert")):
            data="Vlera e fituar është : " + str(CONVERT(listaEfjaleve[1],listaEfjaleve[2]))
        elif((listaEfjaleve[0].lower().strip() == "morse")):
            data=str(MORSE(text.strip()))
        elif((listaEfjaleve[0].lower().strip() == "bday")):
            try:
                line=int(listaEfjaleve[1])
                data= "Probabiliteti që në grupin prej "+str(line)+" njerëzve të ketë ditelindje të njejta është : "+str(bday(line))
            except socket.error:
                data="Shtypni komanden bday dhe numërin e njerëzve pjesëmarrës në atë vend"
        elif((listaEfjaleve[0].lower().strip() == "gcf")):
            try:
                line = int(listaEfjaleve[1])
                line1= int(listaEfjaleve[2])
                data="GCF "+ str(line) +" "+ str(line1) + " kthen si rezultat numërin "  + str(GCF(line,line1))
            except socket.error:
                data = "Shtypni komanden si të tillë GCF Numëri1 Numëri2"
        else:
            data = "Serveri nuk mund t'i përgjigjet kësaj kërkese!"
        hyrja.send(data.encode())
   #hyrja.close()

while True:
    data, address = serverSocket.accept()
    print("Serveri është lidhur me klientin me IpAdresë %s, në portin %s" % address )
    threading.Thread(target=Pergjigjja,args=(data,address)).start()

serverSocket.close()