class PsvItems(object):

    def __init__(self, Id, name, employerId,employeeIdentityId):
        self.__Id = Id
        self.__name = name
        self.__employerId = employerId
        self.__employeeIdentityId=employeeIdentityId
        self.__index = -1

    @property
    def id(self):
        return self.__Id

    @property
    def name(self):
        return self.__name

    @property
    def employerId(self):
        return self.__category
    
    @property
    def employeeIdentityId(self):
        return self.__employeeIdentityId
    
with open('data.psv') as f:
    for lines in f.readlines():
        fieldsList=[];
        fieldsList= lines.strip().split('|')
        psvItemList=[PsvItems(fieldsList[0],fieldsList[1],fieldsList[2],fieldsList[3])]
        
# TODO : Create a function Update on the class to update each item update the data in to the table
# Need to parameter the values right now its done like psvItemList=[PsvItems(fieldsList[0],fieldsList[1],fieldsList[2],fieldsList[3])]
# is passed from psv file as a record and update the data base table Need to update in SQL server database.

    
        