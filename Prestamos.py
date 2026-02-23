def validar_fecha(fecha_str):
    if len(fecha_str) < 10: 
        return False
    # Comprobar longitud básica y guiones
    if fecha_str[2] != '-' or fecha_str[5] != '-':
        return False
    
    partes = fecha_str.split('-')
    if len(partes) != 3: return False
    
    try:
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
        
        if mes < 1 or mes > 12: return False
        
        # Días por mes
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Ajuste para bisiestos
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_mes[1] = 29
            
        if dia < 0 or dia > dias_mes[mes-1]:
            return False
            
        return True
    except:
        return False
def validar_fecha(fecha_str):
    if len(fecha_str) < 10: 
        return False
    # Comprobar longitud básica y guiones
    if fecha_str[2] != '-' or fecha_str[5] != '-':
        return False
    
    partes = fecha_str.split('-')
    if len(partes) != 3: return False
    
    try:
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
        
        if mes < 1 or mes > 12: return False
        
        # Días por mes
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Ajuste para bisiestos
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            dias_mes[1] = 29
            
        if dia < 0 or dia > dias_mes[mes-1]:
            return False
            
        return True
    except:
        return False
def fecha_a_numero(fecha_str):
    """Convierte DD-MM-AAAA en un entero AAAAMMDD para comparar."""
    partes = fecha_str.split('-')
    # Ejemplo: '15-02-2024' -> '2024' + '02' + '15' -> 20240215
    return int(partes[2] + partes[1] + partes[0])



def solicitar_prestamo(usuario_actual, herramientas, prestamos,dic_fun):
    print("\n" + "═"*50)
    print(" 📑 CREAR NUEVA SOLICITUD DE PRÉSTAMO ".center(50))
    print("═"*50)
    print(f" Solicitante: {usuario_actual['nombre']} {usuario_actual['apellido']}")
    print("─" * 50)

    # 1. Bucle Herramienta
    while True:
        id_H = input("\n➤ ID de la Herramienta (o 'EXIT'): ").strip().upper()
        if id_H == 'EXIT': return prestamos, herramientas
        if id_H not in herramientas:
            print(" No existe."); continue
        if herramientas[id_H]['estado'] != "Activo":
            print(f" No disponible. Estado: {herramientas[id_H]['estado']}")
            dic_fun['registrar_log'](f"FALLO: {usuario_actual['nombre']} pidió {id_H} (No Activa)")
            continue
        
        if herramientas[id_H]['stock'] <= 0:
            print(" Sin stock."); continue
        break

    # 2. Bucle Cantidad
    while True:
        try:
            cant = int(input(f"➤ Cantidad (Disponible {herramientas[id_H]['stock']}): "))
            if 0 < cant <= herramientas[id_H]['stock']: break
            print(" Cantidad inválida.")
        except: print(" Ingrese números.")

    # 3. Bucle ID Préstamo
    while True:
        id_P = input("➤ ID para esta solicitud (ej: P100): ").strip().upper()
        if id_P not in prestamos:break
        print(" ID ya en uso.")

    # 4. Bucle Fecha Inicio
    while True:
        f_inicio = input("➤ Fecha de inicio (DD-MM-AAAA): ").strip()
        if validar_fecha(f_inicio):break
        print(" Fecha inválida o formato incorrecto (Use DD-MM-AAAA).")

        
    

    # 5. Bucle Fecha Entrega
    while True:
        f_entrega = input("➤ Fecha estimada entrega (DD-MM-AAAA): ").strip()
        if validar_fecha(f_entrega):
            # Validación extra: que la entrega no sea antes que el inicio (comparación simple de strings)
            if fecha_a_numero(f_entrega) >= fecha_a_numero(f_inicio):break
            print(" La fecha de entrega no puede ser anterior al inicio.")
        else:
            print(" Fecha inválida.")

    obs = ("")

    # Registro
    prestamos[id_P] = {
        "id_prestamo": id_P,
        "usuario": f"{usuario_actual['nombre']} {usuario_actual['apellido']}",
        "id_usuario": usuario_actual.get('id'),
        "herramienta": herramientas[id_H]['nombre'],
        "id_herramienta": id_H,
        "cantidad": cant,
        "fecha_inicio": f_inicio,
        "fecha_entrega": f_entrega,
        "estado": "En trámite",
        "observaciones": obs
    }
    
    
    dic_fun['registrar_log'](f"SOLICITUD: {id_P} creada por {usuario_actual['nombre']}")
    print("\n✅ Solicitud registrada en espera de aprobación.")
    return prestamos, herramientas
