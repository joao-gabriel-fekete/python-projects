#This script searches for a name in a table and prints the rows associated to the name.
## In case a composed name is given, it searches iterations removing the last name given each time. 
###In the current state, it lowers the letters and remove diacritics from the name given.

import pandas as pd
import re
import unidecode

sample = pd.read_csv("sample.csv")

def student(name):
  """searches for the name given"""
    global sample

    finish = False
    name = name.lower() #lowers all the letters
    name = unidecode.unidecode(name) #removes diacritics
    name = " ".join(name.split()) #turns multiple spaces into single spaces

    while finish == False:

        match = sample[sample['Name'].str.contains(name) == True]

        if match.empty == True:
            print('No match for: {}'.format(name)) #Message displayed if it does not match a pattern

            if len(re.findall(r'(\w+.)\s', name)) > 0:
                array = re.findall(r'(\w+.)\s', name) #Removes the last given name and searches again.
                name = ' '.join(array)
            else:
                print('No more possible searches') #Message in case no more names can be removed.
                finish = True

        else:
            print('Match found for: {}'.format(name))
            print(match)
            finish = True


attempt = student('alan nascimento')
