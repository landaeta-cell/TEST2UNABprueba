#print("cantidad de productis a  item")
n=int(input("ingrese item: "))
i=0
while i<n:
 i+=1 
 codigo = int(input("codigo: "))
 nombre = str(input("nombre: "))
 cantidad = float(input("cantidad: "))
 precioCompra = float(input("precio: "))
 totalparcial = float(precioCompra*cantidad)
#IVA = 0.19*totalparcial
 IVA=int(input("tipo de iva; 1 exento de iva, 2 iva 5%, 3 iva 19%: "))
 
 if IVA==1:
   tarifa=totalparcial*0.0
 elif IVA==2:
  tarifa=totalparcial*0.05
 else:
  tarifa=totalparcial*0.19
 print(n) 
 print(codigo)
 print(nombre)
 print(totalparcial)
 print(tarifa+totalparcial)