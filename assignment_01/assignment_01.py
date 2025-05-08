# Assignment 1: write a Python script that calculates the average of the integers that are divisible by 3
# Sample input: 1, 6, 10, 15, 99, 45, 56, 32, 150, 151, 672, 558, 789, 335, 23, 65, 47, 33
# Average formula: average = sum of numbers / count of numbers

def avg_three( input: list [ int ] ) -> float:
    """
    This function takes a list of integers and returns the average of the integers that are divisible by 3.
    :param input: list of integers
    :return: a float - the average of integers divisible by 3
    """
    # Check if the input is a list
    # If the input is not a list raise a TypeError
    # Using the built-in isinstance() function to check the type of input
    if not isinstance(input, list):
        raise TypeError("Input must be a list of integers.")

    # Filter the list to only include integers divisible by 3
    # Using list comprehension to filter the list
    divisible_by_3 = [num for num in input if num % 3 == 0]
    
    # Calculate the average
    # If there are no integers divisible by 3, return 0.0
    # If there are integers divisible by 3, return the average
    # Using the built-in sum() and len() functions to calculate the average
    if len(divisible_by_3) == 0:
        return 0.0
    else:
        return sum(divisible_by_3) / len(divisible_by_3)

# Test the function
# if __name__ == "__main__":
test_list = [1, 6, 10, 15, 99, 45, 56, 32, 150, 151, 672, 558, 789, 335, 23, 65, 47, 33]
#     # test_list =  [3 , 8, 15]
#     # test_list = [87, 64, 998, 46, 332, 78, 98]
#     # test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#     # test when the input is empty list
#     # test_list = []

   
#     # test when the input is not a list
#     # test_list = 1
#     # test_list = ()
#     # test_list = (1, 6, 10, 15, 99, 45, 56, 32, 150, 151, 672, 558, 789, 335, 23, 65, 47, 33)
#     # test_list = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"The average of the integers divisible by 3 in the list is: {avg_three(test_list)}")
    