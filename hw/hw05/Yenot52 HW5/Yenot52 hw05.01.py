#Task 1
def convert_to_float(integer_list):
    float_list = []
    for num in integer_list:
        float_list.append(float(num))
    return float_list
    
#Create a sample list of integers
integer_list = [1, 2, 3, 4, 5]

#Convert integers to floats
float_list = convert_to_float(integer_list)

#Print the original and converted lists 
print("Original list:", integer_list)
print("Converted list:", float_list)