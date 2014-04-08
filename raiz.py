a=input('Digite o coeficiente a:')
b=input('Digite o coeficiente b:')
c=input('Digite o coeficiente c:')
delta = b**2 - 4*a*c
print 'Valor de delta:',(delta)
if (delta < 0):
  print ('Sem raizes reais')
else:
  raiz1= (-1*b - delta**0.5)/(2.0*a)
  print (raiz1)
  raiz2= (-1*b + delta**0.5)/(2.0*a)
  print (raiz2)

