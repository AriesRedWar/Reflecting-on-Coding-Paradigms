fruits_list = []

def add_fruit(food):
    if(food['type'] == 'fruit'):
        fruits_list.append(food)

add_fruit({ 'name': 'strawberry', 'type': 'fruit'})
add_fruit({'name': 'pizza', 'type': 'hot'})
add_fruit({ 'name': 'orange', 'type': 'fruit'})
print(fruits_list)