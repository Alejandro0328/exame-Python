import json
def cargar_datos(nom_archivo):
    try:
        with open(nom_archivo, "r") as arch:
            return json.load(arch)
    except FileNotFoundError:
        return {}

def guardar_datos(datos, nom_archivo):
    try:
        with open(nom_archivo, "w") as arch:
            json.dump(datos, arch,indent=4)
            print(f"---Guardado exitoso en {nom_archivo} ---")
    except Exception as e:
        print(f"Error al guardar: {e}")

def guardar_datos_Prestamos_vencidos(datos, nom_archivo):
    try:
        with open(nom_archivo, "w",encoding="utf-8") as arch:
            arch.write("ID_Prestamo,Usuario.Herramiente,Cantidad_Prestada,fecha_inicio,fecha_estimada,dias_de_atrazo\n")
            for id_pv,info in datos.items():
                linea = f"{id_pv},{info['usuario']},{info['herramienta']},{info['cantidad']},{info['fecha_i']},{info['fecha_es']}\n"
                arch.write(linea)
            print(f"---Guardado exitoso en {nom_archivo} ---")

    except Exception as e:
        print(f"Error al guardar: {e}")
def cargar_prestamos_csv(nom_archivo):
    datos_vencidos = {}
    try:
        with open(nom_archivo, "r", encoding="utf-8") as arch:
            lineas = arch.readlines()
            
            # Si el archivo está vacío o solo tiene el encabezado, retornamos vacío
            if len(lineas) <= 1:
                return {}

            # Saltamos la primera línea (el encabezado)
            for linea in lineas[1:]:
                # Quitamos saltos de línea y separamos por comas
                partes = linea.strip().split(",")
                
                # Verificamos que la línea tenga todos los datos (6 columnas)
                if len(partes) == 6:
                    id_p = partes[0]
                    datos_vencidos[id_p] = {
                        "usuario": partes[1],
                        "herramienta": partes[2],
                        "cantidad": int(partes[3]),
                        "fecha_i": partes[4],
                        "fecha_es": partes[5]
                    }
        return datos_vencidos
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error al leer el reporte CSV: {e}")
        return {}

def guardar_prestamos_markdown(datos, nom_archivo):
    try:
        with open(nom_archivo, "w", encoding="utf-8") as arch:
            # Título y encabezado de la tabla Markdown
            arch.write("# REPORTE DE PRÉSTAMOS VENCIDOS\n\n")
            arch.write("| ID Préstamo | Usuario | Herramienta | Cantidad | Fecha Inicio | Fecha Entrega |\n")
            arch.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
            
            for id_pv, info in datos.items():
                # Creamos la fila usando el formato de tabla Markdown | dato | dato |
                fila = f"| {id_pv} | {info['usuario']} | {info['herramienta']} | {info['cantidad']} | {info['fecha_i']} | {info['fecha_es']} |\n"
                arch.write(fila)
                
            print(f"--- Reporte Markdown generado con éxito en {nom_archivo} ---")
    except Exception as e:
        print(f"Error al guardar Markdown: {e}")

def cargar_prestamos_markdown(nom_archivo):
    datos_vencidos = {}
    try:
        with open(nom_archivo, "r", encoding="utf-8") as arch:
            lineas = arch.readlines()
            
            # El contenido real de datos empieza en la línea 4 
            # (Línea 0: Título, 1: Vacío, 2: Encabezado, 3: Separador)
            if len(lineas) <= 4:
                return {}

            for linea in lineas[4:]:
                # Limpiamos los bordes de la tabla y separamos por '|'
                partes = [p.strip() for p in linea.strip().split("|") if p.strip()]
                
                if len(partes) == 6:
                    id_p = partes[0]
                    datos_vencidos[id_p] = {
                        "usuario": partes[1],
                        "herramienta": partes[2],
                        "cantidad": int(partes[3]),
                        "fecha_i": partes[4],
                        "fecha_es": partes[5]
                    }
        return datos_vencidos
    except FileNotFoundError:
        return {}
    except Exception as e:
        print(f"Error al leer el reporte Markdown: {e}")
        return {}