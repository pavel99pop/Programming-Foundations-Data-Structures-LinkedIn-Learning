# Linear Search

my_list = [1, 6, 9, 7, 5, 6, 1, 3, 6, 5, 4 ,8 ,10, 65, 1]

def search(value):
  for item in my_list:
    if item == value:
      return True
  return False

print(search(7))
try:
  print(my_list.index(11))
except:
  print('Value not in list')