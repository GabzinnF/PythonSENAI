
def conversor_temperatura_kelvins(c):
    k = c + 273
    return k

def conversor_temperatura_fahrenheit(c):
    f = c * 1.8 + 32
    return f





c= int(input("Celsius:"))
print(conversor_temperatura_kelvins(c),"Kelvins")

print(conversor_temperatura_fahrenheit(c),"Fahrenheit")
#ctk= conversor temperatura kelvins
#ctf= conversor temperatura fahrenheit
