def create_dict(file_name: str) -> dict:
    recipes_dict = dict()
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            dish_name = line.strip()
            number_of_ingredients = int(file.readline())
            list_of_ingredients = []
            for ingredient in range(number_of_ingredients):
                ingredient_name, quantity, measure = file.readline().strip().split('|')
                list_of_ingredients.append({"ingredient_name": ingredient_name, "quantity": quantity, "measure": measure})
            recipes_dict[dish_name] = list_of_ingredients
            file.readline()
    return recipes_dict
recipes_book = create_dict("recipes.txt")
print(recipes_book)

def get_shop_list_by_dishes(dishes, person_count):
    dict_of_ingredients = {}
    for dish in dishes:
        for ingredient in recipes_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = int(ingredient['quantity']) * person_count
            if ingredient_name in dict_of_ingredients.keys():
                quantity = dict_of_ingredients[ingredient_name]['quantity'] + quantity
            dict_of_ingredients.update({ingredient_name: {'measure': measure, 'quantity': quantity}})
    return dict_of_ingredients

list_of_dishes = ['Фахитос', 'Омлет']
result = get_shop_list_by_dishes(list_of_dishes, 3)
print(result)