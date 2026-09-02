# Calculadora 1.1

## Descripción

Esta es la versión 1.1 de mi calculadora desarrollada en Python.

En esta versión se mejoró la validación de entradas y el manejo de errores, haciendo que el programa sea más resistente ante entradas incorrectas del usuario.

## Nuevas funciones e integraciones

### 1. Validación de operaciones

La calculadora ahora verifica que la operación seleccionada corresponda a una opción válida.

Las operaciones disponibles están dentro del rango:

```text
1 - 4
```

Si el usuario introduce un número fuera de este rango, el programa muestra un mensaje de error y vuelve a solicitar la opción.

### 2. Validación del tipo de entrada

También se agregó una validación para evitar que el programa termine inesperadamente cuando el usuario introduce letras o símbolos.

Se utiliza `try/except` para manejar los errores producidos al intentar convertir la entrada a un número entero.

Ejemplo:

```text
Escriba la operación deseada (1-4): hola

Error: debe ingresar un número, no letras ni símbolos.
```

### 3. Manejo de errores

Las entradas incorrectas ya no provocan que el programa termine inmediatamente.

El programa informa al usuario del problema y permite volver a intentar la operación.

## Tecnologías utilizadas

- Python
- `input()`
- Condicionales `if / else`
- Ciclos `while`
- Manejo de excepciones `try / except`
- Funciones
- Git
- GitHub

## Objetivo del proyecto

El objetivo de este proyecto es practicar los fundamentos de programación en Python y mejorar progresivamente la estructura y robustez del programa mediante nuevas versiones.

## Historial de versiones

### Calculator 1.1
- Se agregó validación de operaciones.
- Se agregó validación del tipo de entrada.
- Se incorporó manejo de `ValueError`.
- Se mejoró el comportamiento ante entradas inválidas.
- El programa vuelve a solicitar la información en lugar de finalizar inesperadamente.

### Calculator 1.0
- Primera versión funcional de la calculadora.
- Implementación de las operaciones básicas.
- Uso de funciones para realizar los cálculos.