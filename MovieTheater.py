import sys

#Process the Entire Script.
def movieTheater(inputFile=None, outputFile=None):
    inputData = get_input_file(inputFile)
    if (inputData != None):
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
        
    return input_file.read()
    
    
#Parse the input file.
def parse_input_file(inputData):
    
    #Default format R000 X where 000 is reservation number and X is number of seats.
    
    #Split on the newline to get each reservation.
    reservations = inputData.split("\n")
    parsedData = dict()
    #Now split each name into a key->value pair.
    for res in reservations:
        this_res = res.split(" ")
        parsedData[this_res[0]] = int(this_res[1])
    return parsedData
    
#Assign Seats
def assign_seats(parsedData):

    #Assume we want to start by filling in rows closest to the middle first,
    #with seats towards the middle priority. No one wants to sit on an edge
    #or at the top or bottom of the theater. 
    rows = [ [], [], [], [], [], [], [], [], [], [] ]
    current_row = 0
    current_position = "new"
    for res, num in parsedData.items():
        print("Reservation: ", res, ", seats: ", num, "\n")
        if( (len(rows[current_row]) + num + 3) <= 20):
            #We have room on the current row. 
            if(current_position == "new"):
                #Starting a new row, so don't need empty seats.
                for n in range(num):
                    rows[current_row].append(res)
                    
                #Set to start
                current_position = "start"
            elif(current_position == "start"):
                #Add the seats to the start.
                
                #Space 3 Empty seats
                rows[current_row].insert(0, "Empty")
                rows[current_row].insert(0, "Empty")
                rows[current_row].insert(0, "Empty")
                
                #Add the seats for the reservation
                for n in range(num):
                    rows[current_row].insert(0, res)
                
                #We've added a reservation, now change to add on the other side of the row.
                #This keeps earliest reservations in the middle.
                current_position = "end"
            else:
                #Space 3 empty seats
                rows[current_row].append("Empty")
                rows[current_row].append("Empty")
                rows[current_row].append("Empty")
                #Add the seats for the reservation
                for n in range(num):
                    rows[current_row].append(res)
                    
                #Now switch back to the beginning of the row.
                current_position = "start"
        else:
            #No room on current row, start a new row.
            current_row += 1
            for n in range(num):
                rows[current_row].append(res)
            current_position = "start"
     
    print (rows)
    return

#Output the output file.
def write_output_file(seats, name=None): 
    return

if __name__ == "__main__":
    movieTheater()