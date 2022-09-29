class Persona:

    total_lineas_codigo = 0

    #A traves de INIT inicializamos nuestra instancia. ¿Qué es una instancia? Un objeto ya creado
    def __init__(self, nombre, apellido, edad, correo): #self es toda la información de mi instancia. SELF es mi instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.lineas_codigo = 0
    
    def imprimir(self): #self = elena
        print(f'Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Email: {self.correo}, Lineas de Código: {self.lineas_codigo}')
    
    def cumpleaños(self): #self = elena
        self.edad += 1 #elena.edad +=1 -> elena.edad = 31
        if(Persona.mayoria_edad(self.edad)):#31 - True
            print("Felicidades, eres mayor de edad")
        
     
    def codificar(self, cantidad_lineas): 
        #self = elena, cantidad_lineas = 10
        self.lineas_codigo += cantidad_lineas
        Persona.total_lineas_codigo += cantidad_lineas

    @classmethod
    def imprime_lineas_codigo(cls):
        print(f'Total de líneas de código codificadas por todos: {cls.total_lineas_codigo}')

    @staticmethod
    def mayoria_edad(edad): #edad = 31
        if edad > 18:
            return True
        else:
            return False

    #Polimorfismo significa el tener diferentes funcionalidades a través de las clases heredadas. Diferente comportamiento
    def que_haces(self):
        raise NotImplementedError
    