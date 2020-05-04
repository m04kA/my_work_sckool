f_obj = open("num_1.txt", "w")
my_notes = []
words = input()
while words != '':
    my_notes.append(words + '\n')
    words = input()
f_obj.writelines(my_notes)
f_obj.close()
