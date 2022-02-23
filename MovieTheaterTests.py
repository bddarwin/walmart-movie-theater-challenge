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