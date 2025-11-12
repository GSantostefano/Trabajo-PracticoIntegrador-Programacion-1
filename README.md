# Trabajo Práctico Integrador - Gestión de Datos de Países

## Descripción del Programa

Sistema de gestión de información sobre países desarrollado en Python que permite realizar operaciones de consulta, filtrado, ordenamiento y análisis estadístico sobre un conjunto de datos almacenados en formato CSV.

El programa implementa las estructuras de datos fundamentales aprendidas en Programación 1 (listas y diccionarios) y ofrece una interfaz de consola intuitiva para la gestión completa de información geográfica y demográfica.

## Integrantes del Grupo 132

- Gabriel Santostefano
- Juan Santostefano

## Funcionalidades Principales

### 1. Agregar País

- Permite agregar un nuevo país al sistema
- Solicita: nombre, población, superficie y continente
- El continente se elige ingresando el número que figura en la lista desplegada
- Valida que no existan campos vacíos
- Verifica que el país no exista previamente (si existe, vuelve al menú principal)
- Guarda automáticamente los cambios en el archivo CSV

### 2. Actualizar Población y Superficie

- Permite modificar la población y superficie de un país existente
- Muestra los valores actuales antes de la actualización
- Confirma los cambios realizados
- Actualiza el archivo CSV automáticamente

### 3. Buscar País por Nombre

- Búsqueda con coincidencia parcial (no requiere nombre exacto)
- Insensible a mayúsculas/minúsculas
- Muestra todos los países que coincidan con el criterio
- Despliega información completa del país encontrado

### 4. Filtrar Países

Submenú con tres opciones de filtrado:

#### 4.1 Por Continente

- Muestra continentes disponibles en el sistema (solo los que tienen países cargados)
- El usuario selecciona el continente ingresando el número correspondiente
- Filtra países del continente seleccionado
- Muestra resultados en tabla ordenada

#### 4.2 Por Rango de Población

- Solicita población mínima y máxima
- Filtra países dentro del rango especificado
- Valida que el rango sea coherente

#### 4.3 Por Rango de Superficie

- Solicita superficie mínima y máxima en km²
- Filtra países dentro del rango especificado
- Valida que el rango sea coherente

### 5. Ordenar Países

Permite ordenar por tres criterios:

- **Por Nombre**: Orden alfabético ascendente
- **Por Población**: Ascendente o descendente
- **Por Superficie**: Ascendente o descendente

Los resultados se muestran en una tabla formateada.

### 6. Mostrar Estadísticas

Calcula y muestra:

- País con mayor población
- País con menor población
- Promedio de población mundial
- Promedio de superficie
- Cantidad de países por continente
- Total de países registrados
- Población mundial total
- Superficie mundial total

### 7. Mostrar Todos los Países

- Lista completa de países registrados
- Formato de tabla ordenada
- Información completa de cada país
- Contador de total de registros

### 8. Salir

- Confirmación antes de cerrar
- Garantiza que todos los cambios estén guardados

## Instrucciones de Uso

### Requisitos Previos

- Python 3.x instalado en el sistema
- Archivo `paises.csv` en la misma carpeta que el programa

### Ejecución del Programa

1. Abrir una terminal o consola
2. Navegar hasta la carpeta del proyecto:

```bash
cd tpIntegradorProgramacion
```

3. Ejecutar el programa:

```bash
python TpIntegradorGrupo132.py
```

### Uso del Menú

1. El programa mostrará el menú principal con 8 opciones
2. Ingrese el número de la opción deseada (1-8)
3. Siga las instrucciones en pantalla para cada funcionalidad
4. Presione Enter cuando se solicite para volver al menú principal
5. Los cambios se guardan automáticamente en el archivo CSV

## Ejemplos de Entradas y Salidas

### Ejemplo 1: Agregar un País

**Entrada:**

```
Opción: 1
Nombre: Uruguay
Población: 3473727
Superficie: 176215
Continente (número): 2
```

**Salida:**

```
OK - País agregado correctamente!
Nombre: Uruguay
Población: 3,473,727
Superficie: 176,215 km²
Continente: América

OK - Cambios guardados en el archivo CSV
```

### Ejemplo 2: Buscar País

**Entrada:**

```
Opción: 3
Nombre a buscar: Arg
```

**Salida:**

```
País encontrado:
============================================================
Nombre: Argentina
Población: 45,376,763
Superficie: 2,780,400 km²
Continente: América
============================================================
```

### Ejemplo 3: Filtrar por Continente

**Entrada:**

```
Opción: 4
Tipo de filtro: 1
Número de continente: 2
```

**Salida:**

```
OK - Países en América (5):
==========================================================================================
N°   País                      Población       Superficie (km²) Continente
==========================================================================================
1    Argentina                 45,376,763      2,780,400        América
2    Brasil                    213,993,437     8,515,767        América
3    México                    126,014,024     1,964,375        América
4    Canadá                    38,155,012      9,984,670        América
5    Uruguay                   3,473,727       176,215          América
==========================================================================================
```

