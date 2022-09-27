from Persona import Persona #Importamos la clase Persona

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