def gestionar_solicitudes(prestamos, herramientas):
    print("\n" + "═"*100)
    print("   APROBACIÓN DE SOLICITUDES (ADMIN) ".center(100))
    print("═"*100)
    
    # Filtramos solicitudes pendientes
    pendientes = [id_p for id_p, p in prestamos.items() if p['estado'] == "En trámite"]
    
    if not pendientes:
        print(" No hay solicitudes pendientes de aprobación.".center(100))
        print("═"*100)
        input("\nPresione Enter para volver...")
        return prestamos, herramientas

    print(f"{'ID Préstamo':<15}{'Stock':<15}{'Usuario':<35}{'Herramienta':<20}{'Fecha de Inicio':<20}")
    print("─"*100)
    for id_p in pendientes:
        print(f"{id_p:<15}{prestamos[id_p]['cantidad']:<15}{prestamos[id_p]['usuario']:<35}{prestamos[id_p]['herramienta']:<20}{prestamos[id_p]['fecha_inicio']:<20}")
    
    print("─"*100)
    id_S = input("\n➤ ID del préstamo a gestionar (o EXIT para salir): ").strip().upper()

    if id_S == 'EXIT': return prestamos, herramientas

    if id_S in pendientes:
        id_H = prestamos[id_S]['id_herramienta']
        cant_solicitada = prestamos[id_S]['cantidad']
        
        while True:
            accion = input("¿Desea ACTIVAR o RECHAZAR el préstamo? ").strip().upper()
            
            if accion == "RECHAZAR":
                razon = input(" ➤ Ingrese el motivo del rechazo (observación): ").strip()
                prestamos[id_S]['estado'] = "Rechazado"
                prestamos[id_S]['observaciones'] = razon
                print(f"\n❌ Solicitud {id_S} rechazada correctamente.")
                break
                
            elif accion == "ACTIVAR":
                # Verificamos si hay stock suficiente para la cantidad pedida
                if herramientas[id_H]['stock'] >= cant_solicitada:
                    prestamos[id_S]['estado'] = "Activo"
                    herramientas[id_H]['stock'] -= cant_solicitada
                    
                    print(f"\n✅ Préstamo {id_S} activado correctamente.")
                    print(f"📦 Stock actualizado de {herramientas[id_H]['nombre']}: {herramientas[id_H]['stock']}")
                    break 
                else:
                    print(f"\nError: No hay stock suficiente (Disponibles: {herramientas[id_H]['stock']}).")
                    print("Debe RECHAZAR la solicitud o esperar a que devuelvan herramientas.")
                    break 
            else:
                print("\n Opción no válida. Escriba ACTIVAR o RECHAZAR.")
    else:
        print("\n ID no válido o la solicitud no está 'En trámite'.")
    
    input("\nPresione Enter para continuar...")
    return prestamos, herramientas

def mostrar_prestamos_todos(prestamos):
    print("\n" + "═"*100)
    print(" 📊 HISTORIAL GLOBAL DE PRÉSTAMOS ".center(100))
    print("═"*100)
    
    if not prestamos:
        print(" No hay registros de préstamos.".center(100))
        print("═"*100)
        return prestamos

    print(f"{'ID':<10}{'Usuario':<20}{'Herramienta':<20}{'Estado':<15}{'Entrega':<15}")
    print("─"*100)

    for id, info in prestamos.items():
        print(f"{id:<10}{info['usuario']:<20}{info['herramienta']:<20}{info['estado']:<15}{info['fecha_entrega']:<15}") 
    
    print("═"*100)

def registrar_devolucion(prestamos, herramientas):
    print("\n" + "📥" + "─"*38)
    print(" REGISTRAR DEVOLUCIÓN ".center(40))
    print("─"*40)
    
    id_P = input("➤ ID del Préstamo a devolver: ").strip().upper()
    
    if id_P not in prestamos:
        print("\n ID de préstamo no encontrado.")
        return prestamos, herramientas
    
    if prestamos[id_P]['estado'] != "Activo":
        print(f"\n No se puede devolver. El estado actual es: {prestamos[id_P]['estado']}")
        input("Presione Enter para continuar -->")
        return prestamos, herramientas

    print(f"\nRecibiendo: {prestamos[id_P]['herramienta']} de {prestamos[id_P]['usuario']}")
    confirmar = input("¿Confirmar devolución física? (Si/No): ").strip().capitalize()

    if confirmar == "Si":

        prestamos[id_P]['estado'] = "Devuelto"
        
        id_H = prestamos[id_P]['id_herramienta']
        herramientas[id_H]['stock'] += prestamos[id_P]['cantidad']
        
        print(f"\n✅ Devolución procesada. Stock de {herramientas[id_H]['nombre']} restaurado.")
    else:
        print("\n Acción cancelada.")
    
    return prestamos, herramientas

def ver_mis_prestamos(prestamos, usuario_sesion):
    print("\n" + "═" * 100)
    print(f" 📂 ESTADO DE MIS PRÉSTAMOS ".center(60))
    print(f" Usuario: {usuario_sesion['nombre']} {usuario_sesion['apellido']} ".center(100))
    print("═" * 100)
    
    id_actual = usuario_sesion.get('id')
    encontrado = False


    print(f"{'ID':<8} {'Herramienta':<18} {'Cant.':<7} {'Estado':<12} {'Observaciones':<30}")
    print("─" * 100)

    for id_p, info in prestamos.items():

        if info.get('id_usuario') == id_actual:
            encontrado = True
            herramienta = info.get('herramienta')
            cantidad = info.get('cantidad')
            estado = info.get('estado')
            observacion = info.get('observaciones')
            
            print(f"{id_p:<8} {herramienta[:17]:<18} {cantidad:<7} {estado:<12} {observacion:<30}")

    if not encontrado:
        print("     No tienes solicitudes o préstamos registrados.".center(60))
    
    print("─" * 100)

 