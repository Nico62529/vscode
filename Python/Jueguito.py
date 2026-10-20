import random

def jueguito():

    
    numero_aleatorio = random.randint(1, 100)
    intentos = 0
    max_intentos = 10
    
    print("=========================================")
    print(" BIENVENIDO A MI PRIMER PROYECTO (INTENTO)")
    print("=========================================")

    user = input("Introduce tu nombre de usuario temporal:")
    print("Voy a pensar en un numero de 1-100")
    print(f"Tienes un maximo de {max_intentos} intentos para adivinarlo sino pierdes.\n")
    
    while intentos < max_intentos:
        try:
            intento_usuario = int(input("Introduce tu numero: "))
        except ValueError:
            print("Por favor, introduce un numero que sea valido.")
            continue
            
        intentos += 1
        
        if intento_usuario < numero_aleatorio:
            print("🔼 Mas alto... Intentalo de nuevo!")
        elif intento_usuario > numero_aleatorio:
            print("🔽 Mas bajo... Intentalo de nuevo!")
        else:
            print(f"\n¡FELICIDADES {user}!")
            print(f"Lograste adivinar el numero en {intentos} intentos.")
            return
            
        print(f"Te quedan {max_intentos - intentos} intentos.\n")
        
    print(f"\nOh no... ¡Te quedaste sin intentos!")
    print(f"GG. El numero secreto era el {numero_aleatorio}. Suerte a la otra!")


