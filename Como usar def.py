#hacer un programa con funciones 
#Saludar a una persona 
#contar vocales de una palabra
#verificar si un numero es par o impar
#sumar dos numeros
#calcular el area de un circulo 

def presentacion():
   nom = "Carlos"
   ape = "Alquinga"
   edad = 23
   mov = "Estoy estudiando programacion por que quiero crear y diseñar aplicaciones."
   #Se imprime la presentacion 
   print(f"Hola, mi nombre es: {nom} {ape}\nTengo: {edad} años.\n{mov}")
   return nom
def par_impar():
    limite = int(input("Ingrese el tamaño del bucle: "))
    tipo = input("Ingrese si quiere PARES o IMPARES: ")
    #Inicar la suma en 0
    suma=0
    #Crear el bucle
    for i in range(1,limite+1):
       if tipo == "pares" and i%2==0:
         suma += i
         print(f"{i} + {suma-i} = {suma}")
       elif tipo == "impares" and i%2!=0:
         suma += i
         print(f"{i} + {suma-i} = {suma}")
    
    print(f"La suma total de los numeros: ´{tipo}´ hasta {limite} es {suma}")
def contador_vocales():
   palabra = input("Ingrese la palabra: ")
   vocales = "aeiouAEIOU"
   contador = 0
   for letra in palabra:
     if letra in vocales:
         contador += 1
   print(f"El numero de vocales es {contador}")
def minutos_horas():
   minutos = int(input("Ingrese los minutos para transformarlos: "))
   horas = minutos //  60
   rest = minutos % 60
   print(f"los {minutos} dan como resultado: {horas} Horas y {rest} Minutos.")
def grados_fahrenheit():
   far = int(input("Ingrese los grados Fahrenheit que desea transformar a Celsius: "))
   celsius = (far - 32)* 5/9
   print(f"{far} grados Fahrenheit son {celsius: .2f} grados Celsius")
print("")
presentacion()
print("")
par_impar()
print("")
contador_vocales()
print("")
minutos_horas()
print("")
grados_fahrenheit()

