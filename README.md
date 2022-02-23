# walmart-movie-theater-challenge

## Assumptions Made

The following assumptions have been made: 
1. Seats towards the middle row are preferred most, with center seats in that row being ideal, and seats further to the edge less ideal. 
2. Ideally, rows should be filled every other row, but if a showing of the movie gets too crowded, every row can be filled. 
3. As a show gets even more crowded, customers would still want empty seats next to them. Overflow customers at this point would have to be pushed to another showing.

## Executing the Script
The script can be executed in the command line by executing MovieTheater.py. The file accepts one argument - the file name of the input file.

## Executing the Tests
The tests for the script can be executed in the command line by executing MovieTheaterTest.py. 

## Including the script in another project
If you choose to include the script in another project, a function exists as movieTheater(inputFile, ouptputFile=None), where inputFile is the file with the reservation data, and outputFile is where the data will be written. If outputFile is not specified, it will default to Output/AssignedSeats.txt.

## Known Issues and Future Goals
With more time to work on the project, my first goal would be to fill out the rows better. For example, if a reservation with 7 tickets comes up, and the row currently being filled only has 6 seats left, those 6 seats will be left empty and a new row is started. Smaller reservations from further in the reservation list could go back and fill in those empty seats.
My second goal would be to prioritize earlier reservations being as close to the center of a row as possible - they are currently only centered by number of reservations on each side of them, rather than number of seats filled on each side.
