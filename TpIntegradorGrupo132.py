# Trabajo Práctico Integrador - Grupo 132
# Gestión de Datos de Países en Python
# Alumnos: Gabriel Santostefano - Juan Santostefano

import csv
import os

NOMBRE_ARCHIVO = "paises.csv"

# ==================== FUNCIONES DE PERSISTENCIA CSV ====================

def cargar_paises():
    paises = []
    
    # Validación 1: Verificar si existe el archivo
    if not os.path.exists(NOMBRE_ARCHIVO):
        with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
            escritor.writeheader()
        return paises
    
    with open(NOMBRE_ARCHIVO, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            # Validación 2: Verificar que tenga todas las columnas
            if fila.get("nombre") and fila.get("poblacion") and fila.get("superficie") and fila.get("continente"):
                # Validación 3: Verificar que población y superficie sean números
                if fila["poblacion"].isdigit() and fila["superficie"].isdigit():
                    paises.append({
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    })
    
    return paises

def guardar_paises(paises):
    with open(NOMBRE_ARCHIVO, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["nombre", "poblacion", "superficie", "continente"])
        escritor.writeheader()
        escritor.writerows(paises)

# ==================== FUNCIONES DE VALIDACIÓN ====================

def normalizar_texto(texto):
    return " ".join(texto.strip().split()).lower()

def clave_nombre(pais):
    return normalizar_texto(pais["nombre"])

def clave_poblacion(pais):
    return pais["poblacion"]

def clave_superficie(pais):
    return pais["superficie"]

def validar_numero_positivo(numero_str):
    if not numero_str.isdigit():
        return False
    
    numero = int(numero_str)
    return numero > 0

def buscar_pais_por_nombre(paises, nombre):
    nombre_normalizado = normalizar_texto(nombre)
    
    for pais in paises:
        if normalizar_texto(pais["nombre"]) == nombre_normalizado:
            return pais
    
    return None

def pais_existe(paises, nombre):
    return buscar_pais_por_nombre(paises, nombre) is not None

# ==================== FUNCIONES DEL MENÚ ====================

def agregar_pais(paises):
    print("\n=====================Opción 1=========================")
    print("\nUsted eligió la Opción 1: Agregar País")
    
    # Validar nombre
    while True:
        nombre = input("\n>> Ingrese el nombre del país >> ").strip()
        
        if nombre == "":
            print("\n* El nombre no puede estar vacío!")
            continue
        
        if pais_existe(paises, nombre):
            print("\n* El país ya existe en el sistema!")
            return
        
        break
    
    # Validar población
    while True:
        poblacion_str = input(f">> Ingrese la población de {nombre} >> ").strip()
        
        if poblacion_str == "":
            print("\n* La población no puede estar vacía!")
            continue
        
        if validar_numero_positivo(poblacion_str):
            poblacion = int(poblacion_str)
            break
        else:
            print("\n* La población debe ser un número entero positivo!")
    
    # Validar superficie
    while True:
        superficie_str = input(f">> Ingrese la superficie en km² de {nombre} >> ").strip()
        
        if superficie_str == "":
            print("\n* La superficie no puede estar vacía!")
            continue
        
        if validar_numero_positivo(superficie_str):
            superficie = int(superficie_str)
            break
        else:
            print("\n* La superficie debe ser un número entero positivo!")
    
    # Validar continente
    continentes_validos = ["África", "América", "Asia", "Europa", "Oceanía", "Antártida"]
    
    print("\nContinentes disponibles:")
    for i, cont in enumerate(continentes_validos, 1):
        print(f"   {i}. {cont}")
    
    while True:
        continente_ingresado = input(f"\n>> Ingrese el número del continente de {nombre} (1 al 6) >> ").strip()
        
        if continente_ingresado == "":
            print("\n* El continente no puede estar vacío!")
            continue
        
        if continente_ingresado.isdigit():
            numero_continente = int(continente_ingresado)
            if 1 <= numero_continente <= len(continentes_validos):
                continente_seleccionado = continentes_validos[numero_continente - 1]
                break
            else:
                print(f"\n* Debe ingresar un número entre 1 y {len(continentes_validos)}!")
        else:
            print("\n* Debe ingresar un número válido del 1 al 6!")
    
    # Guardar datos normalizados
    nombre_normalizado = " ".join(nombre.split())
    paises.append({
        "nombre": nombre_normalizado,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente_seleccionado
    })
    
    print("\nOK - País agregado correctamente!")
    print(f"Nombre: {nombre_normalizado}")
    print(f"Población: {poblacion:,}")
    print(f"Superficie: {superficie:,} km²")
    print(f"Continente: {continente_seleccionado}")
    
    guardar_paises(paises)
    print("\nOK - Cambios guardados en el archivo CSV")

def actualizar_pais(paises):
    print("\n=====================Opción 2=========================")
    print("\nUsted eligió la Opción 2: Actualizar Población y Superficie")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        print("Primero debe agregar países (Opción 1)")
        return
    
    # Mostrar lista de países
    print("\nPaíses Disponibles:")
    print("=" * 90)
    print(f"{'N°':<4} {'País':<25} {'Población':<15} {'Superficie (km²)':<15} {'Continente':<15}")
    print("=" * 90)
    
    for i in range(len(paises)):
        numero = i + 1
        nombre = paises[i]["nombre"]
        poblacion = paises[i]["poblacion"]
        superficie = paises[i]["superficie"]
        continente = paises[i]["continente"]
        
        if len(nombre) > 23:
            nombre_mostrar = nombre[:20] + "..."
        else:
            nombre_mostrar = nombre
        
        print(f"{numero:<4} {nombre_mostrar:<25} {poblacion:<15,} {superficie:<15,} {continente:<15}")
    
    print("=" * 90)
    
    # Seleccionar país
    while True:
        print(f"\n>> Seleccione un país del 1 al {len(paises)}")
        seleccion_str = input("Ingrese número del país >> ").strip()
        
        if seleccion_str.isdigit():
            seleccion = int(seleccion_str)
            if 1 <= seleccion <= len(paises):
                pais = paises[seleccion - 1]
                print(f"\nPaís seleccionado: '{pais['nombre']}'")
                print(f"Población actual: {pais['poblacion']:,}")
                print(f"Superficie actual: {pais['superficie']:,} km²")
                break
            else:
                print(f"\n* Número debe estar entre 1 y {len(paises)}")
        else:
            print("\n* Debe ingresar un número válido!")
    
    # Actualizar población
    while True:
        poblacion_str = input(f"\n>> Ingrese la nueva población >> ").strip()
        
        if validar_numero_positivo(poblacion_str):
            poblacion_anterior = pais["poblacion"]
            pais["poblacion"] = int(poblacion_str)
            break
        else:
            print("\n* La población debe ser un número entero positivo!")
    
    # Actualizar superficie
    while True:
        superficie_str = input(f">> Ingrese la nueva superficie en km² >> ").strip()
        
        if validar_numero_positivo(superficie_str):
            superficie_anterior = pais["superficie"]
            pais["superficie"] = int(superficie_str)
            break
        else:
            print("\n* La superficie debe ser un número entero positivo!")
    
    print("\nOK - Datos actualizados correctamente!")
    print(f"País: '{pais['nombre']}'")
    print(f"Población: {poblacion_anterior:,} → {pais['poblacion']:,}")
    print(f"Superficie: {superficie_anterior:,} km² → {pais['superficie']:,} km²")
    
    guardar_paises(paises)
    print("\nOK - Cambios guardados en el archivo CSV")

def buscar_pais(paises):
    print("\n=====================Opción 3=========================")
    print("\nUsted eligió la Opción 3: Buscar País por Nombre")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        return
    
    nombre_buscar = input("\n>> Ingrese el nombre del país a buscar >> ").strip()
    
    if nombre_buscar == "":
        print("\n* No puede ingresar texto vacío!")
        return
    
    # Búsqueda con coincidencia parcial
    nombre_buscar_normalizado = normalizar_texto(nombre_buscar)
    resultados = []
    
    for pais in paises:
        nombre_pais_normalizado = normalizar_texto(pais["nombre"])
        if nombre_buscar_normalizado in nombre_pais_normalizado:
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"\n* No se encontraron países que coincidan con: '{nombre_buscar}'")
    elif len(resultados) == 1:
        pais = resultados[0]
        print(f"\nOK - País encontrado:")
        print("=" * 60)
        print(f"Nombre: {pais['nombre']}")
        print(f"Población: {pais['poblacion']:,}")
        print(f"Superficie: {pais['superficie']:,} km²")
        print(f"Continente: {pais['continente']}")
        print("=" * 60)
    else:
        print(f"\nOK - Se encontraron {len(resultados)} países:")
        print("=" * 90)
        print(f"{'N°':<4} {'País':<25} {'Población':<15} {'Superficie (km²)':<15} {'Continente':<15}")
        print("=" * 90)
        
        for i, pais in enumerate(resultados, 1):
            nombre = pais["nombre"]
            if len(nombre) > 23:
                nombre_mostrar = nombre[:20] + "..."
            else:
                nombre_mostrar = nombre
            
            print(f"{i:<4} {nombre_mostrar:<25} {pais['poblacion']:<15,} {pais['superficie']:<15,} {pais['continente']:<15}")
        
        print("=" * 90)

