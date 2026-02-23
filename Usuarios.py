def agregar_Usuario(usuario,dic_fun):
    print("\n" + "═"*40)
    print(" 👤 REGISTRAR NUEVO USUARIO ".center(40))
    print("═"*40)
    
    id_U = input("➤ Ingrese el ID Usuario: ").strip().upper()
    if id_U in usuario:
        print("\n❌ El Usuario ya existe.....")
        dic_fun['registrar_error'] (f"REGISTRO FALLIDO: ID ya Existente {id_U}")
        input("Presione Enter para continuar -->")
        return usuario
        
    nombre = input("➤ Nombre del Usuario: ").strip().capitalize()
    apellidos = input("➤ Apellidos del Usuario: ").strip().capitalize()
    
    while True:
        telefono = input("➤ Número de teléfono (10 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 10:
            break
        print("❌ ERROR: El número debe ser de 10 dígitos numéricos.")
        dic_fun['registrar_error'] (f" AGREGAR_U: Valor no Valido ({telefono})")

        input("Presione Enter para volver intentar ->")
        
    direccion = input("➤ Dirección del usuario: ").strip().capitalize() 
    
    while True:
        tipo = input("➤ Tipo (Administrador/Residente): ").strip().capitalize()
        if tipo == "Administrador" or tipo == "Residente":
            break
        print("❌ ERROR: Tipo no válido. Ingrese (Administrador/Residente)")
        dic_fun['registrar_error'] (f" AGREGAR_U: Categoria no Valida ({tipo})")
        input("-->")

    usuario[id_U] = {
        "id":id_U,
        "nombre": nombre,
        "apellido": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }
    print("\n✅ ¡Usuario registrado con éxito!")
    input("Presione Enter para continuar...")
    return usuario

def mostrar_usuarios(usuarios):
    print("\n" + "═"*90)
    print(" 👥 LISTADO DE USUARIOS ".center(90))
    print("═"*90)
    
    if not usuarios:
        print("📭 No hay Usuarios registrados.".center(90))
        print("═"*90)
        return usuarios


    print(f"{'ID Usuario':<12}{'Nombre Completo':<30}{'Teléfono':<15}{'Dirección':<20}{'Tipo':<10}")
    print("─"*90)

    for id, info in usuarios.items():
        nombre_completo = f"{info['nombre']} {info['apellido']}"
        print(f"{id:<12}{nombre_completo:<30}{info['telefono']:<15}{info['direccion']:<20}{info['tipo']:<10}")
    
    print("═"*90)
    input("\nPresione Enter para continuar -->")

def buscar_usuario(Usuarios):
    while True:
        print("\n" + "🔍" + "─"*38)
        print(" ¿QUÉ USUARIO BUSCAS? ".center(40))
        print("─"*40)
        
        usuarios_bus = input("➤ Ingrese Nombre o Tipo de Usuario: ").strip().capitalize()
        encontrado = False
        
        print("\nResultados:")
        print("─"*40)
        for id, info in Usuarios.items():
            if usuarios_bus in info['nombre']:
                print(f"✔️ Encontrado: {info['nombre']} {info['apellido']} | ID: {id}")
                encontrado = True
            elif usuarios_bus in info['tipo']:
                print(f"✔️ Tipo: {info['tipo']} | Nombre: {info['nombre']} | ID: {id}")
                encontrado = True
        
        if not encontrado:
            print("❌ No hay coincidencias encontradas.")
        
        print("─"*40)
        continuar = input("\n¿Deseas seguir buscando? (Si/No): ").strip().capitalize()
        if continuar != "Si":
            break

def actualizar_usuario(Usuarios,dic_fun):
    print("\n" + "🔄" + "─"*38)
    print(" ACTUALIZAR USUARIO ".center(40))
    print("─"*40)
    
    id_U = input("➤ ID del Usuario a actualizar: ").strip().upper()
    if id_U not in Usuarios:
        print("\n❌ Este Usuario no existe :(")
        dic_fun['registrar_error'] (f"BUSQUEDA FALLIDA: ID No Existente {id_U}")
        input("Presione Enter para continuar -->")
        return Usuarios
        
    nombre = input("➤ Nuevo Nombre: ").strip().capitalize()
    apellidos = input("➤ Nuevos Apellidos: ").strip().capitalize()
    
    while True:
        telefono = input("➤ Nuevo teléfono (10 dígitos): ").strip()
        if telefono.isdigit() and len(telefono) == 10:
            break
        print("❌ ERROR: Debe tener 10 números.")
        dic_fun['registrar_error'] (f" AGREGAR_U: Valor no Valido ({telefono})")
        input("Reintentar ->")
        
    direccion = input("➤ Nueva Dirección: ").strip().capitalize() 
    
    while True:
        tipo = input("➤ Nuevo Tipo (Administrador/Residente): ").strip().capitalize()
        if tipo == "Administrador" or tipo == "Residente":
            break
        print("❌ ERROR: Tipo no válido.")
        dic_fun['registrar_error'] (f" AGREGAR_U: Categoria no Valida ({tipo})")
        input("-->")
    
    Usuarios[id_U] = {
        "id":id_U,
        "nombre": nombre,
        "apellido": apellidos,
        "telefono": telefono,
        "direccion": direccion,
        "tipo": tipo
    }
    print("\n✅ ¡Usuario actualizado correctamente!")
    input("Presione Enter para continuar...")
    return Usuarios

def eliminar_usuario(usuarios,dic_fun):
    print("\n" + "🗑️" + "─"*38)
    print(" ELIMINAR USUARIO ".center(40))
    print("─"*40)
    
    id_U = input("➤ Ingrese el ID del Usuario: ").strip().upper()
    if id_U not in usuarios:
        print("\n❌ El Usuario no existe....")
        dic_fun['registrar_error'] (f"BUSQUEDA FALLIDA: ID No Existente {id_U}")
        input("Presione Enter para continuar -->")
        return usuarios
        
    print(f"\n❗ ¡VAS A ELIMINAR A!: {usuarios[id_U]['nombre']}")
    confirmar = input("¿Estás seguro de ELIMINAR? (Si/No): ").strip().capitalize()

    if confirmar == "Si":
        del usuarios[id_U]
        print("\n✅ Usuario eliminado satisfactoriamente.")
    else:
        print("\n❌ Acción cancelada.")
    
    input("\nPresione Enter para continuar -->")
    return usuarios