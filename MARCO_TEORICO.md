# Marco Teórico - Trabajo Práctico Integrador

## Gestión de Datos de Países en Python

---

## 1. LISTAS EN PYTHON

### 1.1 Definición

Las listas son estructuras de datos dinámicas que permiten almacenar colecciones ordenadas de elementos. En Python, las listas son mutables, lo que significa que pueden modificarse después de su creación.

### 1.2 Características Principales

- **Ordenadas**: Mantienen el orden de inserción de los elementos
- **Mutables**: Se pueden modificar (agregar, eliminar, cambiar elementos)
- **Heterogéneas**: Pueden contener elementos de diferentes tipos de datos
- **Indexadas**: Cada elemento tiene una posición (índice) comenzando desde 0

### 1.3 Sintaxis Básica

```python
# Crear lista vacía
paises = []

# Crear lista con elementos
continentes = ["África", "América", "Asia", "Europa", "Oceanía"]

# Acceder a elementos
primer_continente = continentes[0]  # "África"
```

### 1.4 Operaciones Comunes

- `append()`: Agregar elemento al final
- `len()`: Obtener cantidad de elementos
- `sorted()`: Ordenar elementos
- `for`: Iterar sobre elementos

### 1.5 Aplicación en el Proyecto

En nuestro sistema, utilizamos listas para almacenar la colección de países. Cada país es un diccionario, y todos se almacenan en una lista principal que permite iterar, buscar y ordenar eficientemente.

---

## 2. DICCIONARIOS EN PYTHON

### 2.1 Definición

Los diccionarios son estructuras de datos que almacenan pares clave-valor. Permiten acceder a los valores mediante claves únicas en lugar de índices numéricos.

### 2.2 Características Principales

- **Pares clave-valor**: Cada elemento tiene una clave única y un valor asociado
- **Mutables**: Se pueden modificar después de su creación
- **No ordenados** (Python < 3.7) o **Ordenados por inserción** (Python >= 3.7)
- **Acceso rápido**: Búsqueda de valores por clave en tiempo constante O(1)

### 2.3 Sintaxis Básica

```python
# Crear diccionario
pais = {
    "nombre": "Argentina",
    "poblacion": 45376763,
    "superficie": 2780400,
    "continente": "América"
}

# Acceder a valores
nombre_pais = pais["nombre"]  # "Argentina"
```

### 2.4 Operaciones Comunes

- Acceso por clave: `diccionario["clave"]`
- Modificación: `diccionario["clave"] = nuevo_valor`
- Agregar: `diccionario["nueva_clave"] = valor`
- Iterar: `for clave, valor in diccionario.items()`

### 2.5 Aplicación en el Proyecto

Cada país se representa como un diccionario con cuatro claves: nombre, población, superficie y continente. Esto permite un acceso semántico y claro a los datos, facilitando la lectura y mantenimiento del código.

---

## 3. FUNCIONES

### 3.1 Definición

Las funciones son bloques de código reutilizables que realizan una tarea específica. Permiten modularizar el programa, dividiendo problemas complejos en partes más manejables.

### 3.2 Características Principales

- **Modularización**: Una función = una responsabilidad
- **Reutilización**: El mismo código puede usarse múltiples veces
- **Parámetros**: Reciben datos de entrada
- **Retorno**: Pueden devolver resultados
- **Documentación**: Se documentan con docstrings

### 3.3 Sintaxis Básica

```python
def nombre_funcion(parametro1, parametro2):
    """
    Descripción de lo que hace la función.
    """
    # Código de la función
    resultado = parametro1 + parametro2
    return resultado
```

### 3.4 Tipos de Funciones en el Proyecto

- **Funciones de persistencia**: `cargar_paises()`, `guardar_paises()`
- **Funciones de validación**: `validar_numero_positivo()`, `pais_existe()`
- **Funciones de búsqueda**: `buscar_pais_por_nombre()`
- **Funciones del menú**: `agregar_pais()`, `filtrar_por_continente()`
- **Función principal**: `main()`

### 3.5 Ventajas de la Modularización

- Código más legible y mantenible
- Facilita la detección y corrección de errores
- Permite pruebas unitarias
- Favorece la reutilización de código

---

## 4. ESTRUCTURAS CONDICIONALES

### 4.1 Definición

Las estructuras condicionales permiten ejecutar diferentes bloques de código según se cumplan o no ciertas condiciones.

### 4.2 Tipos de Condicionales

#### 4.2.1 if - elif - else

```python
if condicion1:
    # código si condicion1 es verdadera
elif condicion2:
    # código si condicion2 es verdadera
else:
    # código si ninguna condición anterior es verdadera
```

#### 4.2.2 match - case (Python 3.10+)

