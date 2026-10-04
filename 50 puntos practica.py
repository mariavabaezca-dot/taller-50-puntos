#punto1
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
estatura = float(input("Ingrese su estatura en metros: "))
estudia = input("¿Actualmente estudia? (si/no): ")
if estudia.lower() == "si":
    estudia = True
else:
    estudia = False
print("\n--- DATOS INGRESADOS ---")
print("Nombre:", nombre)
print("Tipo:", type(nombre))

print("Edad:", edad)
print("Tipo:", type(edad))

print("Estatura:", estatura)
print("Tipo:", type(estatura))

print("¿Estudia?:", estudia)
print("Tipo:", type(estudia))

#punto2
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
print("\n--- RESULTADOS ---")
print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)
if numero2 != 0:
    print("División:", numero1 / numero2)
else:
    print("No se puede dividir entre cero.")
print("Potencia:", numero1 ** numero2)
#punto3
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area = (base * altura) / 2
lado1 = float(input("Ingrese el primer lado: "))
lado2 = float(input("Ingrese el segundo lado: "))
lado3 = float(input("Ingrese el tercer lado: "))
perimetro = lado1 + lado2 + lado3
print("\n--- RESULTADOS ---")
print("Área del triángulo:", format(area, ".2f"))
print("Perímetro del triángulo:", format(perimetro, ".2f"))
#punto4
precio = float(input("Ingrese el precio unitario: "))
cantidad = int(input("Ingrese la cantidad comprada: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
subtotal = precio * cantidad
valor_descuento = subtotal * descuento / 100
subtotal_descuento = subtotal - valor_descuento
iva = subtotal_descuento * 0.19
total_final = subtotal_descuento + iva
print("\n--- RESULTADOS DE LA COMPRA ---")
print("Subtotal:", format(subtotal, ".2f"))
print("Valor del descuento:", format(valor_descuento, ".2f"))
print("Subtotal con descuento:", format(subtotal_descuento, ".2f"))
print("IVA (19%):", format(iva, ".2f"))
print("Total final:", format(total_final, ".2f"))
#punto 5
segundos_totales = int(input("Ingrese la cantidad total de segundos: "))
horas = segundos_totales // 3600
resto = segundos_totales % 3600
minutos = resto // 60
segundos = resto % 60
print("\n--- RESULTADO ---")
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
print("Tiempo:", horas, "hora(s),", minutos, "minuto(s) y", segundos, "segundo(s)")
#punto6
numero = int(input("Ingrese un número entero: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
if numero != 0:
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
#punto7
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 11:
    print("Es un niño")
elif edad >= 12 and edad <= 17:
    print("Es un adolescente")
elif edad >= 18 and edad <= 59:
    print("Es un adulto")
elif edad >= 60:
    print("Es un adulto mayor")
else:
    print("Edad no válida")
#punto 8
numero1=float(input("Ingrese el primer número: "))
numero2=float(input("Ingrese el segundo número: "))
numero3=float(input("Ingrese el tercer número: "))
mayor=max(numero1,numero2,numero3)
menor=min(numero1,numero2,numero3)
print("El número mayor es:",mayor)
print("El número menor es:",menor)
if numero1==numero2 or numero1==numero3 or numero2==numero3:
    print("Existen valores repetidos")
else:
    print("No existen valores repetidos")

#punto 9
nota=float(input("Ingrese una nota entre 0.0 y 5.0: "))
if nota<0 or nota>5:
    print("Nota no válida")
elif nota<3.0:
    print("Reprobado")
elif nota<4.0:
    print("Aprobado")
elif nota<4.5:
    print("Sobresaliente")
else:
    print("Excelente")

#punto 10
usuario_correcto="admin"
contrasena_correcta="1234"
codigo_minimo=100
codigo_maximo=999
usuario=input("Ingrese el usuario: ")
contrasena=input("Ingrese la contraseña: ")
codigo=int(input("Ingrese el código de verificación: "))
if usuario!=usuario_correcto:
    print("Rechazo: usuario incorrecto")
elif contrasena!=contrasena_correcta:
    print("Rechazo: contraseña incorrecta")
elif codigo<codigo_minimo or codigo>codigo_maximo:
    print("Rechazo: código fuera del rango válido")
else:
    print("Acceso permitido")

#punto 11
print("Números del 1 al 100:")
for numero in range(1,101):
    print(numero)
print("Múltiplos de 5:")
for numero in range(5,101,5):
    print(numero)

#punto 12
numero=int(input("Ingrese un número entero positivo: "))
if numero>0:
    for i in range(1,13):
        print(numero,"x",i,"=",numero*i)
else:
    print("El número debe ser positivo")

#punto 13
suma=0
mayor=None
menor=None
pares=0
for i in range(10):
    numero=float(input("Ingrese un número: "))
    suma=suma+numero
    if mayor is None or numero>mayor:
        mayor=numero
    if menor is None or numero<menor:
        menor=numero
    if numero%2==0:
        pares=pares+1
promedio=suma/10
print("Suma:",suma)
print("Promedio:",promedio)
print("Mayor:",mayor)
print("Menor:",menor)
print("Cantidad de pares:",pares)

#punto 14
contrasena_correcta="1234"
intentos=0
acceso=False
while intentos<3:
    contrasena=input("Ingrese la contraseña: ")
    if contrasena==contrasena_correcta:
        print("Acceso concedido")
        acceso=True
        break
    else:
        intentos=intentos+1
        print("Contraseña incorrecta")
if not acceso:
    print("Cuenta bloqueada")

#punto 15
cantidad=0
positivos=0
negativos=0
suma=0
while True:
    numero=int(input("Ingrese un número entero (0 para terminar): "))
    if numero==0:
        break
    cantidad=cantidad+1
    suma=suma+numero
    if numero>0:
        positivos=positivos+1
    else:
        negativos=negativos+1
print("Cantidad de números:",cantidad)
print("Positivos:",positivos)
print("Negativos:",negativos)
if cantidad>0:
    print("Promedio:",suma/cantidad)
else:
    print("No se ingresaron números diferentes de cero")

#punto16
def es_par(numero):
    return numero%2==0
for i in range(5):
    numero=int(input("Ingrese un número: "))
    if es_par(numero):
        print("Es par")
    else:
        print("Es impar")

#punto 17
def area_rectangulo(base,altura):
    return base*altura
def perimetro_rectangulo(base,altura):
    return 2*(base+altura)
base=float(input("Ingrese la base: "))
altura=float(input("Ingrese la altura: "))
print("Área:",area_rectangulo(base,altura))
print("Perímetro:",perimetro_rectangulo(base,altura))

#punto 18
def calcular_promedio(n1,n2,n3):
    return (n1+n2+n3)/3
def estado_academico(promedio):
    if promedio<3:
        return "Reprobado"
    elif promedio<4:
        return "Aprobado"
    elif promedio<4.5:
        return "Sobresaliente"
    else:
        return "Excelente"
nombre=input("Ingrese el nombre del estudiante: ")
n1=float(input("Ingrese la primera nota: "))
n2=float(input("Ingrese la segunda nota: "))
n3=float(input("Ingrese la tercera nota: "))
promedio=calcular_promedio(n1,n2,n3)
print("Estudiante:",nombre)
print("Promedio:",promedio)
print("Estado:",estado_academico(promedio))

#punto 19
def calcular_precio_final(precio,descuento):
    return precio-(precio*descuento/100)
precio=float(input("Ingrese el precio: "))
descuento=float(input("Ingrese el porcentaje de descuento: "))
if precio>=0 and 0<=descuento<=100:
    print("Precio final:",calcular_precio_final(precio,descuento))
else:
    print("Precio o descuento no válido")

#punto20
def sumar(a,b):
    return a+b
def restar(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
while True:
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion=input("Seleccione una opción: ")
    if opcion=="5":
        print("Programa finalizado")
        break
    if opcion in ["1","2","3","4"]:
        a=float(input("Ingrese el primer número: "))
        b=float(input("Ingrese el segundo número: "))
        if opcion=="1":
            print("Resultado:",sumar(a,b))
        elif opcion=="2":
            print("Resultado:",restar(a,b))
        elif opcion=="3":
            print("Resultado:",multiplicar(a,b))
        elif opcion=="4":
            if b!=0:
                print("Resultado:",dividir(a,b))
            else:
                print("No se puede dividir entre cero")
    else:
        print("Opción no válida")

#punto21
def mostrar_numeros(n):
    if n==1:
        print(1)
        return
    print(n)
    mostrar_numeros(n-1)
n=int(input("Ingrese un número positivo: "))
if n>0:
    mostrar_numeros(n)
else:
    print("El número debe ser positivo")

#punto 22
def suma_naturales(n):
    if n==1:
        return 1
    return n+suma_naturales(n-1)
n=int(input("Ingrese un número mayor o igual a 1: "))
if n>=1:
    print("La suma es:",suma_naturales(n))
else:
    print("El número debe ser mayor o igual a 1")

#punto 23
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
for numero in [0,1,5,6]:
    print("Factorial de",numero,"=",factorial(numero))

#punto 24
def invertir(cadena):
    if len(cadena)==0:
        return ""
    return invertir(cadena[1:])+cadena[0]
texto=input("Ingrese una cadena: ")
print("Cadena invertida:",invertir(texto))

#punto 25
def suma_digitos(numero):
    if numero<10:
        return numero
    return numero%10+suma_digitos(numero//10)
numero=int(input("Ingrese un número entero positivo: "))
if numero>=0:
    print("Suma de los dígitos:",suma_digitos(numero))
else:
    print("El número debe ser positivo")

#punto 26
ciudades=("Bogotá","Cali","Medellín","Cartagena","Barranquilla","Pereira","Manizales","Santa Marta")
print("Primera ciudad:",ciudades[0])
print("Última ciudad:",ciudades[-1])
print("Cantidad de ciudades:",len(ciudades))
print("Elementos en posiciones pares:")
for i in range(0,len(ciudades),2):
    print(ciudades[i])

#punto 27
notas=(4.5,3.8,2.9,5.0,3.5,4.2,2.5,4.8,3.0,4.0)
promedio=sum(notas)/len(notas)
aprobadas=0
for nota in notas:
    if nota>=3.0:
        aprobadas=aprobadas+1
print("Nota mayor:",max(notas))
print("Nota menor:",min(notas))
print("Promedio:",promedio)
print("Notas mayores o iguales a 3.0:",aprobadas)

#punto 28
producto=(101,"Cuaderno",5000,20)
codigo,nombre,precio,cantidad=producto
total=precio*cantidad
print("Código:",codigo)
print("Nombre:",nombre)
print("Precio:",precio)
print("Cantidad:",cantidad)
print("Valor total del inventario:",total)

#punto 29
estudiantes=(("Ana",4.5),("Juan",3.5),("Laura",4.2),("Carlos",2.9),("María",4.8))
for nombre,promedio in estudiantes:
    if promedio>=4.0:
        print(nombre,"- Promedio:",promedio)

#punto30
numeros=(2,5,3,5,8,5,10,3)
valor=int(input("Ingrese el valor a buscar: "))
print("Cantidad de veces:",numeros.count(valor))
if valor in numeros:
    print("Primera posición:",numeros.index(valor))
else:
    print("El valor no existe")
cantidad=0
primera_posicion=-1
for i in range(len(numeros)):
    if numeros[i]==valor:
        cantidad=cantidad+1
        if primera_posicion==-1:
            primera_posicion=i
print("Sin count ni index:")
print("Cantidad de veces:",cantidad)
if primera_posicion!=-1:
    print("Primera posición:",primera_posicion)
else:
    print("El valor no existe")

#punto 31
nombres=[]
for i in range(5):
    nombre=input("Ingrese un nombre: ")
    nombres.append(nombre)
print("Lista:",nombres)
print("Cantidad de elementos:",len(nombres))

#punto 32
numeros=[10,7,4,9,12,15,8,3,6,11]
pares=[]
for numero in numeros:
    if numero%2==0:
        pares.append(numero)
print("Suma:",sum(numeros))
print("Promedio:",sum(numeros)/len(numeros))
print("Mayor:",max(numeros))
print("Menor:",min(numeros))
print("Números pares:",pares)

#punto 33
productos=[]
for i in range(5):
    producto=input("Ingrese un producto: ")
    productos.append(producto)
print("Lista inicial:",productos)
buscar=input("Ingrese el producto que desea buscar: ")
if buscar in productos:
    print("Producto encontrado")
    posicion=productos.index(buscar)
    nuevo=input("Ingrese el nuevo nombre: ")
    productos[posicion]=nuevo
    print("Lista después de modificar:",productos)
else:
    print("Producto no encontrado")
eliminar=input("Ingrese el producto que desea eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
    print("Lista después de eliminar:",productos)
else:
    print("Producto no encontrado")

#punto 34
notas=[]
while True:
    nota=float(input("Ingrese una nota (-1 para terminar): "))
    if nota==-1:
        break
    notas.append(nota)
if len(notas)>0:
    notas.sort()
    cantidad=len(notas)
    promedio=sum(notas)/cantidad
    if cantidad%2==1:
        mediana=notas[cantidad//2]
    else:
        mediana=(notas[cantidad//2-1]+notas[cantidad//2])/2
    aprobados=0
    for nota in notas:
        if nota>=3:
            aprobados=aprobados+1
    print("Notas ordenadas:",notas)
    print("Promedio:",promedio)
    print("Mediana:",mediana)
    print("Cantidad de aprobados:",aprobados)
else:
    print("No se ingresaron notas")

#punto 35
productos=[["Cuaderno",5000,10],["Lapicero",2000,20],["Mochila",50000,5],["Carpeta",4000,15],["Regla",3000,8]]
total_inventario=0
mayor_inversion=0
producto_mayor=""
for producto in productos:
    nombre=producto[0]
    precio=producto[1]
    cantidad=producto[2]
    inversion=precio*cantidad
    total_inventario=total_inventario+inversion
    print(nombre,"- Valor:",inversion)
    if inversion>mayor_inversion:
        mayor_inversion=inversion
        producto_mayor=nombre
print("Valor total almacenado:",total_inventario)
print("Producto con mayor inversión:",producto_mayor)

#punto 36
colores_lista=["rojo","azul","verde","rojo","amarillo","azul","rosa"]
colores=set(colores_lista)
print("Lista original:",colores_lista)
print("Set resultante:",colores)
print("Los duplicados fueron eliminados porque los sets no permiten elementos repetidos.")

#punto 37
numeros=[]
for i in range(10):
    numero=int(input("Ingrese un número: "))
    numeros.append(numero)
numeros_diferentes=set(numeros)
print("Números ingresados:",numeros)
print("Cantidad de valores diferentes:",len(numeros_diferentes))

#punto 38
curso1={"Ana","Juan","Laura","Carlos","María"}
curso2={"Juan","Carlos","Pedro","Sofía","María"}
print("Estudiantes en ambos cursos:",curso1&curso2)
print("Solo en el primer curso:",curso1-curso2)
print("Solo en el segundo curso:",curso2-curso1)
print("Todos los estudiantes:",curso1|curso2)

#punto 39
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("Unión:",set1|set2)
print("Intersección:",set1&set2)
print("Diferencia de set1:",set1-set2)
print("Diferencia simétrica:",set1^set2)

#punto 40
dia1={"A01","A02","A03","A04","A05"}
dia2={"A03","A04","A05","A06","A07"}
recurrentes=dia1&dia2
nuevos=dia2-dia1
unico=dia1^dia2
print("Usuarios recurrentes:",recurrentes)
print("Usuarios nuevos del segundo día:",nuevos)
print("Usuarios que aparecieron en exactamente un día:",unico)

#punto 41
def calcular_promedio(n1,n2,n3):
    return (n1+n2+n3)/3
estudiantes=[]
cantidad=int(input("¿Cuántos estudiantes desea registrar?: "))
for i in range(cantidad):
    nombre=input("Ingrese el nombre: ")
    n1=float(input("Ingrese la primera nota: "))
    n2=float(input("Ingrese la segunda nota: "))
    n3=float(input("Ingrese la tercera nota: "))
    promedio=calcular_promedio(n1,n2,n3)
    if promedio<3:
        estado="Reprobado"
    elif promedio<4:
        estado="Aprobado"
    elif promedio<4.5:
        estado="Sobresaliente"
    else:
        estado="Excelente"
    estudiantes.append([nombre,promedio,estado])
for estudiante in estudiantes:
    print(estudiante)
promedio_general=sum(estudiante[1] for estudiante in estudiantes)/len(estudiantes)
mayor=max(estudiantes,key=lambda x:x[1])
print("Promedio general:",promedio_general)
print("Estudiante con mayor promedio:",mayor[0])

#punto 42
inventario=[]
def agregar_producto():
    codigo=input("Código: ")
    producto=input("Producto: ")
    precio=float(input("Precio: "))
    cantidad=int(input("Cantidad: "))
    inventario.append((codigo,producto,precio,cantidad))
def mostrar_inventario():
    for producto in inventario:
        print(producto)
def calcular_total():
    total=0
    for codigo,producto,precio,cantidad in inventario:
        total=total+precio*cantidad
    return total
while True:
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular valor total")
    print("4. Salir")
    opcion=input("Seleccione una opción: ")
    if opcion=="1":
        agregar_producto()
    elif opcion=="2":
        mostrar_inventario()
    elif opcion=="3":
        print("Valor total:",calcular_total())
    elif opcion=="4":
        break
    else:
        print("Opción no válida")

#punto 43
respuestas=[]
cantidad=int(input("¿Cuántas respuestas desea registrar?: "))
for i in range(cantidad):
    lenguaje=input("Ingrese su lenguaje favorito: ")
    respuestas.append(lenguaje)
lenguajes=set(respuestas)
print("Lenguajes diferentes:",lenguajes)
for lenguaje in lenguajes:
    print(lenguaje,":",respuestas.count(lenguaje),"votos")

#punto 44
def obtener_pares(numeros):
    return [n for n in numeros if n%2==0]
def obtener_impares(numeros):
    return [n for n in numeros if n%2!=0]
def obtener_positivos(numeros):
    return [n for n in numeros if n>0]
def obtener_negativos(numeros):
    return [n for n in numeros if n<0]
def obtener_promedio(numeros):
    return sum(numeros)/len(numeros)
numeros=[]
cantidad=int(input("¿Cuántos números desea ingresar?: "))
for i in range(cantidad):
    numeros.append(float(input("Ingrese un número: ")))
unicos=set(numeros)
resumen=(len(obtener_pares(numeros)),len(obtener_impares(numeros)),len(obtener_positivos(numeros)),len(obtener_negativos(numeros)),obtener_promedio(numeros))
print("Pares:",obtener_pares(numeros))
print("Impares:",obtener_impares(numeros))
print("Positivos:",obtener_positivos(numeros))
print("Negativos:",obtener_negativos(numeros))
print("Promedio:",obtener_promedio(numeros))
print("Valores únicos:",unicos)
print("Resumen:",resumen)

#punto 45
def suma_recursiva(lista):
    if len(lista)==0:
        return 0
    return lista[0]+suma_recursiva(lista[1:])
numeros=[]
cantidad=int(input("¿Cuántos números desea ingresar?: "))
for i in range(cantidad):
    numeros.append(float(input("Ingrese un número: ")))
resultado_recursivo=suma_recursiva(numeros)
resultado_ciclo=0
for numero in numeros:
    resultado_ciclo=resultado_ciclo+numero
print("Lista:",numeros)
print("Suma recursiva:",resultado_recursivo)
print("Suma con ciclo:",resultado_ciclo)

#punto46
def buscar_recursivo(tupla,valor,posicion=0):
    if posicion==len(tupla):
        return -1
    if tupla[posicion]==valor:
        return posicion
    return buscar_recursivo(tupla,valor,posicion+1)
numeros=(10,20,30,40,50,60)
valor=int(input("Ingrese el valor que desea buscar: "))
posicion=buscar_recursivo(numeros,valor)
if posicion==-1:
    print("El valor no existe")
else:
    print("El valor se encuentra en la posición:",posicion)

#punto 47
def calcular_descuento(total):
    if total>=500000:
        return total*0.10
    elif total>=200000:
        return total*0.05
    else:
        return 0
def calcular_iva(valor):
    return valor*0.19
ventas=[]
cantidad=int(input("¿Cuántos clientes desea procesar?: "))
for i in range(cantidad):
    cliente=input("Ingrese el nombre del cliente: ")
    compra=float(input("Ingrese el valor de la compra: "))
    descuento=calcular_descuento(compra)
    subtotal=compra-descuento
    iva=calcular_iva(subtotal)
    total=subtotal+iva
    ventas.append(total)
    print("Cliente:",cliente)
    print("Descuento:",descuento)
    print("IVA:",iva)
    print("Total a pagar:",total)
total_vendido=sum(ventas)
print("Total vendido:",total_vendido)
print("Compra promedio:",total_vendido/len(ventas))

#punto 48
def analizar_jornadas(jornada1,jornada2):
    repetidos=set(jornada1)&set(jornada2)
    unicos1=set(jornada1)-set(jornada2)
    unicos2=set(jornada2)-set(jornada1)
    diferentes=set(jornada1)|set(jornada2)
    print("Asistentes repetidos:",repetidos)
    print("Únicos de la primera jornada:",unicos1)
    print("Únicos de la segunda jornada:",unicos2)
    print("Total de personas diferentes:",len(diferentes))
jornada1=[]
jornada2=[]
cantidad1=int(input("¿Cuántos asistentes hubo en la primera jornada?: "))
for i in range(cantidad1):
    jornada1.append(input("Nombre del asistente: "))
cantidad2=int(input("¿Cuántos asistentes hubo en la segunda jornada?: "))
for i in range(cantidad2):
    jornada2.append(input("Nombre del asistente: "))
print("Primera jornada:",jornada1)
print("Segunda jornada:",jornada2)
analizar_jornadas(jornada1,jornada2)

#punto 49
biblioteca=[("001","Cien años de soledad","Gabriel García Márquez",False),("002","El principito","Antoine de Saint-Exupéry",False),("003","Don Quijote","Miguel de Cervantes",True)]
def listar_libros():
    for libro in biblioteca:
        estado="Prestado" if libro[3] else "Disponible"
        print(libro[0],"-",libro[1],"-",libro[2],"-",estado)
def buscar_codigo(codigo):
    for i in range(len(biblioteca)):
        if biblioteca[i][0]==codigo:
            return i
    return -1
def prestar(codigo):
    posicion=buscar_codigo(codigo)
    if posicion==-1:
        print("Libro no encontrado")
    elif biblioteca[posicion][3]:
        print("El libro ya está prestado")
    else:
        libro=biblioteca[posicion]
        biblioteca[posicion]=(libro[0],libro[1],libro[2],True)
        print("Libro prestado correctamente")
def devolver(codigo):
    posicion=buscar_codigo(codigo)
    if posicion==-1:
        print("Libro no encontrado")
    elif not biblioteca[posicion][3]:
        print("El libro ya estaba disponible")
    else:
        libro=biblioteca[posicion]
        biblioteca[posicion]=(libro[0],libro[1],libro[2],False)
        print("Libro devuelto correctamente")
while True:
    print("1. Listar libros")
    print("2. Buscar por código")
    print("3. Prestar")
    print("4. Devolver")
    print("5. Salir")
    opcion=input("Seleccione una opción: ")
    if opcion=="1":
        listar_libros()
    elif opcion=="2":
        codigo=input("Ingrese el código: ")
        posicion=buscar_codigo(codigo)
        if posicion==-1:
            print("Libro no encontrado")
        else:
            print(biblioteca[posicion])
    elif opcion=="3":
        prestar(input("Ingrese el código: "))
    elif opcion=="4":
        devolver(input("Ingrese el código: "))
    elif opcion=="5":
        break
    else:
        print("Opción no válida")

#punto50
def suma_notas_recursiva(notas):
    if len(notas)==0:
        return 0
    return notas[0]+suma_notas_recursiva(notas[1:])
def calcular_promedio(notas):
    return suma_notas_recursiva(notas)/len(notas)
def clasificar(promedio):
    if promedio<3:
        return "Reprobado"
    elif promedio<4:
        return "Aprobado"
    elif promedio<4.5:
        return "Sobresaliente"
    else:
        return "Excelente.."
estudiantes=[]
cantidad=int(input("¿Cuántos estudiantes desea registrar?: "))
todas_las_notas=[]
for i in range(cantidad):
    nombre=input("Nombre del estudiante: ")
    notas=(float(input("Nota 1: ")),float(input("Nota 2: ")),float(input("Nota 3: ")))
    estudiantes.append((nombre,notas))
    todas_las_notas.extend(notas)
for nombre,notas in estudiantes:
    promedio=calcular_promedio(notas)
    print("Estudiante:",nombre)
    print("Notas:",notas)
    print("Promedio:",promedio)
    print("Estado:",clasificar(promedio))
notas_diferentes=set(todas_las_notas)
promedio_grupo=sum(todas_las_notas)/len(todas_las_notas)
print("Promedio general del grupo:",promedio_grupo)
print("Notas diferentes registradas:",notas_diferentes)    
       