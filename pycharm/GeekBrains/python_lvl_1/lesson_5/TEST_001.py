def write(first, second):
    with open("file.dat", "r") as f_obj:
        words = f_obj.readlines()
        for idx in range(len(words)):
            words[idx] = words[idx].replace(first, second)
    with open("file.dat", "w") as f_obj:
        f_obj.writelines(words)


write('AAA', '5')
