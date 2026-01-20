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


# Clonar el repositorio
```bash
git clone https://github.com/CesarSosa19/numerical-methods-python
```

# Entrar a la carpeta del proyecto
```bash
cd numerical-methods-python
```

# Ejecutar el programa: Asegúrate de estar en la carpeta raíz y ejecuta:
```bash
python src/main.py
```
