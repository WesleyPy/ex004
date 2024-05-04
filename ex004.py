n = str(input('Digite algo: '))
print(f''' 
    Tipo: {type(n)}
    É Alpha númerico? {n.isalnum()},
    É alpha? {n.isalpha()},
    É Minuscula? {n.islower()},
    É maiuscula? {n.isupper()},
    Está capitalizada? {n.istitle()},
    É Decimal? {n.isdecimal()},
    É numérica? {n.isnumeric()},
    É espaço? {n.isspace()}
      ''')