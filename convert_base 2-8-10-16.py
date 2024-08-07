# Script written by Scott Baird using ideas and sample code from geeksforgeeks.org and toppr.com.

# This script will convert a base 2, 8, 10, 16 (binary, octal, decimal, and hexadecimal) integer number to its counterparts.
# It does not use any built in functions for conversion.  All defined functions are iterative or recursive.

# The only check is to ensure that the user is selecting one of the 4 number systems.
# This means it does not check that the number entered is valid to that number system.
# For example, choosing Octal and entering 999 will result in incorrect output because 999 is not a valid octal number.
# Other incorrect inputs may return a KeyError.

# An additional limitation is that this script does not work with fractional or floating point numbers.

# Process for the script is to 1) ask for the number system, 2) ask for the number to be converted, 3) accept as decimal or convert to decimal, 4) then convert from decimal to the other 3 number systems and put the result.
# For example, Octal is selected.  The entered number is first convert to decimal, the decimal is used to convert to hex and binary, then the decimal, hex, and binary values are outputed.


hex_table = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
def decToHex(decimal):
    hex_temp = ''
    while decimal != 0:
        remainder = decimal % 16
        hex_temp = hex_table[remainder] + hex_temp
        decimal = decimal // 16
    return hex_temp

dec_to_oct_table = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7'}
def decToOct(decimal):
    octal_temp = ''
    while decimal != 0:
        remainder = decimal % 8
        octal_temp = dec_to_oct_table[remainder] + octal_temp
        decimal = decimal // 8
    return octal_temp

def decToBin(decimal):
    bin_temp = ''
    while decimal !=0:
        remainder = decimal % 2
        bin_temp = str(remainder) + bin_temp
        decimal = decimal // 2
    return bin_temp

# establish the dec to hex equivalents
hex_to_dec_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10 , 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
def hexToDec(decimal):
    num_temp = conv_num.upper()
    decimal = 0
    # get the length of the hex number and subtract 1
    length = len(num_temp)-1
    for digit in num_temp: # for loop will continue for each digit in hex
        decimal += hex_to_dec_table[digit]*16**length # using the specific dictionary, multiply the number by 16 to its positional power
        length -= 1 # subtract one from the length
    return decimal

def octToDec(num_temp):
    base = 1
    decimal = 0
    while num_temp:
        last_digit = num_temp % 10
        num_temp = int(num_temp / 10)
        decimal += last_digit * base
        base = base * 8
    return decimal

def binToDec(num_temp):
    base = 1
    decimal = 0
    while num_temp:
        last_digit = num_temp % 10
        num_temp = int(num_temp / 10)
        decimal += last_digit * base
        base = base * 2
    return decimal

select_base = ''
while select_base != "q":
  number_sys = {1:"Decimal", 2:"Octal", 3:"Hex", 4:"Binary", "q":"Quit"}
  print(number_sys)

  select_base = input("Select a number.\n")
    
  if select_base == 'q':
    print("Qutting")
    break
  elif select_base >= "5":
    print("Invalid choice. Select 1 - 4.")
    print('\n')
    continue
  else:
    conv_num = input("Enter number to be converted.\n")

    if select_base == "1": # decimal
      conv_num = int(conv_num)
      print("As octal:", decToOct(conv_num))
      print("As hex:", decToHex(conv_num))
      print("As binary:", decToBin(conv_num))
      print('\n')
      continue
    elif select_base == "2": # octal
      conv_num = int(conv_num)
      deci = octToDec(conv_num)
      print("As hex:", decToHex(deci))
      print("As decimal:", deci)
      print("As binary:", decToBin(deci))
      print('\n')
      continue
    elif select_base == "3": # hex
      deci = hexToDec(conv_num)
      print("As decimal:", deci)
      print("As octal:", decToOct(deci))
      print("As binary:", decToBin(deci))
      print('\n')
      continue
    else: # binary
      conv_num = int(conv_num)
      deci = binToDec(conv_num)
      print("As hex:", decToHex(deci))
      print("As octal:", decToOct(deci))
      print("As decimal:", deci)
      print('\n')
      continue
 
