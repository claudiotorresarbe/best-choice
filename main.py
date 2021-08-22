#library
from bestchoice import Generate

#data
#object,price,importance level
table = [['pants',75,10],
         ['jeans',50,7],
         ['shirt',45,8],
         ['dress',65,7],
         ['ball',25,5]]

#column for calculation
#in this case, the price and importance level
columns = [1,2]

#index of column importance
importance = 2

#filters where 1 is the price <= 10 dollars
filters = [[1,'<=',150]]

#call function generate
gen = Generate(table)

#get all possibilities
lista = gen.list_all()

#new table after filter
#the first parameter 1 and 2 are columns for calculation
#the second parameter 1 <= price filter your new table 
res = gen.list_best(columns,filters)

#saves the best filtered result
top = max([sublist[-1] for sublist in res])

filters.append([importance,'==',top])
#table with new result
new = gen.list_best(columns,filters)

#set index of top values
best = [x[0] for x in new][0]

#result
print(f'This is your best choice: {", ".join([str(x[0]) for x in lista[best]])}')