def filtrar_por_continente(paises):
    print("\n=================Filtrar por Continente================")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        return
    
    # Obtener continentes únicos
    continentes = set()
    for pais in paises:
        continentes.add(pais["continente"])
    
    continentes_lista = sorted(list(continentes))
    
    print("\nContinentes disponibles:")
    for i, cont in enumerate(continentes_lista, 1):
        print(f"   {i}. {cont}")
    
    continente_seleccionado = None
    
    while True:
        continente_ingresado = input(f"\n>> Ingrese el número del continente (1 al {len(continentes_lista)}) >> ").strip()
        
        if continente_ingresado == "":
            print("\n* No puede ingresar texto vacío!")
            continue
        
        if continente_ingresado.isdigit():
            numero_continente = int(continente_ingresado)
            if 1 <= numero_continente <= len(continentes_lista):
                continente_seleccionado = continentes_lista[numero_continente - 1]
                break
            else:
                print(f"\n* Debe ingresar un número entre 1 y {len(continentes_lista)}!")
        else:
            print("\n* Debe ingresar un número válido!")
    
    # Filtrar países
    continente_normalizado = normalizar_texto(continente_seleccionado)
    resultados = []
    
    for pais in paises:
        if normalizar_texto(pais["continente"]) == continente_normalizado:
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"\n* No se encontraron países en el continente: '{continente_seleccionado}'")
    else:
        print(f"\nOK - Países en {continente_seleccionado} ({len(resultados)}):")
        print("=" * 90)
        print(f"{'N°':<4} {'País':<25} {'Población':<15} {'Superficie (km²)':<15} {'Continente':<15}")
        print("=" * 90)
        
        for i, pais in enumerate(resultados, 1):
            nombre = pais["nombre"]
            if len(nombre) > 23:
                nombre_mostrar = nombre[:20] + "..."
            else:
                nombre_mostrar = nombre
            
            print(f"{i:<4} {nombre_mostrar:<25} {pais['poblacion']:<15,} {pais['superficie']:<15,} {pais['continente']:<15}")
        
        print("=" * 90)

