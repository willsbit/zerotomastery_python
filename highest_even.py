def highest_even(li):
    for item in li:
        even_nums = []
        if item % 2 == 0:
            even_nums.append(item)
    return max(even_nums)


li = [10, 2, 3, 4, 5, 6, 3, 2, 5, 25, 100]

print(highest_even(li))
