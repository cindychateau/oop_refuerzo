from Persona import Persona
from Curso import Curso

#Declaramos que la clase superior es Persona
class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, correo, matricula, nombre_curso): #nombre_curso = "Python Intensivo"
        super().__init__(nombre, apellido, edad, correo)

        self.matricula = matricula
        self.curso_estudiante = Curso(nombre_curso) #Guardo en el atributo curso_estudiante de Estudiante una instancia de Curso
    
    def estudiar(self):
        print("Hoy estamos estudiando mucho Python")

    #Sobreescritura / Anulación
    def imprimir(self):
        print(f'Nombre: {self.nombre}, Email: {self.correo}, Líneas de Código: {self.lineas_codigo}, Matrícula: {self.matricula}')

    #Sobrescritura + Uso de la función superior
    def cumpleaños(self):
        super().cumpleaños()
        print("A seguir estudiando ;)")
    
    def que_haces(self):
        print("Estoy estudiando y aprendiendo")