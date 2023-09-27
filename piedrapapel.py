#Lectura de datos
print("Bienvenido a piedra, papel, tijera, lagarto o spock")
jugador1=input("Jugador 1 introduce tu jugada: ")
jugador2=input("Jugador 2 introduce tu jugada: ")

#Cálculos
#Si hay un empate
if jugador1==jugador2:
    print("Empate")
#en caso de no haber empate
else:
    #Si el jugador 1 saca tijeras
    if jugador1=="tijeras":
        if jugador2=="spock" or jugador2=="piedra":
            print("El Jugador 2 gana")
        else:
            #Si el jugador 1 saca papel
            if jugador1=="papel":
                if jugador2=="tijeras" or jugador2=="lagarto":
                    print("El Jugador 2 gana")
                else:
                    #Si el jugador 1 saca piedra
                    if jugador1=="piedra":
                        if jugador2=="papel" or jugador2=="spock":
                            print("El Jugador 2 gana")
                        else:
                            #Si el jugador 1 saca lagarto
                            if jugador1=="lagarto":
                                if jugador2=="piedra" or jugador2=="tijeras":
                                    print("El Jugador 2 gana")
                                else:
                                    #Si el jugador 1 saca spock
                                    if jugador1=="spock":
                                        if jugador2=="lagarto" or jugador2=="papel":
                                            print("El jugador 2 gana")
                                        else:
                                            print("El jugador 1 gana")
                                    else:
                                        print("El jugador 1 gana")
                            else:
                                print("El jugador 1 gana")
                    else:   
                        print("El jugador 1 gana")
            else:
                print("El jugador 1 gana")
    else:
        print("El jugador 1 gana")

     
