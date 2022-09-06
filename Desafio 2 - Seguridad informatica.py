##Valentina Valdivia
#Benjamin Retamales

import requests 

abc  = "abcdefghijklmnopqrstuvwxyz "
def CesarCifr(mensaje,n): #Funcion Cesar , recibe el mendasaje a cifrar y en n , este es la clave de cesar , en nuestro caso es 8 y 12 
    cifrado =""
    for l in mensaje: #Como el abc esta en mayuscula, el mensaje recibido se transforma en mayuscula
            if l in abc:
                i = abc.find(l)
                i += n
                if i >=26 :
                    i -= 26
                cifrado += abc[i]

            else:
                    cifrado + l 
            
    return cifrado

def CesarDes(cifrado,n):
    mensaje =""
    for l in cifrado:
        if l in abc:
                e = abc.find(l)
                e -=n
                if e<0:
                    e+=26
                  
                mensaje += abc[e]
        else:
                mensaje+ l
    return mensaje


def get_desp(char):
    return (ord(char.upper())-65)


def vigenereCif(mensaje,clave):
    cifrado = ""
    for i in range(0,len(mensaje)):
        des = get_desp(clave[i % len(clave)]) #Desplazamiento de la clave
        cifrado+=(CesarCifr(mensaje[i],des)) #Usamos Cesar
    return cifrado

def vigenereDescif(mensaje,clave):
    cifrado = ""
    for i in range(0,len(mensaje)):
        des = get_desp(clave[i % len(clave)]) #Desplazamiento de la clave
        cifrado+=(CesarDes(mensaje[i],des)) #Usamos Cesar
    return cifrado


def main():
    run = True
    while (run):
        print(" 1) Desafio N°2")
        print(" 2) Salir")
        opcion = int(input("Indique su opción : "))
        print("-------------------------------------------------------------")


        if (opcion ==1):
            headers = {
                'Content-Type': 'text/plain',
            }
            response = requests.get('https://finis.mmae.cl/GetMsg', headers=headers)
            mensajeE = response.json()
            mensajeD = mensajeE['msg'].lower()
            print("El mensaje a decifrar es:",mensajeD)
            cesar3 = CesarDes(mensajeD,12)
            vigenere3 = vigenereDescif(cesar3,"finispasswd")
            decifrado = CesarDes(vigenere3,8)
            print(decifrado)

        else:
            print("Saliendo")
            run = False

main()


