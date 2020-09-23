shopping_list = {'Piekarnia' :  ['Chleb', 'Pączek', 'Bułki'], \
'Warzywniak' :  ['Marchew', 'Seler', 'Rukola']}
for  sklep in shopping_list:
    print(f'Idę do  {sklep} kupic następujące rzeczy {shopping_list[sklep]}')
print(f'W sumie kupuje {sum(len(shopping_list[sklep]) for products in shopping_list.values()} produktow')
 
