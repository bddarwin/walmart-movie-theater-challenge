import MovieTheater

#Test 1 - Opening an Invalid File.
print("Test One - Opening an Invalid File.\n")
MovieTheater.movieTheater("SampleData/SampleDataFAIL.txt")
print("\n")

#Test 2 - Opening a valid file.
print("Test Two - Opening a Valid File.\n")
MovieTheater.movieTheater("SampleData/SampleDataOne.txt")
print("\n")
