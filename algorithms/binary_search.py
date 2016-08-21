def binary_search(list, item):
  low  = 0
  high = len(list) - 1
  index = 0

  while low <= high:
    mid   = (low + high) / 2
    guess = list[mid]

    index += 1

    if guess == item:
      print index
      return mid

    if guess > item:
      high = mid - 1
    else:
      low  = mid + 1

  return None

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

print binary_search(my_list, 1)
#print binary_search(my_list, 2)
