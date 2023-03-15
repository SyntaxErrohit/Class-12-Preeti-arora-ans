def capitalize_sentance():
    f1 = open("test_report.txt", "r")
    f2 = open("temp.txt", "w")
    f1_lines = f1.readlines()
    for line in f1_lines:
        words = line.lstrip().split('.')
        temp = []
        for i in words:
            if i != '':
                temp.append(i.capitalize())
            else:
                temp.append('')
        f2.write('.'.join(temp))
    f1.close()
    f2.close()


capitalize_sentance()