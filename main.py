import Archivos
import Usuarios
import Herramienta
import menus
import Prestamos
import Reportes
import Logs

def iniciar():
    U=Archivos.cargar_datos("usuarios.json")
    H=Archivos.cargar_datos("herramientas.json")
    P=Archivos.cargar_datos("prestamos.json")
    Funciones= {
        # Herramientas
        'agregar_h':Herramienta.agregar_herramientas,
        'mostrar_h': Herramienta.mostrar_herramientas_todas,
        'buscar_h': Herramienta.buscar_herramienta,
        'actualizar_h':Herramienta.actualizar_herramienta,
        'inavilitar_h':Herramienta.inavilitar_herramienta,
        'eliminar_h':Herramienta.eliminar_herramienta,
        # Usuarios
        'agregar_u':Usuarios.agregar_Usuario,
        'mostrar_u':Usuarios.mostrar_usuarios,
        'buscar_u':Usuarios.buscar_usuario,
        'actualizar_u': Usuarios.actualizar_usuario,
        'eliminar_u':Usuarios.eliminar_usuario,
        # Comunidad
        'consultar_p': Herramienta.consultar_poseedor,       
        'resumen_b': Herramienta.mostrar_resumen_vecindario,
        # Prestamos
        'mis_prestamos':Prestamos.ver_mis_prestamos,
        'solicitar_p': Prestamos.solicitar_prestamo,    
        'gestionar_s': Prestamos.gestionar_solicitudes,  
        'mostrar_p': Prestamos.mostrar_prestamos_todos,   
        'reg_devolucion': Prestamos.registrar_devolucion,
        #reportes
        'rep_stock': Reportes.stock_bajo,
        'rep_estado': Reportes.prestamos_por_estado,
        'rep_historial': Reportes.historial_usuario,
        'rep_popular': Reportes.herramientas_populares,
        'rep_vencidos': Reportes.prestamos_vencidos,      
        'rep_usuarios': Reportes.usuarios_mas_activos,
        # LOgs
        'ver_eventos': Logs.ver_eventos,
        'ver_errores': Logs.ver_errores,
        'registrar_log': Logs.registrar_evento,
        'registrar_error': Logs.registrar_error,
        # Guardado
        'guardar': Archivos.guardar_datos,
    }
    menus.menu_principal(U,H,P,Funciones)

iniciar()

