import sys, math

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
    rows = [[]]
    current_row = 0
    current_position = "new"
    for res, num in parsedData.items():
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
            rows.append([])
            #First, append seats to the existing row to make it 20.
            num_seats = (20 - len(rows[current_row]))
            num_seats_before = math.floor(num_seats /2)
            num_seats_after = math.floor(num_seats /2)
            for n in range(num_seats_before):
                rows[current_row].insert(0, "Empty")
            for n in range(num_seats_after):
                rows[current_row].append("Empty")
            current_row += 1
            for n in range(num):
                rows[current_row].append(res)
            current_position = "start"
    #We've ended so lets append the final row we've been working on with empty seats.
    num_seats = (20 - len(rows[current_row]))
    num_seats_before = math.floor(num_seats /2)
    num_seats_after = math.floor(num_seats /2)
    for n in range(num_seats_before):
        rows[current_row].insert(0, "Empty")
    for n in range(num_seats_after):
        rows[current_row].append("Empty")   
    
    #Now that we've assigned seats, we can create the output data 
    
    #Rows to letters to prioritize non-overlapping but better seats to earlier reservations.
    
    if(len(rows) <= 5):
        row_letters = ["F", "H", "D", "J", "B"]
    elif(len(rows) == 6):
        row_letters = ["F", "G", "H", "D", "J", "B"]
    elif(len(rows) == 7):
        row_letters = ["F", "G", "H", "E", "D", "J", "B"]
    elif(len(rows) == 8):
        row_letters = ["F", "G", "H", "E", "D", "I", "J", "B"]
    elif(len(rows) == 9):
        row_letters = ["F", "G", "H", "E", "D", "I", "J", "C", "B"]        
    elif(len(rows) == 10):
        row_letters = ["F", "G", "H", "E", "D", "I", "J", "C", "B", "A"]
       
       
    assignedSeats = dict()
    for row, rowdata in enumerate(rows):
        for index, seat in enumerate(rowdata):
            if(seat != "Empty"):
                if seat in assignedSeats.keys():
                    #Add the seat to the existing key.
                    assignedSeats[seat].append(str(row_letters[row]) + str(index+1))
                else:
                    assignedSeats[seat] = [str(row_letters[row]) + str(index+1)]

    assignedSeats = dict(sorted(assignedSeats.items()))
    return assignedSeats

#Output the output file.
def write_output_file(assignedSeats, name=None): 

    #If we don't have a filename, set one.
    if(name == None):
        name = "Output/AssignedSeats.txt"
    
    #Try and Open the File.
    try:
        output_file = open(name, "w")
    except IOError:
        print("Error: File could not be written.")
        return 
     
    #parse the assigned seats data into a single string to write to the file.
    file_contents = "" 
    for res, seats in assignedSeats.items():
        file_contents += res + " "
        for seat in seats:
            file_contents += seat + ","
        #trim the last comma
        file_contents = file_contents[:-1]
        #add a newline.
        file_contents += "\n"
    
    #Write the contents to the file.
    output_file.write(file_contents)
    print("File successfully written to: ", name)
    return

if __name__ == "__main__":
    movieTheater()