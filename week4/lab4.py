# Question 1: Robot Return to Origin

def robot_returns_to_origin(moves):
    # Initialize starting position
    x = 0
    y = 0

    for move in moves:
       if move = "U":
        y = y + 1 # y += 1
        elif move == "D":
            y = y - 1 # y -= 1
            elif move == "R":
                x = x+1  # y + 1 
                elif move = "L":
                    x = x -1 
                    return x == 0 and y == 0



    pass    

    # TODO: Loop through each move and update x, y

    # TODO: Return True if back at origin, False otherwise
    pass

    # Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))




    # Question 2: Two Sum

# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    for j in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] = target:
            return (i, j)

    return None

# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    seen = {}  # Dictionary to store {number: index}
    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in seen:
            return (seen[needed], i)
            seen[numbers[i]] = i

    return None

# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()
Expected Output
=== Part A: Brute Force (Nested Loops) ===
Numbers: [2, 7, 11, 15], Target: 9
Result: (0, 1)

Numbers: [3, 2, 4], Target: 6
Result: (1, 2)

Numbers: [3, 3], Target: 6
Result: (0, 1)

Numbers: [1, 5, 3, 8, 2], Target: 10
Result: (1, 3)

=== Part B: Optimized (Dictionary) ===
Numbers: [2, 7, 11, 15], Target: 9
Result: (0, 1)

Numbers: [3, 2, 4], Target: 6
Result: (1, 2)

Numbers: [3, 3], Target: 6
Result: (0, 1)

Numbers: [1, 5, 3, 8, 2], Target: 10
Result: (1, 3)
Hints
Part A (Nested Loops):

The inner loop starts at i + 1 to avoid checking the same pair twice
This approach checks every possible pair: O(n²) comparisons
Part B (Dictionary):

If target is 9 and current number is 2, you need 7 (target - current)
Store each number with its index: seen[numbers[i]] = i
Dictionary lookup is fast: O(1) per chec

Question 3: Shuffle the Array (List Slicing + Loops)
LeetCode #1470 | Concepts: List slicing ([:n], [n:]), for loop, range(), append()

Problem Statement
Given an array of the form [x1, x2, ..., xn, y1, y2, ..., yn], return the array in the form [x1, y1, x2, y2, ..., xn, yn].

In other words, interleave the first half with the second half.

Instructions
Create a function called shuffle_array that takes nums (list) and n (int) as parameters
Inside the function:
Use slicing to split the array into two halves:
first_half = nums[:n] (elements from index 0 to n-1)
second_half = nums[n:] (elements from index n to end)
Create an empty result list
Use a for loop with range(n) to interleave elements
Return the shuffled result
Test with multiple inputs and print intermediate steps
Starter Code


    # Question 3: Shuffle the Array

def shuffle_array(nums, n):
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    # TODO: slice from start to n
    second_half = nums[n:]   # TODO: slice from n to end

    # Step 2: Create empty result list
    result = []

    for i in range(n):
        result.append(first_half[i]):
        result.append(second_half[i]):

    return result


    # Step 3: Interleave using a for loop
    # TODO: Loop through range(n) and append alternating elements

    return result

# Test cases
test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()




# Question 4: First Unique Character

# Helper function: Count all characters in a string
def count_characters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
            else:
                counts[char] = 1
                return counts
    
    return counts

# Main function: Find first unique character
def first_unique_character(s):
    # Step 1: Get character counts using helper function
    char_counts = count_characters(s)
    for i in range (len(s)):
        if char_counts[s[i]] == 1:
            return i 
        return -1

    # Step 2: Loop through string with index to find first unique
    # TODO: Use for i in range(len(s)) to check each character
    # Return i if char_counts[s[i]] == 1

    # Step 3: Return -1 if no unique character found
    return -1

# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()