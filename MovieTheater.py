import sys

#Process the Entire Script.
def movieTheater(inputFile=None, outputFile=None):
    inputData = get_input_file(inputFile)
    parsedData = parse_input_file(inputData)
    seats = assign_seats(parsedData)
    write_output_file(seats, outputFile)
    
#Get the input file.
def get_input_file(name=None):

    #Did we include the name argument?
    if(name != None):
        file_name = name
    #Check that the argument was included.
    else:
        if(len(sys.argv) == 1):
            print("Error: No argument was found for the input file. An input file must be included.")
            return
        file_name = sys.argv[1]
        
    #Try and find the input file.
    try:
        input_file = open(file_name, "r")
    except IOError:
        print("Error: File could not be read.")
        return
        
    print(input_file.read())
    
    
#Parse the input file.
def parse_input_file(inputData):
    sys.exit()
#Assign Seats
def assign_seats():
    sys.exit()

#Output the output file.
def write_output_file(seats, name=None): 
    sys.exit()

if __name__ == "__main__":
    get_input_file()