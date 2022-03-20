
x=0
#ESAMPIO 1:
for i in range(10):
    x=x+i
    values='Per l\'indice %d ottengo il valore di x: %d' %(i, x)   #print in integer
    values='Per l\'indice %d ottengo il valore hex di x: %02X' %(i, x)   #conversione in esadecimale
    values='Per l\'indice %d ottengo il valore float di x: %07.2f' %(i, x)  #conversione in floating point
    
    print(values)
    
print()
misura='La parete misura %5.2f metri, quindi compra %4.1f di cavo!' %(15.90, 15.99)   #conversione in floating point 
print(misura)
print()
x=(17.0/13.0)*10000

print('x=', x, 'Risultato in esponenziale = %e' %(x)) #conversione in notazione scientifica
print()



my_list=['Gennaio', 'Febbraio', 'Marzo']

for i in range(3):
    
    print(my_list[i].center(20,'!'), my_list[i].upper()) #print degli elementi in lista centrati e maiuscoli


for i in range(32, 96):     #print del carattere ASCII corrispondente al valore indicato nel range
    print('%c' %(i), end='')
    if (i % 16) == 0:
      print('')
    