```python
match variable:
    case valor1:
        # código para valor1
    case valor2:
        # código para valor2
    case _:
        # código por defecto
```

### 4.3 Operadores de Comparación

- `==`: Igual a
- `!=`: Diferente de
- `>`, `<`: Mayor/menor que
- `>=`, `<=`: Mayor/menor o igual que
- `in`: Pertenencia

### 4.4 Operadores Lógicos

- `and`: Y lógico
- `or`: O lógico
- `not`: Negación

### 4.5 Aplicación en el Proyecto

Utilizamos condicionales para:

- Validar entradas del usuario
- Verificar existencia de países
- Controlar flujo del menú principal
- Manejar diferentes casos de búsqueda y filtrado

---

## 5. ESTRUCTURAS REPETITIVAS

### 5.1 Definición

Las estructuras repetitivas (bucles o loops) permiten ejecutar un bloque de código múltiples veces.

### 5.2 Tipos de Bucles

#### 5.2.1 Bucle while

Ejecuta código mientras una condición sea verdadera.

```python
while condicion:
    # código a repetir
    # modificar condición para evitar bucle infinito
```

#### 5.2.2 Bucle for

Itera sobre una secuencia (lista, rango, etc.).

```python
for elemento in lista:
    # código a ejecutar para cada elemento
```

#### 5.2.3 for con range()

```python
for i in range(10):  # 0 a 9
    # código que usa el índice i
```

### 5.3 Control de Flujo en Bucles

- `break`: Termina el bucle inmediatamente
- `continue`: Salta a la siguiente iteración

### 5.4 Aplicación en el Proyecto

- `while True`: Para menús y validaciones hasta obtener entrada válida
- `for pais in paises`: Para recorrer todos los países
- `for i in range(len(paises))`: Para acceder a índices y valores

---

## 6. ALGORITMOS DE ORDENAMIENTO

### 6.1 Definición

Los algoritmos de ordenamiento reorganizan los elementos de una colección según un criterio específico (ascendente o descendente).

### 6.2 Función sorted() en Python

Python proporciona la función `sorted()` que implementa el algoritmo **Timsort**, una combinación optimizada de Merge Sort e Insertion Sort.

```python
# Función normal
def obtener_poblacion(pais):
    return pais["poblacion"]

# Ordenar lista de números
numeros_ordenados = sorted([3, 1, 4, 1, 5])  # [1, 1, 3, 4, 5]

# Ordenar con clave personalizada usando la función auxiliar
paises_ordenados = sorted(paises, key=obtener_poblacion)

# Orden descendente
paises_desc = sorted(paises, key=obtener_poblacion, reverse=True)
```

### 6.3 Aplicación en el Proyecto

Implementamos tres tipos de ordenamiento:

1. **Por nombre**: Orden alfabético usando `normalizar_texto()`
2. **Por población**: Numérico, ascendente o descendente
3. **Por superficie**: Numérico, ascendente o descendente

### 6.4 Complejidad Temporal

- Timsort: O(n log n) en el peor caso
- Eficiente para datos parcialmente ordenados

---

## 7. ESTADÍSTICAS BÁSICAS

### 7.1 Definición

Las estadísticas básicas son medidas que resumen y describen características de un conjunto de datos.

### 7.2 Medidas Implementadas

#### 7.2.1 Máximo y Mínimo

```python
def obtener_poblacion(pais):
    return pais["poblacion"]

pais_mayor_poblacion = max(paises, key=obtener_poblacion)
pais_menor_poblacion = min(paises, key=obtener_poblacion)
```

#### 7.2.2 Conteo por Categoría

```python
paises_por_continente = {}
for pais in paises:
    continente = pais["continente"]
    if continente in paises_por_continente:
        paises_por_continente[continente] += 1
    else:
        paises_por_continente[continente] = 1
```

### 7.3 Aplicación en el Proyecto

Calculamos:

- País con mayor/menor población
- Promedio de población mundial
- Promedio de superficie
- Distribución de países por continente
- Totales generales

---

## 8. ARCHIVOS CSV

### 8.1 Definición

CSV (Comma-Separated Values) es un formato de archivo de texto plano que almacena datos tabulares. Cada línea representa un registro, y los campos se separan por comas.

### 8.2 Estructura del CSV

```
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
```

### 8.3 Módulo csv de Python

#### 8.3.1 Lectura con csv.DictReader

```python
import csv

with open("paises.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["nombre"])  # Acceso por nombre de columna
```

#### 8.3.2 Escritura con csv.DictWriter

```python
import csv

with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["nombre", "poblacion", "superficie", "continente"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)
    escritor.writeheader()  # Escribir encabezados
    escritor.writerows(paises)  # Escribir todos los registros
```

### 8.4 Ventajas del Formato CSV

