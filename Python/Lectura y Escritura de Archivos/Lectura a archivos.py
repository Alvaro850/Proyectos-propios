from io import open

Texto1_py = open("texto1.txt","r")
Texto1_py_L = len(Texto1_py.read())

Texto1_py.seek(0)
Last_number = Texto1_py.readline(2)

Texto1_py.close()


