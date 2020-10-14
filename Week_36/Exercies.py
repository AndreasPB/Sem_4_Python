
# Sort the list based on the last letter in the name.
def lastLetterSort(s):

    return s[-1]

names = ['Niels','Peterax','Børge','Flemmiaangb','Sofusc','Erika']
print(names)

sorted_names = sorted(names, key=lastLetterSort)
print(sorted_names)


# Sort the list with the names where the letter ‘a’ is in the name first.

def letterASort(s):

    for i in s:
        if i == 'a':
            return False
        
    return True
        


names_with_a = sorted(names, key=letterASort)
print(names_with_a)