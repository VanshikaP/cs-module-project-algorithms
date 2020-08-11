'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # dictionary for counts
    counts = {}

    # add item counts
    for item in arr:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    
    # find item with count 1
    for item, val in counts.items():
        if val is 1:
            return item



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")