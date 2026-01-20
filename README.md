# numerical-methods-python

## Descripción
Este proyecto es una herramienta de consola interactiva diseñada para encontrar raíces de ecuaciones no lineales de forma automatizada. Resolver ecuaciones complejas (como `x - cos(x) = 0`) analíticamente es difícil o imposible; este software resuelve ese problema implementando algoritmos iterativos clásicos.

El programa permite al usuario ingresar cualquier función matemática en tiempo real y calcular sus raíces con alta precisión, sin necesidad de calcular derivadas manualmente.

**Características principales:**
* Evaluación dinámica de funciones matemáticas (input de usuario).
* Cálculo automático de derivadas (Diferencias Finitas).
* Selección de tolerancia y número de iteraciones.

## Tecnologías
* **Lenguaje:** Python 3.x
* **Control de Versiones:** Git & GitHub
* **Librerías Estándar:** `math` (para funciones trigonométricas, exponenciales, etc.)
* **Paradigmas:** Programación Modular y Funcional (uso de Lambdas).

## Estructura
El proyecto sigue una arquitectura modular para separar la lógica de negocio (matemática) de la interfaz de usuario.

```text
├── src/
│   ├── main.py              # Punto de entrada: Menú CLI y validación de inputs
│   └── methods/             # Paquete con la lógica numérica
│       ├── __init__.py
│       ├── bisection.py     # Implementación del algoritmo de Bisección
│       └── newton.py        # Implementación de Newton-Raphson con derivada numérica
├── .gitignore               # Archivos excluidos del repositorio
└── README.md                # Documentación del proyecto
```

## Ejecución

Sigue estos pasos para descargar y probar el proyecto en tu entorno local:

### 1. Prerrequisitos
Asegúrate de tener instalado:
* [Python 3.8+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

### 2. Instalación
Abre tu terminal y clona este repositorio:


#### 2.1 Clonar el repositorio
```bash
git clone https://github.com/CesarSosa19/numerical-methods-python
```

#### 2.2 Entrar a la carpeta del proyecto
```bash
cd numerical-methods-python
```

### 3. Ejecutar el programa: Asegúrate de estar en la carpeta raíz y ejecuta:
```bash
python src/main.py
```
Nota para Windows: Si el comando python no funciona, prueba escribiendo py main.py

## Guía de Uso

El programa es interactivo y funciona desde la consola. Para asegurar que tus cálculos sean correctos, es importante seguir la sintaxis de Python al escribir las ecuaciones.

### 1. Reglas de Sintaxis
* **Variable:** Utiliza siempre la letra **`x`** (minúscula).
* **Potencias:** Usa el operador **`**`** (doble asterisco). El símbolo `^` **no** funciona para potencias en Python.
* **Funciones Matemáticas:** Antepón el prefijo `math.` para usar funciones trigonométricas, logaritmos o exponenciales.

### 2. Ejemplos de Escritura

| Ecuación Matemática | **Cómo escribirla en el programa** |
| :--- | :--- |
| $x^2 - 4$ | `x**2 - 4` |
| $e^x - 1$ | `math.exp(x) - 1` |
| $\sin(x) - x$ | `math.sin(x) - x` |
| $\sqrt{x} - 5$ | `math.sqrt(x) - 5` |
| $\ln(x) + 2$ | `math.log(x) + 2` |

### 3. Pasos para usar el programa

1.  **Iniciar:** Ejecuta el archivo `main.py`.
2.  **Definir la función:** Escribe tu ecuación cuando veas `f(x) = `.
    * *Ejemplo:* `math.cos(x) - x**3`
3.  **Seleccionar el Método:**
    * Escribe `1` para **Bisección** (requiere un intervalo `[a, b]`).
    * Escribe `2` para **Newton-Raphson** (requiere un punto inicial `x0`).
4.  **Parámetros:** Ingresa los valores solicitados (intervalos o punto inicial) y la tolerancia deseada (ej. `0.0001`).
5.  **Resultado:** El programa mostrará la raíz aproximada o un mensaje de error si no converge.
