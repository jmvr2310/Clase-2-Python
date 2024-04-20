
listas = [["pantalon", 901], ["camisa", 793], ["zapato", 123]]
#lista   [         0       ,         1      ,         2      ]
#sublistas[    0     ,  1 ], [   0    ,  1 ], [   0    ,  1 ]

print(listas[0])
print(listas[0][0])
print(listas[2][1])

sub1 = ["pantalon", 901, "caro"]
sub2 = ["camisa", 793, "fea"]
sub3 = ["zapato", 123, "barato"]
lista2 = [sub1, sub2, sub3]

print(lista2)
print(lista2[1][0:3:2]) # el numero luego del segundo : indica de cuanto en cuanto muestra los elementos,
                        # en este caso, como es cada 2 pasa del primero al tercero