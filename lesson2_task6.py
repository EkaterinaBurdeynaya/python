goods = []
dict_1 = {}

i = 1
for i in range(3):
    value_name = input('Please enter name: ')
    value_price = input('Please enter price: ')
    value_quantity = input('Please enter quantity: ')
    value_unit= input('Please enter unit: ')
    dict_1 = {'name' : value_name, 'price' : value_price, 'quantity' : value_quantity, 'unit' : value_unit}
    goods.append((i, dict_1))

print(goods)

analytic = {}
name_list =[]
price_list = []
quantity_list = []
unit_list = []

i = 0
for i in range(3):
    name_list.append(goods[i][1].get('name'))
    price_list.append(goods[i][1].get('price'))
    quantity_list.append(goods[i][1].get('quantity'))
    unit_list.append(goods[i][1].get('unit'))
    analytic = {'name' : name_list, 'price' : price_list, 'quantity' : quantity_list, 'unit' : unit_list}

print(analytic)
