import Archivos
import Prestamos
import menus
import Herramienta


def registar_reparacion(herramientas,Her_reparacion):
    menus.limpiar_pantalla()
    menus.imprimir_encabezado(" REGISTRAR HERRAMIENTA EN REPARACIÒN ")
    print("─"*50)
    if not herramientas:
        print("No hay herramientas registradas.".center(50))
        print("═"*50)
        input("\nPresione Enter para continuar...")
        return herramientas,Her_reparacion
    print(f"{'ID':<10}{'Nombre':<30}{'Estado':<10}")
    print("─"*50)

    
    for id, info in herramientas.items():
        print(f"{id:<10}{info['nombre']:<30}{info['estado']:<10}")
    while True:
            id_H = input("\n➤ ID de la Herramienta (o 'Salir'): ").strip().upper()
            if id_H == 'SALIR': return herramientas,Her_reparacion
            if id_H not in herramientas:
                    print(" No existe."); continue
            if herramientas[id_H]['estado'] != "Activo":
                    print(f" No disponible. Estado: {herramientas[id_H]['estado']}")
                    continue
                
            if herramientas[id_H]['stock'] <= 0:
               print(" Sin stock."); continue
            break
    print(F"VAS A MANDAR A REPARAR {herramientas[id_H]['nombre']} ")
    rta= input("¿ ESTAS SEGURO ? (Si/No): ").strip().capitalize()
    if rta == "Si":
        herramientas[id_H]['estado'] = "Taller" # Pongo "Taller" por que asi lo tengo en mi proyecto (Taller = Reparacion)
    else:
        print("Accion cacelada. Vuelva pronto")
        input("Presione cualquier tecla para continuar -->")
        return herramientas

    while True:
            f_inicio = input("➤ Fecha de inicio (DD-MM-AAAA): ").strip()
            if Prestamos.validar_fecha(f_inicio):break
            print(" Fecha inválida o formato incorrecto (Use DD-MM-AAAA).")
    while True:
            f_entrega = input("➤ Fecha estimada entrega (DD-MM-AAAA): ").strip()
            if Prestamos.validar_fecha(f_entrega):
                if Prestamos.fecha_a_numero(f_entrega) >= Prestamos.fecha_a_numero(f_inicio):break
                print(" La fecha de entrega no puede ser anterior al inicio.")
            else:
                print(" Fecha inválida.")
    for id_H, info in herramientas.items():
                obs=input("Observaciones: ")
                Her_reparacion[id_H] ={
                    "id_herramienta": id_H,
                    "nombre": info['nombre'],
                    "fecha_inicio": f_inicio,
                    "fecha_enrega": f_entrega,
                    "observaciones": obs
        }
                Archivos.guardar_datos(Her_reparacion,"reparaciones.json")
                Archivos.guardar_datos(herramientas,"herramientas.json")
                return herramientas,Her_reparacion
def mostrar_reparaciones(Reparaciones):
    menus.limpiar_pantalla()
    print(" -------------HERRAMIENTAS EN REPARACION--------------- ".center(90))
    print("─"*90)
    if not Reparaciones:
            print("No hay herramientas registradas.".center(90))
            print("═"*90)
            input("\nPresione Enter para continuar...")
            return Reparaciones

    print(f"{'ID':<10}{'Nombre':<30}{'Inicio':<20}{'Fin Est':<20}")
    print("-"*90)
    for id, info in Reparaciones.items():
        print(f"{id:<10}{info['nombre']:<30}{info['fecha_inicio']}{info['fecha_enrega']}")
    print("═"*90)
    input("-->")
        
                            


def menu():
    herramientas=Archivos.cargar_datos("herramientas.json")
    Her_reparaciones= Archivos.cargar_datos("reparaciones.json")           

    while True:
        menus.limpiar_pantalla()
        menus.imprimir_encabezado(" BIENVENIDO AL MODULO DE EXAMEN")
        print(" 1. Registar Reparacion")
        print(" 2. Mostrar Reparaciones")
        print(" 0. salir")
        print("─" * 50)
        
        op = input("\n Seleccione una opción: ")
        if op == "1":
            herramientas,Her_reparaciones=registar_reparacion(herramientas,Her_reparaciones)

        elif op == "2":
            mostrar_reparaciones(Her_reparaciones)
        elif op == "0":
            break
        else:
            print(" Opción no válida.")
            input("Presione Enter...")
def main():

    herramientas=Archivos.cargar_datos("herramientas.json")
    Her_reparaciones= Archivos.cargar_datos("reparaciones.json")           

    menu(herramientas,Her_reparaciones)
menu()