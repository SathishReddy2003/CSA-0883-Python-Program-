array_of_elements = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3
sorted_array = sorted(array_of_elements)
Mth_max = sorted_array[-M]
Nth_min = sorted_array[N-1]
sum_value = Mth_max + Nth_min
difference_value = Mth_max - Nth_min
product_value = Mth_max * Nth_min
print(f"{M}th Maximum Number = {Mth_max}")
print(f"{N}th Minimum Number = {Nth_min}")
print(f"Sum = {sum_value}")
print(f"Difference = {difference_value}")
print(f"Product = {product_value}")
