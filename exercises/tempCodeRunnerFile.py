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

resultado = variable_03 or not variable_01 or not variable_02 or not variable_04 or not variable_05
    
# COMPLETAR - FIN

assert resultado == 80