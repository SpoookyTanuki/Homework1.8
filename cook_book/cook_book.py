from pprint import pprint

with open('recipes.txt') as f:
    all_recipes_dict = dict()
    line = " "

    while line != "":
        line = f.readline().replace("\n", "")
        name = line
        line = f.readline().replace("\n", "")
        ingr_count = int(line)
        ingr_list = list()

        for i in range(0, ingr_count):
            line = f.readline().replace("\n", "")
            all_ingr = line.split(' | ')
            parts_ingr = list()

            for j in all_ingr:
                parts_ingr.append(j.replace("\n", ""))
            ingr_dict = dict()
            ingr_dict.update({'ingredient_name': parts_ingr[0]})
            ingr_dict.update({'quantity': parts_ingr[1]})
            ingr_dict.update({'measure': parts_ingr[2]})
            ingr_list.append(ingr_dict)

        all_recipes_dict.update({name: ingr_list})
        line = f.readline()

pprint("cook_book = " + str(all_recipes_dict))



print()



def get_shop_list_by_dishes(dishes, person_count = 2):
    ingr_dict = dict()

    for dish in dishes:
        parts_ingr = all_recipes_dict[dish]

        for i in parts_ingr:
            quan_meas = dict()
            quan_meas.update({'measure': i['measure']})
            quan_meas.update({'quantity': (int(i['quantity']) * person_count)})
            ingr_dict.update({i['ingredient_name']: quan_meas})

    pprint(ingr_dict)
                
get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3)
