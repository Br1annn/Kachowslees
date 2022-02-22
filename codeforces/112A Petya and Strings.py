#112A Petya and STrings
import string
#compare 2 strings to see if they are equal or not, case does not matter


first_string = input().lower()
second_string = input().lower()


if first_string == second_string:
    print('0')

if first_string < second_string:
    print('-1')

if first_string > second_string:
    print('1')
