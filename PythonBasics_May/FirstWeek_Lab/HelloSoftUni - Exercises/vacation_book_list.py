pages_number_current = float(input())
pages_per_hour = float(input())
number_of_days = float(input())

total_book_time = int(pages_number_current / pages_per_hour)
hours_per_day = total_book_time / number_of_days
print(int(hours_per_day))