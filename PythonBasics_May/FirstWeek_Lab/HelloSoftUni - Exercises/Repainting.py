needed_nylon = float(input())
needed_paint = float(input())
needed_paint_remover = float(input())
hour_rate = float(input())

total_nylon = (needed_nylon + 2) * 1.5
total_paint = (needed_paint * 1.10) * 14.5
total_paint_remover = needed_paint_remover * 5

sum_materials = total_nylon + total_paint + total_paint_remover + 0.4
sum_workers = (sum_materials * 0.3) * hour_rate

total_sum = sum_materials + sum_workers

print(total_sum)

