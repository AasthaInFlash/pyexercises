"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of daily temperatures (floats).
# 2. Process, function by function: #    - `calculate_mean`: Computes the average value of a list of numbers.
#    - `filter_above_threshold`: Collects all numbers from a list that exceed a given cutoff.
#    - `count_items`: Counts how many elements exist in a list.
#    - `count_above_average_days`: Combines those three functions in order to get the final count.
# 3. Out: A single integer representing how many days had temperatures above the average.
# 4. The question my fourth function answers: It answers: "How many days in the list were warmer than the average temperature?"
#    Splitting it into three small functions makes it easier to check because each piece
#    can be tested independently with simple inputs. If the final count is wrong, I can
#    test each helper alone to pinpoint whether the math, the filtering, or the counting failed.


# Your code below

def calculate_mean(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def filter_above_threshold(numbers: list[float], threshold: float) -> list[float]:
    return [num for num in numbers if num > threshold]


def count_items(items: list) -> int:
    return len(items)


def count_above_average_days(temperatures: list[float]) -> int:
    average_temp = calculate_mean(temperatures)
    warmer_days = filter_above_threshold(temperatures, average_temp)
    return count_items(warmer_days)


assert calculate_mean([10.0, 20.0, 30.0]) == 20.0
assert filter_above_threshold([15.0, 22.0, 18.0, 25.0], 20.0) == [22.0, 25.0]
assert count_items([22.0, 25.0]) == 2

print("All 3 unit tests passed!")

daily_temps = [18.5, 20.0, 21.2, 19.8, 22.1, 23.0, 21.5]
result = count_above_average_days(daily_temps)
print(f"Days above average temperature: {result}")
