# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# MGalloway,05.26.2023,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def save_data_to_file(file_name, list_of_data):
        '''Saves string data to a file

        :param data: (string) with data to save
        :param file_name:(string) with name of file
        :return: nothing'''
        pass # TODO: Add code here
        objFile = open(file_name, "ab")
        pickle.dump(list_of_data,objFile)
        objFile.close()

    @staticmethod
    def read_data_from_file(file_name):
        '''Reads string data from file

        returns each row'''
        pass # TODO: Add code here
        objFile = open(file_name, "rb")
        objFileData = pickle.load(objFile) #load() only loads one row of data.
        objFile.close()
        return objFileData

# Presentation ------------------------------------ #
    # TODO: Get ID and NAME From user, then store it in a list object
    intPNo = int(input('Enter Part Number:'))
    strPName = str(input('Enter Part Name:'))
    lstCustomer = [intPNo, strPName]

    # TODO: store the list object into a binary file
    save_data_to_file(strFileName,lstCustomer)

    # TODO: Read the data from the file into a new list object and display the contents
    print(read_data_from_file(strFileName))
    print('\n')

# Error Handling ------------------------------------ #
try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isnumeric():
        raise Exception('Do not use numbers for the file\'s name')
except Exception as e:
    print("There was a non-specific error!")
    print(e, e.__doc__, type(e), sep='\n')

#Close program
print('\r')
input('Press enter to close program.')
exit()