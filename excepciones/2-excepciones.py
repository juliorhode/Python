# ----------------- Inicio de la funcion -----------------
def divide():
    try:
        op1 = (float(input("Introduce el primer numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))
        print("La division es: " + str(op1/op2))

    # except ValueError:
        # print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividor entre 0")

    # Captura generica de excepcion
    except:
        print("Ha ocurrido un error")

    # Lo que va aqui, siempre se va a ejecutar
    finally:
        print("Calculo finalizado")
# ----------------- Fin de la funcion -----------------

divide()