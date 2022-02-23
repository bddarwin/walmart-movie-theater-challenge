import MovieTheater

#Test 1 - Opening an Invalid File.
print("Test One - Opening an Invalid File.\n")
MovieTheater.get_input_file("SampleData/SampleDataFAIL.txt")
print("\n")

#Test 2 - Opening a valid file.
print("Test Two - Opening a Valid File.\n")
MovieTheater.get_input_file("SampleData/SampleDataOne.txt")
print("\n")
