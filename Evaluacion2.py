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
while(True):
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
        pedido=int(input("Ingrese una opciòn: "))
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
            os.system('cls')
            print("Terminando pedido..." , "espere un momento", sep="\n")
            time.sleep(2)
            while(True):
                try:
                    print("1. Si")
                    print("2. No")
                    Codigo=int(input("¿Posee codigo de descuento?: "))
                    if Codigo==1:
                        soyotaku=input("Ingrese codigo de descuento: ")
                        if soyotaku=="soyotako":
                            print("Felicidades, se le aplicara un 10\\% de descuento en su compra")
                        else:
                            print("Codigo no vàlido")
                            print("Reingresar codigo (s)", "Volver al menu (x)", sep="\n")
                            Respuesta=input(": ")
                            if Respuesta=="s":
                                soyotaku=input("Ingrese codigo de descuento: ")
                                if soyotaku=="soyotako":
                                    print("Felicidades, se le aplicara un 10\\% de descuento en su compra")
                            elif Respuesta=="x":
                                print("Volviendo al menu...")
                                limpiar_pantalla()
                                continue
                            else:
                                print("Volviendo al menu...")
                                limpiar_pantalla()
                                continue
                    else:
                        print


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
 
