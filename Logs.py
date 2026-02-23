def registrar_evento(mensaje):
    """
    Guarda un evento en el archivo logs.txt. 
    """
    # Creamos la línea del evento
    linea = f" EVENTO: {mensaje}\n"
    
    try:
        with open("Eventos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except:
        pass

    
    print("─"*50)
    input("\nPresione Enter para continuar...")
def registrar_error(mensaje):
    """
    Guarda un evento en el archivo logs.txt. 
    """
    # Creamos la línea del error
    linea = f" ERROR: {mensaje}\n"
    
    try:
        with open("Errores.txt", "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except:
        pass

# --- Visiules de logs ---

def ver_eventos():
    print("\n" + "📜" + "─"*48)
    print(" REGISTRO DE EVENTOS (ACTIVIDAD) ".center(50))
    print("─"*50)
    try:
        with open("Eventos.txt", "r", encoding="utf-8") as archivo:
            print(archivo.read() or " No hay eventos registrados.")
    except FileNotFoundError:
        print(" Archivo de Eventos no encontrado.")
    input("\nPresione Enter...")

def ver_errores():
    print("\n" + "⚠️" + "─"*48)
    print(" REGISTRO DE ERRORES CRÍTICOS ".center(50))
    print("─"*50)
    try:
        with open("Errores.txt", "r", encoding="utf-8") as archivo:
            print(archivo.read() or " No hay errores registrados.")
    except FileNotFoundError:
        print(" Archivo de Errores no encontrado.")
    input("\nPresione Enter...")

def registrar_Pretamo_vencido(mensaje):
    """
    Guarda un evento en el archivo logs.txt. 
    """
    # Creamos la línea del evento
    linea = f""
    
    try:
        with open("Eventos.csv", "a", encoding="utf-8") as archivo:
            archivo.write(linea)
    except:
        pass

    
    print("─"*50)
    input("\nPresione Enter para continuar...")