day2input = '''abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab'''


input_list = day2input.splitlines()

def counting(code_list):
    two_counter = 0
    three_counter = 0
    for each_item in code_list:
        c = [each_item.count(i) for i in each_item]
        if 2 in c:
            two_counter += 1
        elif 3 in c:
            three_counter +=1
    print (two_counter, three_counter)

counting(input_list)



