"""
This loads all of the locations and generates their objects
"""


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def look(self):
        return self.description


f = open("locations.txt", 'r', newline='')
for line in f:
    txt = line.split('|')
    name = txt[0]
    descr = txt[1]
    Location(name, descr)
    #create location object here

f.close()


print(field.description)

