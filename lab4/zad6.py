# zadanie 6
# https://pl.wikipedia.org/wiki/Symbol_Newtona
def newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return newton(n - 1, k - 1) + newton(n - 1, k)


print("wartosc newtona: ", newton(25, 20))

# zadanie 7
num_set = {1, 2, 3, 4, 5}
word_set = {'lol', 'xd'}

print(7 in num_set)  # czy znajduje sie w zbiorze
print('xd' not in word_set)  # czy nie znajduje sie w zbiorze

print("======================")

nums = {1, 2, 3, 4, 5, 1, 2, 3}
print(nums)

# dodawanie
nums.add(-1)
print(nums)

# remove usuwa okreslony element
nums.remove(3)
print(nums)

# pop usuwa dowolny element zbioru (chyba pierwszy)
nums.pop()
print(nums)

print("======================")

num1 = {1, 2, 3, 5, 6}
num2 = {1, 3, 4, 5, 6}
print("zbior num1: ", num1)
print("zbior num2: ", num2)

print("suma zbiorow num1 i num2", num1 | num2)
print("czesc wspolna zbiorow num1 i num2", num1 & num2)
print("roznica zbiorow num1 i num2", num1 - num2)
print("roznica zbiorow num2 i num1", num2 - num1)
print("roznica symetryczna zbiorow num1 i num2", num1 ^ num2)


words = {'a', 'b', 'c'}
print(words)