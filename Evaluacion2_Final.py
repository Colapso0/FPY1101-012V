import os
import time
def limpiar_pantalla():
    print("La pantalla se limpiara en segundos...")
    time.sleep(2)
    os.system('cls')
pikachu=0
otako=0
pulpo=0
anguila=0
Menu=True
#Menu
while(Menu==True):
    while(True):
        os.system("cls")
        print("Hola bienvenido a delivery de Sushi" , "Ofrecemos un menu de roll con 4 tipos distintos", sep="\n")
        print("1. Pikachu Roll $4500") 
        print("2. Otaku Roll $5000")
        print("3. Pulpo Venenoso Roll $5200")
        print("4. Anguila Eléctrica Roll $4800")
        print("5. Terminar pedido")
        print(f"\n\n\nPikachu Roll= {pikachu}" ) 
        print(f"Otaku Roll= {otako}")
        print(f"Pulpo Venenoso Roll= {pulpo}")
        print(f"Anguila Eléctrica Roll= {anguila}")
        try:
            pedido=int(input("Ingrese una opcion: "))
            if pedido >=1 and pedido <=4:
                if pedido==1:
                    pikachu+=1
                elif pedido==2:
                    otako+=1
                elif pedido==3:
                    pulpo+=1
                elif pedido==4:
                    anguila+=1
                continue
            elif pedido==5:
                Total_Rolls=pikachu+otako+pulpo+anguila
                Sub_total=(pikachu*4500)+(otako*5000)+(pulpo*5200)+(anguila*4800)
                os.system('cls')
                print("Terminando pedido..." , "espere un momento", sep="\n")
                time.sleep(2)
                #Pregunta descuento
                p=1
                while(p==1):
                    Descuento=0
                    try:
                        print("1. Si")
                        print("2. No")
                        Codigo=int(input("¿Posee codigo de descuento?: "))
                        if Codigo==1:
                            soyotaku=input("\nIngrese codigo de descuento: ")
                            if soyotaku=="soyotako":
                                print("\n\t\tFelicidades, se le aplicara un 10\\% de descuento en su compra")
                                Descuento=Sub_total*0.1
                                break
                            else:
                                R=1
                                while(R==1):
                                    print("\n\t\tCodigo no vàlido")
                                    print("\nReingresar codigo (s)", "Volver al menu (x)", sep="\n")
                                    Respuesta=input(": ")
                                    if Respuesta=="s":
                                        soyotaku=input("Ingrese codigo de descuento: ")
                                        if soyotaku=="soyotako":
                                            print("\n\t\tFelicidades, se le aplicara un 10\\% de descuento en su compra")
                                            Descuento=Sub_total*0.1
                                            break
                                        else:
                                            R=1

                                    elif Respuesta=="x":
                                        print("Volviendo al menu...")
                                        limpiar_pantalla()
                                        R=0
                                        p=0
                                        continue
                                    else:
                                        print("Volviendo al menu...")
                                        limpiar_pantalla()
                                        R=0
                                        p=0
                                        continue
                        else:
                            break



                    except ValueError:
                        print("Ingrese una opcion valida (1-2)")
                        continue 
            else:
                print("Ingrese una opcion valida (1-4)")
                limpiar_pantalla()
                continue
        except ValueError:
            print("Ingrese un digito entre 1-4")
            limpiar_pantalla()
            continue
        if p==0:
                    continue
        limpiar_pantalla()
        Total=int(Sub_total-Descuento)
        print("*****************************") 
        print(f"Total Productos= {Total_Rolls}")
        print("*****************************") 
        print(f"\nPikachu Roll= {pikachu}" ) 
        print(f"Otaku Roll= {otako}")
        print(f"Pulpo Venenoso Roll= {pulpo}")
        print(f"Anguila Eléctrica Roll= {anguila}")
        print("\n*****************************")
        print(f"Subtotal por pagar= {Sub_total}")
        print(f"Descuento por codigo= {Descuento}")    
        print(f"Total= {Total}")    
        break

    Otra=input=("¿Desea realizar otra compra? (si/no): ")
    if Otra=="si":
        Menu=True
    else:
        Menu=False