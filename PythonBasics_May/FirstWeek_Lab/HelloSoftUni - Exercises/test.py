chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())
chick_price = 10.35
fish_price = 12.40
veggie_price = 8.15
delivery = 2.50
total_chicken = chicken_menu * chick_price
print(total_chicken)
total_fish = fish_menu * fish_price
print(total_fish)
total_veggie = veggie_menu * veggie_price
print(total_veggie)
food_price = total_chicken + total_fish + total_veggie
desert = 0.2 * food_price
total_sum = delivery + desert + food_price
print(total_sum)

