"""
# problem 1

apple_three = int(input())
apple_two = int(input())
apple_one = int(input())

banana_three = int(input())
banana_two = int(input())
banana_one = int(input())

apple_total = apple_three * 3 + apple_two * 2 + apple_one
banana_total = banana_three * 3 + banana_two * 2 + banana_one

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')      


## Problem 2 


meals_dict = {
    "Burger" : {
        1 : ["Cheeseburger", 461],
        2 : ["Fish Burger", 431],
        3 : ["Veggie Burger", 420],
        4 : ["No Burger", 0],
    },
    "Drink" : {
        1 : ["Soft Drink", 130],
        2 : ["Orange Juice", 160],
        3 : ["Milk", 118],
        4 : ["No Drink", 0],
    },
    "Side" : {
        1 : ["Fries", 100],
        2 : ["Baked Potato", 57],
        3 : ["Chef Salad", 70],
        4 : ["No Side Order", 0],
    },
    "Dessert" : {
        1 : ["Apple Pie", 167],
        2 : ["Sundae", 266],
        3 : ["Fruit Cup", 75],
        4 : ["No Dessert", 0],
    },
}
burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

total_cals = meals_dict['Burger'][burger_choice][1] + meals_dict['Drink'][drink_choice][1] + meals_dict['Side'][side_choice][1] + meals_dict['Dessert'][dessert_choice][1]
print(f'Your total Calorie count is {total_cals}.')


# Special Day

month = int(input())
day = int(input())

if month > 2:
    print('After')
elif month == 2 and day > 18:
    print('After')
elif month == 2 and day == 18:
    print('Special')
else:
    print('Before')

# Happy or Sad
text = input()
sum = text.count(':-)') + text.count(':-(') 

if sum == 0:
    print('none')
elif text.count(':-)') > text.count(':-('):
    print("happy")
elif text.count(':-)') < text.count(':-('): 
    print('sad') 
else: 
    print('unsure') 
    
## Cheese-kun
W = int(input())
C = int(input())

if W == 3 and C >= 95:
    print(f'C.C. is absolutely satisfied with her pizza.')
elif W == 1 and C <= 50:
    print(f'C.C. is fairly satisfied with her pizza.')
else:
    print(f'C.C. is very satisfied with her pizza.')        
    

# Who is in the Middle?  
bowl_wt = [0, 0, 0]
bowl_wt[0] = int(input())
bowl_wt[1] = int(input())
bowl_wt[2] = int(input())

bowl_wt.sort()
print(bowl_wt[1])    

    
"""
