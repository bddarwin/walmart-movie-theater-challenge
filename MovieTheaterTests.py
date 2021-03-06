import MovieTheater

#Test 1 - Opening an Invalid File.
print("Test One - Opening an Invalid File.\n")
MovieTheater.movieTheater("SampleData/SampleDataFAIL.txt")
print("\n")

#Test 2 - Opening a valid file.
print("Test Two - Opening a Valid File.\n")
MovieTheater.movieTheater("SampleData/SampleDataOne.txt")
print("\n")

#Test 3 - Opening a valid file while setting output file.
print("Test Three - Testing Custom Output file.\n")
MovieTheater.movieTheater("SampleData/SampleDataOne.txt", "Output/TestOutputFile.txt")
print("\n")

#Test 4 - Lots more data.
print("Test Four - Lots more seats taken.\n")
MovieTheater.movieTheater("SampleData/SampleDataTwo.txt", "Output/OutputDataTwo.txt")
print("\n")

#Test 5 - Blank File
print("Test Five - Blank File.\n")
MovieTheater.movieTheater("SampleData/SampleDataBlank.txt")
print("\n")

#Test 6 - Invalid Data
print("Test Six - Invalid Data File.\n")
MovieTheater.movieTheater("SampleData/SampleDataInvalid.txt")
print("\n")

#Test 7 - Too many seats.
print("Test Seven - Too many seats.\n")
MovieTheater.movieTheater("SampleData/SampleDataOverload.txt", "Output/OutputDataOverload.txt")
print("\n")