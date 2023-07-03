def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average
dataset=[4, 7, 8, 3, 56, 7]
answer=calculate_average(dataset)
print("The average is ", answer)