def filtrar_por_poblacion(paises):
    print("\n================Filtrar por Población=================")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        return
    
    # Solicitar rango
    while True:
        min_str = input("\n>> Ingrese población mínima >> ").strip()
        if min_str.isdigit():
            poblacion_min = int(min_str)
            break
        else:
            print("\n* Debe ingresar un número válido!")
    
    while True:
        max_str = input(">> Ingrese población máxima >> ").strip()
        if max_str.isdigit():
            poblacion_max = int(max_str)
            if poblacion_max >= poblacion_min:
                break
            else:
                print("\n* La población máxima debe ser mayor o igual a la mínima!")
        else:
            print("\n* Debe ingresar un número válido!")
    
    # Filtrar países
    resultados = []
    for pais in paises:
        if poblacion_min <= pais["poblacion"] <= poblacion_max:
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"\n* No se encontraron países con población entre {poblacion_min:,} y {poblacion_max:,}")
    else:
        print(f"\nOK - Países con población entre {poblacion_min:,} y {poblacion_max:,} ({len(resultados)}):")
        print("=" * 90)
        print(f"{'N°':<4} {'País':<25} {'Población':<15} {'Superficie (km²)':<15} {'Continente':<15}")
        print("=" * 90)
        
        for i, pais in enumerate(resultados, 1):
            nombre = pais["nombre"]
            if len(nombre) > 23:
                nombre_mostrar = nombre[:20] + "..."
            else:
                nombre_mostrar = nombre
            
            print(f"{i:<4} {nombre_mostrar:<25} {pais['poblacion']:<15,} {pais['superficie']:<15,} {pais['continente']:<15}")
        
        print("=" * 90)

