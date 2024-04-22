numbers = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

def filter_odd_num(in_num):
    if(in_num % 3 == 0 and in_num < 30):
        return True
    else:
        return False

out_filter = filter(filter_odd_num, numbers)

print("Отфильтрованный список: ", list(out_filter))
