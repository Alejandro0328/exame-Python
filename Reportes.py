import menus
import Prestamos 
def usuarios_mas_activos(prestamos):
    print("\n" + "🏆" + "─"*38)
    print(" USUARIOS CON MÁS SOLICITUDES ".center(40))
    print("─"*40)
    
    conteo = {}
    for p in prestamos.values():
        u = p['usuario']
        conteo[u] = conteo.get(u, 0) + 1
    
    # Ordenar de mayor a menor
    for nombre in sorted(conteo, key=conteo.get, reverse=True):
        print(f"👤 {nombre:<20} | Préstamos: {conteo[nombre]}")
        
    input("\nPresione Enter...")
def prestamos_vencidos(prestamos):
    print("\n" + "⏰" + "─"*38)
    print(" REPORTE: PRÉSTAMOS VENCIDOS ".center(40))
    print("─"*40)
    
    # Pedir la fecha actual para comparar
    hoy_str = input("➤ Ingrese la fecha de hoy (DD-MM-AAAA): ").strip()
    
    if not Prestamos.validar_fecha(hoy_str):
        print("❌ Fecha inválida.")
        return

    hoy_num = Prestamos.fecha_a_numero(hoy_str)
    encontrado = False
    
    print(f"\n{'ID':<10}{'Usuario':<20}{'Herramienta':<20}{'Venció el':<15}")
    print("─"*65)

    for id_p, info in prestamos.items():
        # Solo verificamos préstamos que aún están "Activos"
        if info['estado'] == "Activo":
            fecha_vence_num = Prestamos.fecha_a_numero(info['fecha_entrega'])
            
            # Si la fecha de entrega es menor a hoy, está vencido
            if fecha_vence_num < hoy_num:
                print(f"{id_p:<10}{info['usuario']:<20}{info['herramienta']:<20}{info['fecha_entrega']:<15}")
                encontrado = True
                
    if not encontrado:
        print("✅ No hay préstamos vencidos a la fecha.")
    
    input("\nPresione Enter para continuar...")
def stock_bajo(herramientas):
    while True:
        cantidad = input("➤ Cantidad de Stock (Minima) : ").strip()
        if cantidad.isdigit(): # Verifica que sean solo números
            stock = int(cantidad)
            break
        print("❌ ERROR: Ingrese un número entero válido.")
        input("-->")
    print("\n" + "⚠️" + "─"*38)
    print(f" REPORTE: STOCK BAJO (< {stock}) ".center(40))
    print("─"*40)
    
    encontrado = False
    print(f"{'ID':<10}{'Herramienta':<20}{'Stock':<10}")
    print("─"*40)
    
    for id, info in herramientas.items():
        if info['stock'] < stock:
            print(f"{id:<10}{info['nombre']:<20}{info['stock']:<10}")
            encontrado = True
            
    if not encontrado:
        print("✅ Todas las herramientas tienen stock suficiente.")
    input("\nPresione Enter para continuar...")
    
def prestamos_por_estado(prestamos):
    menus.imprimir_encabezado("📊 ESTADO DE PRÉSTAMOS")
    print("1. Ver Activos\n2. Ver En Trámite\n3. Ver Devueltos")
    op = input("\n➤ Seleccione: ")
    
    estados = {"1": "Activo", "2": "En trámite", "3": "Devuelto"}
    seleccion = estados.get(op)
    
    if seleccion:
        print(f"\nListado de préstamos: {seleccion}")
        print("─"*60)
        for id, info in prestamos.items():
            if info['estado'] == seleccion:
                print(f"ID: {id} | Usuario: {info['usuario']} | Herramienta: {info['herramienta']}")
    input("\nPresione Enter...")

def historial_usuario(prestamos):
    busqueda = input("➤ Ingrese nombre del usuario para ver su historial: ").strip().capitalize()
    print(f"\n📜 Historial para: {busqueda}")
    print("─"*60)
    
    for id, info in prestamos.items():
        if busqueda in info['usuario']:
            print(f"Fecha: {info['fecha_inicio']} | {info['herramienta']} | Estado: {info['estado']}")
    input("\nPresione Enter...")

def herramientas_populares(prestamos):
    conteo = {}
    for p in prestamos.values():
        h = p['herramienta']
        conteo[h] = conteo.get(h, 0) + 1
    
    # Ordenar de mayor a menor
    top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)
    
    print("\n🏆 HERRAMIENTAS MÁS SOLICITADAS")
    for nombre, total in top[:5]: # Top 5
        print(f"➤ {nombre}: {total} veces")
    input("\nPresione Enter...")
    