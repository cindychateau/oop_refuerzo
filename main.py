from Persona import Persona #Importamos la clase Persona

from Estudiante import Estudiante #Importando la clase Estudiante

elena = Persona("Elena", "De Troya", 15, "elena@codingdojo.com") #Instancia de Persona

juana = Persona("Juana", "De Arco", 20, "juana@codingdojo.com")

#print(elena)
#print(juana)

elena.imprimir()
juana.imprimir()

elena.cumpleaños()

elena.imprimir()

elena.correo = "ele@codingdojo.com"

elena.imprimir()

#1er día del Bootcamp
elena.codificar(10)
juana.codificar(15)

#2do día del Bootcamp
juana.codificar(20)

juana.imprimir()

Persona.imprime_lineas_codigo()

pablo = Estudiante("Pablo", "Picasso", 50, "pablo@codingdojo.com", 1234, "Python Intensivo")

pablo.imprimir()

pablo.estudiar()

pablo.cumpleaños()

pablo.curso_estudiante.agrega_calificacion(10)

pablo.curso_estudiante.agrega_calificacion(9)

pablo.curso_estudiante.agrega_calificacion(10)

print(pablo.curso_estudiante.nombre_curso)
print(pablo.curso_estudiante.calificaciones)

#juana.estudiar() -> ERROR
