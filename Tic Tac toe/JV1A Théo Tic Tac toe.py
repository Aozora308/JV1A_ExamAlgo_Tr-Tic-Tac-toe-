def myTable(tab):
    n = len(tab)
    #Traverse tout les elements
    for i in range(n):
        for j in range(0, n-i-1):
            # echanger si il est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]

X = 1
O = 2
Vide = 0

tab = [O,X,X,Vide,O,X,O,Vide,Vide]
taille = len(tab)
print(taille)

myTable(tab)

print ("le tableau trié est")
for i in range(len(tab)):
    print ("%d" %tab[i])
