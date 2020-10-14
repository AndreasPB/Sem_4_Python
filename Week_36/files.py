f = open('text.txt', 'r')
print(f.read())

s = open('flotfil.txt')
print(f.readline())

s = open('flotfil.txt', 'a')
s.write('Hallo??')