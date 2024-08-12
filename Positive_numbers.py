def print_positive_number(n):
  pos_num = [num for num in n if num > 0]
  return pos_num

list1 = [1, 5, -7, 8, -2]
print("The positive numbers are: ",print_positive_number(list1))
