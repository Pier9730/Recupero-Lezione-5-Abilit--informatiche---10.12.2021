a=7.283
b=5
c=9756.123
d=1000
z=4+7j
z1=7.3+9j
string='Paperino'

#somma
sum_int=int(a+b)
sum_float=float(a+b)
sum_str=string+string+str(sum_float)

print(sum_int, sum_float, sum_str)
print()

#prodotto
prod_int=int(a*b)
prod_float=float(a*b)
prod_str='Papara'+'z'*2+'i'

print(prod_int, prod_float, prod_str)
print()

#sottrazione
sott_int=int(a-b)
sott_float=float(a-b)
sott_comp=z-a

print(sott_int, sott_float, sott_comp)
print()

#divisione
div_float=a/b
div_comp=z/z1
div_floatcomp=z/a

print(div_float, div_comp, div_floatcomp)
print()

#divisione intera
print(a//b, c//b, d//a) 
print()

#modulo
print(a%b, c%d, c%b)


