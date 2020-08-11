'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(arr, k):
    # Your code here
    window = [arr[i] for i in range(k)]
    output = []

    def add_max():
        max = window[0]
        for i in range(k):
            if window[i] > max:
                max = window[i]
        output.append(max)
    
    add_max()
    for i in range(1, len(arr) - k + 1):
        window.remove(arr[i - 1])
        window.append(arr[i + k - 1])
        add_max()
    
    return output

        # takes 53.791 sec for large test file


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
