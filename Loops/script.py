#=== CODE CHALLENGE 1 ===
#Write your function here
def divisible_by_ten(nums):
  count = 0
  for x in nums:
    if x % 10 == 0:
      count += 1
  return count

#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# === CODE CHALLENGE 2 ===
#Write your function here
def add_greetings(names):
  new_list = ["Hello, " + name for name in names]
  return new_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#=== CODE CHALLENGE 3 ===
# Deleting starting numbers
#Write your function here
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst

#Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# === CODE CHALLENGE 4 ===
# Odd indices 
def odd_indices(lst):
  new_list = []
  for index in range(1, len(lst), 2):
    new_list.append(lst[index])
  return new_list
#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

#=== CODE CHALLENGE 5 ===
# Exponents
#Write your function here
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#=== CODE CHALLENGE 6 ===
#Larger sum
#Write your function here
def larger_sum(lst1,lst2):
  sum1 = 0
  sum2 = 0
  for list1 in lst1:
    sum1 += list1
  for list2 in lst2:
    sum2 += list2
  print(sum1)
  print(sum2)
  if sum1 > sum2 or sum1 == sum2:
    return lst1
  else:
    return lst2
  
#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))

#=== CODE CHALLENGE 7 ===
#Over 9000
#Write your function here
def over_nine_thousand(lst):
  add = 0
  if len(lst) == 0:
    return 0
  for x in lst:
      add += x
      if add > 9000:
        break
  return add

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

#=== CODE CHALLENGE 8 ===
#max num
#Write your function here
def max_num(nums):
  nums.sort()
  return nums[-1]

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# === CODE CHALLENGE 9 ===
#Same values
#Write your function here
def same_values(lst1,lst2):
  equal_val = []
  length = len(lst1)
  for i in range(0, length):
    if lst1[i] == lst2[i]:
      equal_val.append(i)
  return equal_val

#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

# === CODE CHALLENGE 10 ===
# reversed list
#Write your function here
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
