"""Lógica Simple y Cortocircuito"""


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si al menos una de las variables es True.
"""

<<<<<<< HEAD

esta_lloviendo = True
riego_activado = True

# COMPLETAR - INICIO
piso_mojado = esta_lloviendo or riego_activado
=======
esta_lloviendo = False
riego_activado = True

# COMPLETAR - INICIO

piso_mojado = esta_lloviendo or riego_activado

>>>>>>> 65a035c50067dcdefbe25f2291db59c4b0c2e01f
# COMPLETAR - FIN

assert piso_mojado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el área es mayor a 5.
Restricción: Usar NOT.
"""

lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)
area_mayor_a_cinco = True

# COMPLETAR - INICIO
<<<<<<< HEAD
=======
if not area_cuadrado >= 5:
    area_mayor_a_cinco = False
    
>>>>>>> 65a035c50067dcdefbe25f2291db59c4b0c2e01f
# COMPLETAR - FIN

assert area_mayor_a_cinco


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50
resultado = True

# COMPLETAR - INICIO
if numero_1 % 7 == 0 and numero_2 % 7 != 0:
    resultado = True
else:
    resultado = False

# COMPLETAR - FIN

assert resultado


"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100

# COMPLETAR - INICIO
<<<<<<< HEAD
resultado = variable_03
=======

resultado = variable_03 or not variable_01 or not variable_02 or not variable_04 or not variable_05
    
>>>>>>> 65a035c50067dcdefbe25f2291db59c4b0c2e01f
# COMPLETAR - FIN

assert resultado == 80