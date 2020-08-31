#!/usr/bin/python3
import sys

def main():
    # Simply modified the this line to print the result of the function call.
    print(next_biggest_number(sys.argv[1]))


def next_biggest_number(num):
    # Create a list of digits and get its length.
    digits = list(map(int,str(num)))
    n = len(digits)
    # Check to see if the digits are non-decreasing from right
    # to left. If so, this is the largest number that can be
    # formed from these digits. In that case, return '-1'.
    # Start by comparing the tens and ones digit. Work to the
    # left, and exit the loop when a smaller digit is encountered
    # to the left.
    k = 2
    while digits[n - k] >= digits[n - k + 1] :
        k += 1
        if n - k < 0:
            return -1
    # If we encountered a smaller digit, initialize a new list for
    # the next biggest number.
    next_biggest = []
    # Place the first n-k digits of the original list into the new list.
    # These are unchanged.
    next_biggest.extend(digits[0:n - k])
    # Next, append the smallest digit larger than the n-k+1th digit
    # to the new list. Remove that digit from the old list before sorting.
    next_biggest.append(digits.pop(n - digits[::-1].index(min(filter(
        lambda x: x > digits[n - k], digits[n - k + 1:n])))-1))
    # After removing that digit, sort the digits after the n-k+1th digit
    # and add them to the new list in ascending order. This list of digits
    # represents the next biggest number.
    next_biggest.extend(sorted(digits[n-k:n]))
    # Reconstruct the number from the list of digits and return the number.
    result = 0
    for i in range(n) :
        result = result + next_biggest[i] * 10 ** (n - i - 1)
    return result

if __name__ == "__main__":
    main()
