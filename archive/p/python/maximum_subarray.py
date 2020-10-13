def maximum_subarray():
    str_input = input()
    if str_input == "":
        print("Usage: Please provide a list of at least two integers to sort in the format: '1, 2, 3, 4, 5'")
        return

    # split comma separated input string into list of integers
    arr = [int(num) for num in str_input.split(',')]
    ans = 0
    curr_sum = 0
    for i in range(len(arr)):
        if (curr_sum + arr[i] > 0):
            curr_sum += arr[i]
        else:
            curr_sum = 0
        ans = max(ans, curr_sum)
    print(ans)
    return


if __name__ == "__main__":
    maximum_subarray()  # call function to carry out kadane's algorithm
