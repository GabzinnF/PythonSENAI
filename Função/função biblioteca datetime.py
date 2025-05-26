from datetime import datetime

def hd(n):
    print(datetime.now().hour,"Horas")
    h= datetime.now().hour
    if  h >= 0 and h <= 5:
        print("Boa Madruga",n)
    elif h >= 5.01 and h <= 12:
        print("Bom Dia",n,)
    elif h >= 12.01 and h <= 19:
        print("Boa Tarde",n)
    elif h >= 19.01 and h<= 23.59:
        print("Boa Noite",n)
        
n= input("Digite seu nome ")
    
hd(n)
    