- **Simplicidad**: Fácil de leer y escribir
- **Interoperabilidad**: Compatible con Excel, Google Sheets, etc.
- **Ligereza**: Archivos de texto plano, sin overhead
- **Estándar**: Ampliamente soportado

### 8.5 Consideraciones Importantes

- **Encoding UTF-8**: Para caracteres especiales (ñ, acentos)
- **newline=""**: Evita líneas en blanco adicionales en Windows
- **Context Manager (with)**: Cierra automáticamente el archivo

### 8.6 Aplicación en el Proyecto

- **Persistencia**: Los datos se guardan permanentemente
- **Carga inicial**: Al iniciar, se cargan datos existentes
- **Guardado automático**: Cada modificación se guarda inmediatamente
- **Portabilidad**: El archivo CSV puede editarse externamente

---

## 9. MANEJO DE ERRORES Y VALIDACIONES

### 9.1Validaciones Implementadas

1. **Campos no vacíos**: `if texto.strip() == ""`
2. **Números positivos**: `if numero <= 0`
3. **Duplicados**: Verificación antes de agregar
4. **Rangos coherentes**: `if maximo >= minimo`
5. **Opciones válidas**: Validar entrada del menú

### 9.2 Importancia

- Evita crashes del programa
- Mejora la experiencia del usuario
- Mantiene integridad de los datos

---

## 10. FLUJO DE OPERACIONES PRINCIPALES

### 10.1 Diagrama de Flujo General

```
INICIO
  ↓
Cargar datos desde CSV
  ↓
Mostrar menú principal
  ↓
Leer opción del usuario
  ↓
Validar opción
  ↓
┌─────────────────────────────────────┐
│  Switch según opción seleccionada   │
├─────────────────────────────────────┤
│ 1. Agregar país                     │
│ 2. Actualizar país                  │
│ 3. Buscar país                      │
│ 4. Filtrar países                   │
│ 5. Ordenar países                   │
│ 6. Mostrar estadísticas             │
│ 7. Mostrar todos                    │
│ 8. Salir                            │
└─────────────────────────────────────┘
  ↓
Ejecutar función correspondiente
  ↓
¿Modificó datos?
  ├─ Sí → Guardar en CSV
  └─ No → Continuar
  ↓
¿Usuario desea salir?
  ├─ Sí → FIN
  └─ No → Volver al menú
```

### 10.2 Flujo de Agregar País

```
AGREGAR PAÍS
  ↓
Solicitar nombre
  ↓
¿Está vacío? → Sí → Mostrar error → Volver a solicitar
  ↓ No
¿Ya existe? → Sí → Mostrar mensaje → Volver al menú principal
  ↓ No
Solicitar población
  ↓
¿Es número positivo? → No → Mostrar error → Volver a solicitar
  ↓ Sí
Solicitar superficie
  ↓
¿Es número positivo? → No → Mostrar error → Volver a solicitar
  ↓ Sí
Mostrar lista de continentes disponibles y solicitar número
  ↓
¿Está vacío? → Sí → Mostrar error → Volver a solicitar
  ↓ No
¿Número válido? → No → Mostrar error → Volver a solicitar
  ↓ No
Crear diccionario del país
  ↓
Agregar a lista de países
  ↓
Guardar en CSV
  ↓
Mostrar confirmación
  ↓
RETURN
```

---

## 11. CONCLUSIONES

### 11.1 Aprendizajes Clave

1. **Estructuras de Datos**: La combinación de listas y diccionarios permite modelar datos complejos de forma eficiente y legible.

2. **Modularización**: Dividir el programa en funciones específicas facilita el desarrollo, testing y mantenimiento del código.

3. **Persistencia de Datos**: El uso de archivos CSV permite almacenar datos de forma permanente y portable.

4. **Validaciones**: Implementar validaciones robustas es fundamental para la integridad de los datos y la experiencia del usuario.

5. **Algoritmos**: Los algoritmos de búsqueda, filtrado y ordenamiento son herramientas esenciales para el procesamiento de datos.

### 11.2 Aplicaciones Prácticas

Este proyecto demuestra conceptos aplicables a:

- Sistemas de gestión empresarial
- Análisis de datos
- Aplicaciones web con bases de datos
- Procesamiento de información geográfica
- Reportes y estadísticas

### 11.3 Competencias Desarrolladas

- Programación estructurada
- Manejo de estructuras de datos
- Algoritmos de búsqueda y ordenamiento
- Persistencia de datos
- Validación de entradas
- Diseño de interfaces de usuario por consola
- Documentación de código
- Trabajo en equipo

---

---

**Elaborado por: Grupo 132**  
**Materia: Programación 1**  
**Institución: UTN - Tecnicatura Universitaria en Programación**  
**Año: 2025**
