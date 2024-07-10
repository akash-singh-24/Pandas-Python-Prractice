# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /___|")
#
# name2 = "Akash"
# print("My Name is " + name2 + ". I Love Coding")
#
# name1 = "Shatakshi Loves Akash"
# print("My Name is " + name2 + ". I Love " + name1)
#
# print(name1.upper().isupper())
#
# print(len(name1))
#
# print(name1[2:5])
#
# print(name1.index(" "))
#
# print(name1.replace("Loves","Hates"))
#
# print(name1*2)
#
# from math import *
#
# print(floor(6.987))
#
# print(ceil(6.007))
#
# print(pow(5,3))
#
# # name3 = input("Enter you Name : ")
# # print("Hello " + name3)
#
# my_lists = ["Akash","Shatakshi","End of List"]
# print(my_lists)
# print(my_lists[0])
# print(my_lists[1])
# print(my_lists[-1])
# my_lists[0] = "Havoc"
# print(my_lists)
#
# my_lists.append("Sudeshna")
# print(my_lists)
# my_lists.insert(1,"Shatakshi Boyfriend")
# print(my_lists)
# my_lists.remove("Sudeshna")
# print(my_lists)
# my_lists.pop()
# print(my_lists)
# my_lists.sort()
# print(my_lists)
# my_lists.reverse()
# print(my_lists)
# my_lists2 = my_lists.copy()
# print(my_lists)
#
# def facts():
#     print("Functions")
#
# facts()
#
# fact1 = int(1)
# def facts_print(num):
#     print(num)
#     global fact1
#     fact1 *= num
#     num = num - 1
#     if num > 0:
#         facts_print(num)
#
# n1 = int(5)
# facts_print(n1)
# print(fact1)
#
# def factorial_return(asd):
#     if asd == 0 or asd < 0 :
#         return 1
#     else :
#         return asd * factorial_return(asd - 1)
#
# asd_result = factorial_return(-1)
# print(asd_result)
#
# i = 0
# j = 1
# # loop1 = int(input("Enter a Number : "))
# loop1 = 5
# while i <= loop1 - 1:
#     j = 0
#     while j <= i:
#         print(loop1 - i,end = ' ')
#         j += 1
#     print()
#     i += 1
#
# i = 1
# j = 1
#
# while i <= loop1:
#     j = 1
#     while j <= i:
#         print(j,end = ' ')
#         j += 1
#     print()
#     i += 1
#
# i = 1
# j = 1
#
# while i <= loop1:
#     j = 1
#     while j <= i:
#         print(i,end = ' ')
#         j += 1
#     print()
#     i += 1
#
# i = 0
# j = 1
#
# while i <= loop1 - 1:
#     j = 0
#     while j <= i:
#         print(loop1 - j,end = ' ')
#         j += 1
#     print()
#     i += 1
#
#
# for i in "Akash Loves Shatakshi":
#     print(i,end = ' ')
#
# print()
#
# for listy in my_lists:
#     print(listy)
#     for i in listy:
#         print(i,end = ' ')
#         print()
#
# i = 1
# j = 1
# loop1 = int(input("Enter a value for Diamond of Stars : "))
# while i <= loop1:
#     j = 1
#     print('  '*(loop1 - i),end=(' '))
#     while j <= i:
#         print('*',end = ' ')
#         j += 1
#     j = 1
#     while j <= i - 1:
#         print('*',end = ' ')
#         j += 1
#     j = 1
#     print()
#     i += 1
#
# i = 1
# j = 1
# # loop1 = 5
# while i <= loop1 - 1:
#     j = 0
#     print('  ' * (i), end = ' ')
#     while j <= loop1 - i - 1 :
#         print('*',end = ' ')
#         j += 1
#     j = 0
#     while j <= loop1 - 2 - i:
#         print('*',end = ' ')
#         j += 1
#     print()
#     i += 1
#
# i = 1
# j = 1
# loop1 = int(input("Enter a value for Diamond of Stars : "))
# while i <= loop1:
#     j = 1
#     print('  '*(loop1 - i), end=' ')
#     while j <= i:
#         print(j, end=' ')
#         j += 1
#     j = i - 1
#     while j >= 1:
#         print(j, end=' ')
#         j -= 1
#     print()
#     i += 1
#
# i = 1
# while i <= loop1 - 1:
#     j = 1
#     print('  ' * i, end=' ')
#     while j <= loop1 - i:
#         print(j, end=' ')
#         j += 1
#     j = loop1 - i - 1
#     while j >= 1:
#         print(j, end=' ')
#         j -= 1
#     print()
#     i += 1
#
# string_value = 'Beware of Dogs'
# new_string_value = ''
# new_string_value1 = ''
# for chars in string_value:
#     if chars == ' ':
#         new_string_value1 = new_string_value1 + ' * '
#         continue
#     else :
#         new_string_value = new_string_value + chars
#         new_string_value1 = new_string_value1 + chars
# print(new_string_value)
# print(new_string_value1)
#
# str_value = 'Beware off Dogs'
# for i in range(len(str_value)-1):
#     if str_value[i] == str_value[i+1]:
#         print(str_value[i]+str_value[i+1])

# str1 = "akash"
# for i in range(len(str1) - 1):
#     for j in range(i+1,len(str1) - 1):
#         print(j, end='')
#     print()

def count_characters(s):
    char_count = {}
    for i in s:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count


# Example usage:
input_string = 'aaaabbbcdddefghiii  '
result = count_characters(input_string)
for char, count in result.items():
    print(f"{char}: {count}")
