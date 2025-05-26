an=  int(input("Solicite um ano de nascimento"))

md = ""
m= 2025
m2 = m - an
print(m2, "Anos")

if m2 < 18:
    md = "é menor"
    
elif m2 > 18:
    md = " é maior"
    
print(md,"de idade")