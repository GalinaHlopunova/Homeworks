first_strings = ['Elon', 'Misk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git','Comprehension', 'Java', 'Computer', 'Assembler']
first_result = [len(str1) for str1 in first_strings if len(str1) >= 5]
second_result = [(str1, str2) for str1 in first_strings for str2 in second_strings if len(str1) == len(str2)]
first_second_strings = first_strings + second_strings
third_result = dict((str3, len(str3)) for str3 in first_second_strings if len(str3) %2 ==0)
print (first_result)
print (second_result)
print (third_result)
