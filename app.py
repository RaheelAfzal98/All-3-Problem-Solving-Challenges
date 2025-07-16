# Problem 1: Reverse a String 
# This function takes a string and return it reversed using slicing.

def reverse_string(text):
    return text[::-1]

# Problem 2: Count Vowels in a string 
# This function counts the number of vowels(a,e,i,o,u) in the input string.
# It works in a case-insensitive manner.

def count_vowels(text):
    vowels = set("AEIOUaeiou")
    count = 0
    for t in text:
        if t in vowels:
            count += 1
    return count

# Problem 3: Sum of digits
# This function takes a non_negative integer and returns the sum of its digits.

def sum_of_digits(number:int):
    return sum(int(digit) for digit in str(number))

#Run tests only when this script is executed directly
if __name__ == "__main__":
    print(reverse_string("hello"))           # Output: olleh
    print(count_vowels("Apple"))             # Output: 2
    print(sum_of_digits(1234))               # Output: 10