def filtrar_por_superficie(paises):
    print("\n================Filtrar por Superficie================")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        return
    
    # Solicitar rango
    while True:
        min_str = input("\n>> Ingrese superficie mínima (km²) >> ").strip()
        if min_str.isdigit():
            superficie_min = int(min_str)
            break
        else:
            print("\n* Debe ingresar un número válido!")
    
    while True:
        max_str = input(">> Ingrese superficie máxima (km²) >> ").strip()
        if max_str.isdigit():
            superficie_max = int(max_str)
            if superficie_max >= superficie_min:
                break
            else:
                print("\n* La superficie máxima debe ser mayor o igual a la mínima!")
        else:
            print("\n* Debe ingresar un número válido!")
    
    # Filtrar países
    resultados = []
    for pais in paises:
        if superficie_min <= pais["superficie"] <= superficie_max:
            resultados.append(pais)
    
    if len(resultados) == 0:
        print(f"\n* No se encontraron países con superficie entre {superficie_min:,} y {superficie_max:,} km²")
    else:
        print(f"\nOK - Países con superficie entre {superficie_min:,} y {superficie_max:,} km² ({len(resultados)}):")
        print("=" * 90)
        print(f"{'N°':<4} {'País':<25} {'Población':<15} {'Superficie (km²)':<15} {'Continente':<15}")
        print("=" * 90)
        
        for i, pais in enumerate(resultados, 1):
            nombre = pais["nombre"]
            if len(nombre) > 23:
                nombre_mostrar = nombre[:20] + "..."
            else:
                nombre_mostrar = nombre
            
            print(f"{i:<4} {nombre_mostrar:<25} {pais['poblacion']:<15,} {pais['superficie']:<15,} {pais['continente']:<15}")
        
        print("=" * 90)

def menu_filtrar(paises):
    print("\n=====================Opción 4=========================")
    print("\nUsted eligió la Opción 4: Filtrar Países")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        return
    
    print("\n>> Seleccione tipo de filtro:")
    print("   1. Por Continente")
    print("   2. Por Rango de Población")
    print("   3. Por Rango de Superficie")
    
    while True:
        filtro_str = input("\nIngrese opción (1, 2 o 3) >> ").strip()
        
        if filtro_str == "1":
            filtrar_por_continente(paises)
            break
        elif filtro_str == "2":
            filtrar_por_poblacion(paises)
            break
        elif filtro_str == "3":
            filtrar_por_superficie(paises)
            break
        else:
            print("\n* Opción inválida! Ingrese 1, 2 o 3")

