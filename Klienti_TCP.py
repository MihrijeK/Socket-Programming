import socket
import sys
import re

def Ndrysho():
    print("Jep IP Adresen:")
    serverName=input()
    print("Jep numërin e portit: ")
    port=int(input())
    addr = (serverName, port)
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(addr)
        kerkesa = input("Kërkesa juaj : ")
        while True:
            clientSocket.sendall(str.encode(kerkesa))
            data = clientSocket.recv(128)
            print(data.decode("utf-8"))
            kerkesa = input("Kërkesa juaj : ")
            if(kerkesa.lower().strip()=='ndrysho'):
                Ndrysho()
    except socket.error as mesazhi:
        print("Krijimi i Soketit dështojë provo qasjen në një server tjetër . " + str(mesazhi))        
                  
def Validimi(kerkesa):
    if kerkesa.lower().strip()=='ipadress':
        return('IPADRESS')

    elif 'ipadress'in kerkesa.lower():
        print('Për metodën ipaddress ju duhet të shkruani IPADRESS')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif kerkesa.lower().strip()=='port':
        return('PORT')

    elif 'port'in kerkesa.lower():
        print('Për metodën port ju duhet të shkruani PORT')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')
        
    elif re.match('(count) ([a-z])+',kerkesa.lower()):
        return(kerkesa)

    elif 'count'in kerkesa.lower():
        print('Për metodën count ju duhet të shkruani COUNT teksti')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif re.match('(reverse) ([a-z 0-9!@#$%^&.,;])+',kerkesa.lower()):
        return(kerkesa)

    elif 'reverse'in kerkesa.lower():
        print('Për metodën reverse ju duhet të shkruani REVERSE Teksti')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif re.match('(palindrome) ([a-z 0-9])+',kerkesa.lower()):
        return(kerkesa)

    elif 'palindrome' in kerkesa.lower():
        print('Për metodën palindrome ju duhet të shkruani PALINDROME teksti')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif kerkesa.lower().strip()=='time':
        return('TIME')

    elif 'time' in kerkesa.lower():
        print('Për metodën time ju duhet të shkruani TIME')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif kerkesa.lower().strip()=='game':
        return('GAME')

    elif 'game'in kerkesa.lower():
        print('Për metodën game ju duhet të shkruani GAME')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif re.match('(convert) ([a-zA-Z]+) ([0-9])',kerkesa.lower()):
        return(kerkesa)
    
    elif 'convert' in kerkesa.lower():
        print("Për metodën convert ju duhet të shkruani CONVERT OPSIONI Numër")
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif re.match('(gcf) ([0-9]+) ([0-9]+)',kerkesa.lower()):
        return(kerkesa)

    elif 'gcf' in kerkesa.lower():
        print("Për metodën gcf ju duhet të shkruani GCF Numëri1 Numëri2")
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif re.match('(morse) ([a-zA-Z 0-9])+',kerkesa.lower()):
        return(kerkesa)

    elif 'morse' in kerkesa.lower():
        print('Për metodën morse ju duhet të shkruani MORSE teksti')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')

    elif re.match('(bday) ([0-9]+)',kerkesa.lower()):
        return(kerkesa)

    elif 'bday'in kerkesa.lower():
        print('Për metodën bday ju duhet të shkruani bday numër')
        return('Nuk mund të ofrohet kjo metodë. Përmbaju rregullës së shkrimit të kërkesës.')
    elif '' in kerkesa.lower():
        return('Nuk mund të ofrohet kjo metodë . Provo një tjetër.')

print("Jep Ip Adresen (default localhost): ")
serverName=input()
print("Jep numërin e portit (default 13000): ")
port=input()
if serverName=="" or serverName=="localhost":
    serverName="localhost"
if port=="" or port=="13000":
    port=13000
addr = (serverName, port)
try:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(addr)
except socket.error as mesazhi:
    print("Krijimi i Soketit dështojë provo qasjen në një server tjetër . "+ str(mesazhi))
    Ndrysho()

print('                                         Mirë se vini!                                                  ')
print('Serveri FIEK-TCP përmban këto kërkesa (metoda):  \nIPADRESS, '+
      'PORT, COUNT, REVERSE, PALINDROME, TIME, GAME,'+
      'CONVERT(cmToFeets, FeetToCm, kmToMiles, MileToKm),GCF,MORSE,BDAY \nPer IPADRESS shkruaj  IPADRESS '+
      '\nPer PORT : PORT \nPer COUNT : COUNT Tekstin'+
      '\nPer REVERSE : REVERSE tekstin '+
      '\nPer PALINDROME : PALINDROME Tekstin'+
      '\nPer TIME : TIME \nPer GAME : GAME '+
      '\nPer CONVERT: CONVERT OPSIONI Numëri '+
      '\nPer GCF: GCF Numëri1 Numëri2'+
      '\nPer MORSE CODE: MORSE Tekstin'+
      '\nPer BDAY: BDAY Numër'+
      '\nNëse dëshironi të ndërroni portin shtyp : NDRYSHO '+
      '\nNëse dëshironi të ndaloni komunikimin me serverin tonë shtyp : NDALO ')
try:
    print('')
    kerkesa = input("Kërkesa juaj : ")
    i = 1
    while(i==1):
        if(kerkesa.lower().strip() == 'ndalo'):
            i = 2 
            clientSocket.close()
            print("Lidhja me serverin tonë është mbyllur, Cdo të mirë për ty!")
        elif(kerkesa.lower().strip()=='ndrysho'):
                Ndrysho()
        else:
            Kontrollo=Validimi(kerkesa)
            clientSocket.sendall(str.encode(Kontrollo))
            data = clientSocket.recv(128).decode("utf-8")
            print(data)
            kerkesa = input("Kërkesa juaj : ")
except:
    print("Nuk mund të arrihet qasja me këtë server. ")