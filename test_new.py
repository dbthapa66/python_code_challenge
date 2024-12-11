import math
def reverse_word(word):
    reversed = ""
    for letter in word:
            reversed = letter + reversed
    return reversed

print(reverse_word("Nepal India China"))
"""

def check_all_palindromes(arr):
    if arr[0] == reverse_word(arr[0]):
        if arr[1] == reverse_word(arr[1]):
            if arr[2] == reverse_word(arr[2]):
                return True
    return False
"""

def is_palindrome(word):
        return word == reverse_word(word)

def check_all_palindromes(arr):
        for word in arr:
                if is_palindrome(word) == False:
                        return False
        return True

print(check_all_palindromes(['racecar', 'noon', 'civic']))

def isPrime(n):
    for i in range(math.floor(math.sqrt(n))+1):
        if i == 0 or i == 1:
            continue
        if n % i == 0:
            return False
    return True

for i in range(101):
      print(str(i) + " is Prime: ", isPrime(i))


n=1234512
frequency_map = {}
while n > 0:
    digit = n % 10
    #print(digit)
    if digit not in frequency_map:
        frequency_map[digit] = 1
    else:
        frequency_map[digit] += 1
    n = n // 10
    #print(n)

print(frequency_map)
        
def create_staircase(nums):
  step = 1
  subsets = []
  while len(nums) != 0:
    if len(nums) >= step:
      subsets.append(nums[0:step])
      nums = nums[step:]
      step += 1
    else:
      return False
      
  return subsets

print(create_staircase([1, 2, 3, 4, 5, 6]))