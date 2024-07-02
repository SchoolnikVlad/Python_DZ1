numbers = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

out_filter = filter(lambda x: x % 3 == 0 and x < 30, numbers)

print("Отфильтрованный список: ", list(out_filter))