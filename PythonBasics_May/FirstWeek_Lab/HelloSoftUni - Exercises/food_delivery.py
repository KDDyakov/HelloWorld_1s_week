chicken_menus = float(input())
fish_menus = float(input())
veg_menus = float(input())

total_chicken = chicken_menus * 10.35
total_fish = fish_menus * 12.4
total_veg = veg_menus * 8.15
sum_menus = total_chicken + total_fish + total_veg

price_of_dessert = sum_menus * 0.2
delivery_price = 2.5
sum_total_order = sum_menus + price_of_dessert + delivery_price
print(sum_total_order)