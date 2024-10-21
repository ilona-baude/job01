print("Entrez un entier supérieur à zéro:")
n= input()
n=int(n)
x = 1
print("Table de multiplication de", n)
for x in range (1,11):
    result = n*x
    print(n, "x", x, "=", result)
    x+=1