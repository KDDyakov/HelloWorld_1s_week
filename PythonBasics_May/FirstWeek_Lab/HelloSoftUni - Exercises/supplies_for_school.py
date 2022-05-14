pack_of_pencils = 5.8
pack_of_markers = 7.2
whiteboard_cleaner = 1.2

number_of_packs_pencils = float(input())
number_of_packs_markers = float(input())
whiteboard_cleaner_number = float(input())
discount_rate = float(input())

pencils_price = number_of_packs_pencils * pack_of_pencils
markers_price = number_of_packs_markers * pack_of_markers
cleaner_price = whiteboard_cleaner * whiteboard_cleaner_number

sum_total_no_discount = pencils_price + markers_price + cleaner_price
sum_total_with_discount = sum_total_no_discount - (sum_total_no_discount * (discount_rate/100))

print(sum_total_with_discount)