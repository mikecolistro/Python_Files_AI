text_file = open("catfacts.txt","r")
lines = text_file.readlines()
x = len(lines)
y = 0
for y in range(0, x):
    print lines[y]
    y += 1
text_file.close()