### Ejemplo 4: Mostrar Estadísticas

**Entrada:**

```
Opción: 6
```

**Salida:**

```
======================================================================
               ESTADÍSTICAS DE PAÍSES
======================================================================

[POBLACION]:
   • País con mayor población: China (1,412,600,000)
   • País con menor población: Uruguay (3,473,727)
   • Promedio de población: 170,458,621

[SUPERFICIE]:
   • Promedio de superficie: 4,235,678 km²

[PAISES POR CONTINENTE]:
   • África: 3 país(es)
   • América: 5 país(es)
   • Asia: 3 país(es)
   • Europa: 6 país(es)
   • Oceanía: 1 país(es)

[TOTALES]:
   • Total de países registrados: 18
   • Población mundial total: 3,068,255,118
   • Superficie mundial total: 76,242,204 km²
======================================================================
```

## Estructura del Proyecto

```
tpIntegradorProgramacion/
│
├── TpIntegradorGrupo132.py    # Archivo principal del programa
├── paises.csv                  # Base de datos en formato CSV
├── README.md                   # Documentación del proyecto
└── consigna.md                 # Consigna del trabajo práctico
```

## Estructura de Datos

### Diccionario de País

Cada país se representa como un diccionario con las siguientes claves:

```python
{
    "nombre": str,        # Nombre del país
    "poblacion": int,     # Población total
    "superficie": int,    # Superficie en km²
    "continente": str     # Continente al que pertenece
}
```

### Lista de Países

Los países se almacenan en una lista de diccionarios:

```python
paises = [
    {"nombre": "Argentina", "poblacion": 45376763, "superficie": 2780400, "continente": "América"},
    {"nombre": "Japón", "poblacion": 125800000, "superficie": 377975, "continente": "Asia"},
    # ... más países
]
```

## Validaciones Implementadas

1. **Campos vacíos**: No se permiten campos sin contenido
2. **Países duplicados**: Verifica que el país no exista antes de agregarlo
3. **Números positivos**: Población y superficie deben ser enteros positivos
4. **Rangos coherentes**: En filtros, el máximo debe ser mayor o igual al mínimo
5. **Opciones válidas**: Valida que las opciones del menú sean correctas
6. **Formato CSV**: Manejo de errores al leer el archivo
7. **Normalización**: Los textos se normalizan para evitar problemas de comparación

## Conceptos Aplicados

### Listas

- Almacenamiento de múltiples países
- Iteración con bucles `for`
- Métodos: `append()`, `len()`, `sorted()`

### Diccionarios

- Representación de cada país con clave-valor
- Acceso mediante claves: `pais["nombre"]`
- Recorrido con `for` e `items()`

### Funciones

- Modularización del código (una función = una responsabilidad)
- Parámetros y valores de retorno
- Funciones de validación, búsqueda, filtrado y ordenamiento

### Estructuras Condicionales

- `if`, `elif`, `else` para validaciones
- `match-case` para el menú principal
- Operadores de comparación y lógicos

### Estructuras Repetitivas

- `while` para menús y validaciones
- `for` para recorrer listas y diccionarios
- Control de flujo con `break` y `continue`

### Ordenamientos

- Función `sorted()` de Python
- Parámetro `key` utilizando funciones auxiliares (`clave_nombre`, `clave_poblacion`, `clave_superficie`)
- Ordenamiento ascendente y descendente con `reverse`

### Estadísticas Básicas

- Funciones `max()` y `min()` con key
- Cálculo de promedios con `sum()` y división
- Conteo de elementos con diccionarios

### Archivos CSV

- Módulo `csv` de Python
- `csv.DictReader()` para lectura
- `csv.DictWriter()` para escritura
- Manejo de archivos con `with open()`
- Codificación UTF-8 para caracteres especiales

## Tecnologías Utilizadas

- **Lenguaje**: Python 3.x
- **Módulos**:
  - `csv`: Manejo de archivos CSV
  - `os`: Verificación de existencia de archivos

## Referencias Bibliográficas

- Documentación oficial de Python: https://docs.python.org/3/

## Características Destacadas

- Interfaz de usuario clara y profesional
- Persistencia automática de datos en CSV
- Búsqueda inteligente con coincidencia parcial
- Estadísticas completas y detalladas
- Validaciones robustas en todas las entradas
- Código modular y bien comentado
- Cumple 100% con los requerimientos de la consigna
- Formato de números con separadores de miles
- Manejo de errores y excepciones

## Posibles Mejoras Futuras

- Implementar exportación de reportes en PDF
- Agregar gráficos estadísticos con matplotlib
- Crear interfaz gráfica con Tkinter
- Implementar base de datos SQLite
- Agregar más campos (capital, idioma, moneda, etc.)
- Sistema de usuarios con autenticación
- API REST para consultas remotas

## Licencia

Este proyecto fue desarrollado como Trabajo Práctico Integrador para la materia Programación 1 de la UTN-TUP.

---

**Grupo 132 - Programación 1 - UTN-TUP - 2025**
