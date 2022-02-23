import sys

#Get the input file.
def get_input_file():
    #Check that the argument was included.
    if(len(sys.argv) == 1):
        print("Error: No argument was found for the input file. An input file must be included.")
        sys.exit()
        
    #Try and find the input file.
    input_file = open(sys.argv[1], "r")
    print(input_file.read())
#Parse the input file.

#Assign Seats

#Output the output file.

get_input_file()