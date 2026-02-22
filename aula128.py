#Sets - Conjuntos em  Python (Tipo Set)
#Conjuntos são ensinados na matemática 
#
#Representados graficamente pelo diagrama de venn 
#Sets em Python são mutáveis, mas aceitam apenas valores
#imutáveis como valor interno

#Criando um set 
#set(iterável) ou {1,2,3}



# s1 = set('Luiz')
# print(s1)
# s1 = {'Luiz', 1,2,3}
# print(s1,type(s1))


#Sets são eficientes para remover valores duplicados de iteráveis
#- Eles não tem index
#- Eles não garantem ordem
#- Eles são iteráveis (for, in, not in)


# s1 = {1,2,3,3,3,1}
# print(s1)

l1 = [1,2,3,3,3,1]
print(f'Lista L1: {l1}')
s1 = set(l1)
print(f'Conversão de Lista pra set: {s1}')
l2 = list(s1)
print(f'L2: {s1}')

print('Em laço de reptição: ')
for numero in s1:
    print(numero)
#Métodos úteis 
#add, update, clear 