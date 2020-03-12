from io import open

Texto1_py = open("texto1.txt","w")
a = 0

for i in range(9): 
    a = a + 1
    x = str(a)
    Texto1_py.write("El número es:" + x + "\n") 

Texto1_py.close()





