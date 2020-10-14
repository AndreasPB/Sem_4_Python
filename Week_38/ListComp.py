list = [i for i in range(1,7)]

print(list)

alphabet = [chr(i) for i in range(65,91)]
alphabetTwo = [chr(i) for i in range(65,91) if not i in (70, 75, 80, 85)]

alphabetThree = [chr(i) for i in range(65,91) if not i in range (70,80,2)]

print(alphabet)
print(alphabetTwo)

print(alphabetThree)