def ordenar_paises(paises):
    print("\n=====================Opción 5=========================")
    print("\nUsted eligió la Opción 5: Ordenar Países")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        return
    
    print("\n>> Seleccione criterio de ordenamiento:")
    print("   1. Por Nombre")
    print("   2. Por Población")
    print("   3. Por Superficie")
    
    while True:
        criterio_str = input("\nIngrese opción (1, 2 o 3) >> ").strip()
        
        if criterio_str in ["1", "2", "3"]:
            criterio = int(criterio_str)
            break
        else:
            print("\n* Opción inválida! Ingrese 1, 2 o 3")
    
    # Para nombre, siempre ascendente. Para población y superficie, preguntar orden
    if criterio == 1:
        paises_ordenados = sorted(paises, key=clave_nombre)
        texto_orden = "alfabético"
    else:
        print("\n>> Seleccione orden:")
        print("   1. Ascendente (menor a mayor)")
        print("   2. Descendente (mayor a menor)")
        
        while True:
            orden_str = input("\nIngrese opción (1 o 2) >> ").strip()
            
            if orden_str == "1":
                orden_descendente = False
                texto_orden = "ascendente"
                break
            elif orden_str == "2":
                orden_descendente = True
                texto_orden = "descendente"
                break
            else:
                print("\n* Opción inválida! Ingrese 1 o 2")
        
        if criterio == 2:
            paises_ordenados = sorted(paises, key=clave_poblacion, reverse=orden_descendente)
        else:  # criterio == 3
            paises_ordenados = sorted(paises, key=clave_superficie, reverse=orden_descendente)
    
    # Mostrar resultados
    criterios = {1: "Nombre", 2: "Población", 3: "Superficie"}
    print(f"\nOK - Países ordenados por {criterios[criterio]} ({texto_orden}):")
    print("=" * 90)
    print(f"{'N°':<4} {'País':<25} {'Población':<15} {'Superficie (km²)':<15} {'Continente':<15}")
    print("=" * 90)
    
    for i, pais in enumerate(paises_ordenados, 1):
        nombre = pais["nombre"]
        if len(nombre) > 23:
            nombre_mostrar = nombre[:20] + "..."
        else:
            nombre_mostrar = nombre
        
        print(f"{i:<4} {nombre_mostrar:<25} {pais['poblacion']:<15,} {pais['superficie']:<15,} {pais['continente']:<15}")
    
    print("=" * 90)

def mostrar_estadisticas(paises):
    print("\n=====================Opción 6=========================")
    print("\nUsted eligió la Opción 6: Mostrar Estadísticas")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        return
    
    # Calcular estadísticas
    pais_mayor_poblacion = max(paises, key=clave_poblacion)
    pais_menor_poblacion = min(paises, key=clave_poblacion)
    
    total_poblacion = 0
    total_superficie = 0
    
    for pais in paises:
        total_poblacion += pais["poblacion"]
        total_superficie += pais["superficie"]
    
    promedio_poblacion = total_poblacion / len(paises)
    
    promedio_superficie = total_superficie / len(paises)
    
    # Contar países por continente
    paises_por_continente = {}
    for pais in paises:
        continente = pais["continente"]
        if continente in paises_por_continente:
            paises_por_continente[continente] += 1
        else:
            paises_por_continente[continente] = 1
    
    # Mostrar estadísticas
    print("\n" + "=" * 70)
    print("               ESTADÍSTICAS DE PAÍSES")
    print("=" * 70)
    
    print("\n[POBLACION]:")
    print(f"   • País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']:,})")
    print(f"   • País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']:,})")
    print(f"   • Promedio de población: {promedio_poblacion:,.0f}")
    
    print("\n[SUPERFICIE]:")
    print(f"   • Promedio de superficie: {promedio_superficie:,.0f} km²")
    
    print("\n[PAISES POR CONTINENTE]:")
    for continente in sorted(paises_por_continente.keys()):
        cantidad = paises_por_continente[continente]
        print(f"   • {continente}: {cantidad} país(es)")
    
    print("\n[TOTALES]:")
    print(f"   • Total de países registrados: {len(paises)}")
    print(f"   • Población mundial total: {total_poblacion:,}")
    print(f"   • Superficie mundial total: {total_superficie:,} km²")
    
    print("=" * 70)

