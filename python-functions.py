
# def sum_to(num):
#   sum = 0
#   for n in range(1, num + 1):
#     sum += n
#   return sum

# print(sum_to(6))

# def largest(nums):
#   largest_num = 0 
#   for num in nums:
#     if num > largest_num:
#       largest_num = num
#   return largest_num

# print(largest([1, 2, 3, 4]))

# def occurences(string, occ):
#   return string.count(occ)

# print(occurences('hello', 'o'))

def product(*args):
  total = 1
  for num in args:
    total *= num
  return total

print(product(1, 2, 3))