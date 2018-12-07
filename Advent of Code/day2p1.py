day2input = '''abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab'''


input_list = day2input.splitlines()
def counter(code_list):
    for each_item in code_list:
        for each_letter in each_item:
            #if the count of letters in each item is a value do something
            while each_item.count(each_letter) == 2 is False:




