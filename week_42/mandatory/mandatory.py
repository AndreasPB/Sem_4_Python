# Opgave 1
# Beklager at det er blevet så overkompliceret! 
# Hindsight -> Jeg kunne vidst bare have brugt set difference
class Person:
    def __init__(self, name, boardOfDirector, management, employee):
        self.name = name
        self.boardOfDirector = boardOfDirector
        self.management = management
        self.employee = employee

    def __str__(self):
        return str(self.name)

Benny = Person("Benny", True, False, False)
Hans = Person("Hans", True, False, False)
Tine = Person("Tine", True, True, True)
Mille = Person("Mille", True, False, False)
Torben = Person("Torben", True, False, False)
Troels = Person("Troels", True, False, False)
Soeren = Person("Søren", True, False, False)
Trunte = Person("Trunte", False, True, True)
Rane = Person("Rane", False, True, True)
Niels = Person("Niels", False, False, True)
Allan = Person("Allan", False, False, True)
Anna = Person("Anna", False, False, True)
Ole = Person("Ole", False, False, True)
Stine = Person("Stine", False, False, True)
Claus = Person("Claus", False, False, True)
James = Person("James", False, False, True)
Lars = Person("Lars", False, False, True)

# En liste med dem alle
organisation = [Benny, Hans, Tine, Mille, Torben, Troels, Soeren, Trunte, Rane, Niels, Anna, Ole, Stine, Claus, James, Lars]

# Alle spørgsmålene - Held og lykke med at læse det :DD
# who in the board of directors is not an employee?
directorButNotEmployee = []
for o in organisation:
    if o.boardOfDirector == True and o.employee == False:
        directorButNotEmployee.append(o)
        
print("who in the board of directors is not an employee?")
for d in directorButNotEmployee:
    print(d.name, end = ", ")
print("")

# who in the board of directors is also an employee?
directorAlsoEmployee = []
for o in organisation:
    if o.boardOfDirector == True and o.employee == True:
        directorAlsoEmployee.append(o)

print("who in the board of directors is also an employee?")
for d in directorAlsoEmployee:
    print(d.name, end = ", ")
directorAlsoEmployee
print("")

# how many of the management is also member of the board?
managementAlsoBoard = []
for o in organisation:
    if o.management == True and o.boardOfDirector:
        managementAlsoBoard.append(o)

print("how many of the management is also member of the board?")
count = 0
for m in managementAlsoBoard:
    #print(m.name, end = ", ")
    count = count +1
print(count)

# All members of the managent also an employee
managementAlsoEmployee = []
for o in organisation:
    if o.management == True and o.employee == True:
        managementAlsoEmployee.append(o)

print("All members of the managent also an employee")
for m in managementAlsoEmployee:
    print(m.name, end = ", ")
print("")

# All members of the management also in the board?
print("All members of the management also in the board?")
for m in managementAlsoBoard:
    print(m.name, end = ", ")
print("")

# Who is an employee, member of the management, and a member of the board?
employeeAlsoManagementAlsoBoard = []
for o in organisation:
    if o.employee == True and o.management == True and o.boardOfDirector == True:
        employeeAlsoManagementAlsoBoard.append(o)

print("Who is an employee, member of the management, and a member of the board?")
for e in employeeAlsoManagementAlsoBoard:
    print(e.name, end = ", ")
print("")

# Who of the employee is neither a memeber or the board or management?
employeeNotBoardNotManagement = []
for o in organisation:
    if o.employee == True and o.boardOfDirector == False and o.management == False:
        employeeNotBoardNotManagement.append(o)

print("Who of the employee is neither a memeber or the board or management?")
for e in employeeNotBoardNotManagement:
    print(e.name, end = ", ")
print("")


# Opgave 2
listOfTuples = [(key, value) for key, value in {'a' : 'Alpha', 'b' : 'Beta', 'g' : 'Gamma'}.items()]
print(listOfTuples)

# Opgave 3
x = {'a', 'e', 'i', 'o', 'u', 'y'}
y = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

print("Union")
z = x.union(y)
print(z)

print("Difference")
z = y.difference(x)
print(z)

print("Symmetric Difference")
z = x.symmetric_difference(y)
print(z)

print("Disjoint")
z = x.isdisjoint(y)
print(z)

# Opgave 4
def date_decoder(str):
    date = str.split("-")
    
    day = date[0]
    month = months[date[1]]
    year = int(date[2])

    if year >= 0 and year <= 20:
        year += 2000
    else:
        year += 1900

    return year, month, day

months = {
    'JAN': 1,
    'FEB': 2,
    'MAR': 3,
    'APR': 4,
    'MAY': 5,
    'JUN': 6,
    'JUL': 7,
    'AUG': 8,
    'SEP': 9,
    'OCT': 10,
    'NOV': 11,
    'DEC': 12
}

date = "8-MAR-85"
decodedDate = date_decoder(date)
print(decodedDate)

date = "23-NOV-11"
decodedDate = date_decoder(date)
print(decodedDate)