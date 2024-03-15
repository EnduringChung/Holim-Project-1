import random
original_string = input("Please give me a sentence you like:")
desired_length = int(input("Please let me know how long do you want your password to be:"))
new_password = ""
dictionary = {1:'a',
              2:'b',
              3:'c',
              4:'d',
              5:'e',
              6:'f',
              7:'g',
              8:'h',
              9:'i',
              10:'j',
              11:'k',
              12:'l',
              13:'m',
              14:'n',
              15:'o',
              16:'p',
              17:'q',
              18:'r',
              19:'s',
              20:'t',
              21:'u',
              22:'v',
              23:'w',
              24:'x',
              25:'y',
              36:'z'
              }

#Check length

if desired_length > len(original_string):
    partial_string = ""
    for i in range(desired_length+ 1 - len(original_string)):
        index = random.randint(1,26)
        partial_string += dictionary.get(index) 
        original_string += partial_string

elif desired_length < len(original_string):
    for i in range(len(original_string) - desired_length):
        original_string = original_string[:-1]
        
#character to number

for char in original_string:
    if char == 'I' or char == "l":
        new_password += "1"
    elif char == "O":
        new_password += "0"
    elif char == "S":
        new_password += "5"
    else:
        new_password += char

#char_to_num(original_string, )
print(original_string)
print(new_password)