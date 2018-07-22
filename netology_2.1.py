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

def make_ingredients_dict(ingredient):
	ingredients_dict = dict()
	ingredients_dict["ingridient_name"] = ingredient[0]
	ingredients_dict["quantity"] = int(ingredient[1])
	ingredients_dict["measure"] = ingredient[2]
	return ingredients_dict

def make_cook_book(data_path):
	cook_book = dict()
	with open(data_path, "r") as f:
		while True:
			dish = f.readline().strip()
			if not dish:
				break

			count_ingredients = int(f.readline().strip())
			ingredients_list = list()
			for i in range(count_ingredients):
				ingredient = f.readline().strip().split(" | ")
				ingredients_dict = make_ingredients_dict(ingredient)
				ingredients_list.append(ingredients_dict)

			cook_book[dish] = ingredients_list
			empty_line = f.readline().strip()
	return cook_book

local_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(local_path, 'recipes.txt')

cook_book = make_cook_book(data_path)
pprint(cook_book)

create_shop_list()
