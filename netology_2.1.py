from pprint import pprint
import os

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                            shop_list_item['measure']))

def create_shop_list():
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ').split(', ')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)

filename = 'recipes.txt'
DATA_PATH = (os.path.abspath(filename))

cook_book = dict()
with open(DATA_PATH, "r") as f:
	while True:
		dish = f.readline().strip()
		if not dish:
			break

		count_ingredients = int(f.readline().strip())
		ingredients_list = list()
		while count_ingredients != 0:
			ingredients_dict = dict()
			ingredient = f.readline().strip().split(" | ")
			ingredients_dict["ingridient_name"] = ingredient[0]
			ingredients_dict["quantity"] = int(ingredient[1])
			ingredients_dict["measure"] = ingredient[2]
			ingredients_list.append(ingredients_dict)
			count_ingredients -= 1
			print(count_ingredients)
		cook_book[dish] = ingredients_list
		empty_line = f.readline().strip()

pprint(cook_book)


create_shop_list()


