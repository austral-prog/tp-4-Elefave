def line():
    a = float(input("Ingrese el coeficiente A: "))
    b = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    print("El coeficiente A de su ecuación de la recta es:",a)
    print("El coeficiente B de su ecuación de la recta es:",b)
    print("El coeficiente X1 de su ecuación de la recta es:",X1)
    print("El coeficiente X2 de su ecuación de la recta es:",X2)
    print("\nPara la siguiente ecuación:")
    print("\tY =",str(a) +"X +",b)
    Y1 = a*X1+b
    Y2 = a*X2+b
    print("\nDados los siguientes puntos:")
    print(f"\tP1 ({X1}, {Y1})")
    print(f"\tP2 ({X2}, {Y2})")
    distancia = ((X2-X1)**2+(Y2-Y1)**2)**.5
    print("")
    print("La distancia entre ellos es:",distancia)
