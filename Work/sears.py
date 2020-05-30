bill_thickness = (0.11 * 0.001)
sears_height = 442
bill_count = 1
day_count = 1

while bill_count * bill_thickness < sears_height:
    print(day_count, bill_count, bill_count * bill_thickness)
    day_count += 1
    bill_count *= 2

print("Number of days", day_count)
print("Number of bills", bill_count)
print("Final stack height of bills", bill_count * bill_thickness)
