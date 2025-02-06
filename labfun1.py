"""def convertgrams(grams):
    return 28.3495231*grams
print(convertgrams(100))

def  convertfar(farenheit):
    return (5/9)*(farenheit-32)
print(convertfar(100))

def solve(numheads,numlegs):
    for chickens in range(numheads+1):
        rabbits=numheads-chickens
        if(2*chickens+4*rabbits)==numlegs:
            return chickens,rabbits
print(solve(35,94))

def reverse_strings(sentence):
    return ' '.join(sentence.split()[::-1])
print(reverse_strings("We are ready"))

def has_33(nums):
    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3:  
            return True  
    return False  

print(has_33([1, 3, 3]))  
print(has_33([1, 3, 1, 3]))  
print(has_33([3, 1, 3])) 

def spy_game(nums):
    n = 0  
    for num in nums:
        if num == 0 and n == 0:  
            n = 1
        elif num == 0 and n == 1:  
            n = 2
        elif num == 7 and n == 2:  
            return True  
    return False  

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

def sphere_volume(r):
    return (4 / 3) * 3.14 * (r ** 3)  

print(sphere_volume(2))

def unique_list(lst):
    new_list = []  
    for item in lst:
        if item not in new_list:  
            new_list.append(item)  
    return new_list  

print(unique_list([1, 2, 2, 3, 4, 4, 5])) 

def is_palindrome(s):
    s = s.lower()  
    return s ==s[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("civic")

def histogram(numbers):
    for num in numbers:
        print('*' * num)

histogram([4, 9, 7])"""

import random
print("Hello! What is your name?")
name = "KBTU"
print(name)
secret_num= random.randint(1, 20)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
guesses=0

while True:
    print("Take a guess.")
    guess = int(input())
    guesses+=1
    if guess < secret_num:
        print("Your guess is too low.")
    elif guess > secret_num:
        print("Your guess is too high.")
    else:
        print(f"Good job, {name}! You guessed my number in {guesses} guesses")
        break