def mostrar_todos_los_paises(paises):
    print("\n=====================Opción 7=========================")
    print("\nUsted eligió la Opción 7: Mostrar Todos los Países")
    
    if len(paises) == 0:
        print("\n* No hay países registrados!")
        print("El sistema está vacío")
        return
    
    print("\n============= LISTADO DE PAISES =============")
    print("=" * 90)
    print(f"{'N°':<4} {'País':<25} {'Población':<15} {'Superficie (km²)':<15} {'Continente':<15}")
    print("=" * 90)
    
    for i in range(len(paises)):
        numero = i + 1
        nombre = paises[i]["nombre"]
        poblacion = paises[i]["poblacion"]
        superficie = paises[i]["superficie"]
        continente = paises[i]["continente"]
        
        if len(nombre) > 23:
            nombre_mostrar = nombre[:20] + "..."
        else:
            nombre_mostrar = nombre
        
        print(f"{numero:<4} {nombre_mostrar:<25} {poblacion:<15,} {superficie:<15,} {continente:<15}")
    
    print("=" * 90)
    print(f"\nTotal de países registrados: {len(paises)}")

def confirmar_continuar():
    while True:
        confirmacion = input("\n>> Presione Enter para volver al menú >> ").strip()
        if confirmacion == "":
            break
        else:
            print("\n* Presione solo Enter para continuar!")

# ==================== PROGRAMA PRINCIPAL ====================

def main():
    paises = cargar_paises()
    
    print("\n" + "=" * 70)
    print("        SISTEMA DE GESTIÓN DE DATOS DE PAÍSES")
    print("        Trabajo Práctico Integrador - Grupo 132")
    print("        Programación 1 - UTN-TUP")
    print("=" * 70)
    print(f"\nCatálogo cargado desde '{NOMBRE_ARCHIVO}'")
    print(f"Países registrados: {len(paises)}")
    
    while True:
        print("\n" + "=" * 70)
        print("=====================| MENÚ PRINCIPAL |=====================")
        print("=" * 70)
        print("\n>>  1 - Agregar País")
        print(">>  2 - Actualizar Población y Superficie")
        print(">>  3 - Buscar País por Nombre")
        print(">>  4 - Filtrar Países")
        print(">>  5 - Ordenar Países")
        print(">>  6 - Mostrar Estadísticas")
        print(">>  7 - Mostrar Todos los Países")
        print(">>  8 - Salir")
        print("\n" + "=" * 70)
        
        while True:
            opcion_str = input("\n>>  Seleccione una opción del 1 al 8 >> ").strip()
            
            if opcion_str == "":
                print("\n* Debe ingresar una opción!")
                continue
            
            if opcion_str.isdigit():
                opcion = int(opcion_str)
                if 1 <= opcion <= 8:
                    break
                else:
                    print("\n* Error! La opción debe ser un número del 1 al 8!")
            else:
                print("\n* Error! La opción debe ser un número del 1 al 8!")
        
        match opcion:
            case 1:
                agregar_pais(paises)
                confirmar_continuar()
                
            case 2:
                actualizar_pais(paises)
                confirmar_continuar()
                
            case 3:
                buscar_pais(paises)
                confirmar_continuar()
                
            case 4:
                menu_filtrar(paises)
                confirmar_continuar()
                
            case 5:
                ordenar_paises(paises)
                confirmar_continuar()
                
            case 6:
                mostrar_estadisticas(paises)
                confirmar_continuar()
                
            case 7:
                mostrar_todos_los_paises(paises)
                confirmar_continuar()
                
            case 8:
                print("\n=====================Opción 8=========================")
                print("\nUsted eligió la Opción 8 - Salir")
                
                while True:
                    confirmacion = input("\n>> ¿Está seguro de que desea salir? (S/N) >> ").upper().strip()
                    if confirmacion == "S":
                        print("\n" + "=" * 70)
                        print("    Gracias por usar el Sistema de Gestión de Países")
                        print("    Todos los cambios han sido guardados")
                        print("    Trabajo Práctico Integrador - Grupo 132")
                        print("=" * 70)
                        print("\n===================Fin del Programa===================\n")
                        return
                    elif confirmacion == "N":
                        print("\nRegresando al menú principal...")
                        break
                    else:
                        print("\n* Opción inválida! Ingrese S o N")
            
            case _:
                print("\n* Error! La opción debe ser un número del 1 al 8!")
                confirmar_continuar()


main()
