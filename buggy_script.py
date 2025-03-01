# Buggy Python script to calculate the sum of integers in a list
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        if isinstance(num, int): 
            total += num
    return total

# Calling the function with a string in the list
nums = [1, 2, '3', 4]
print("Sum of numbers:", calculate_sum(nums))
