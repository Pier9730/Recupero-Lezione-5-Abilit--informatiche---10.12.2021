par=int(input('Numero di valori:'))

my_list=[None]*par


lim=2**32
for i in range(par):
    
    my_list[i]=float(input('Valore i:'))

for i in range(par):
    if my_list[i] < lim:
        lim=my_list[i]

print(lim)
    
    





    
    
