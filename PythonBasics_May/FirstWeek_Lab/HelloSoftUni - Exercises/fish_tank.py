length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
total_litres = volume / 1000
percent_lit = total_litres * (percent / 100)
result = total_litres - percent_lit

print(result)