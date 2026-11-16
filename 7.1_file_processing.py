"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - Blank lines: lines 3 and 9 are completely empty.
# - Leading whitespace: lines for Alan Turing and Linus Torvalds have extra spaces at the beginning.
# - Inconsistent capitalization: names mix all-lowercase ("grace hopper"), lower-UPPER ("ada LOVELACE"), and UPPER-lower ("GUIDO van rossum").
# - Multi-word last name: "GUIDO van rossum" has three words ("van rossum" is a two-word surname) instead of the usual two words.

# 1. In:A plain text file named `names.txt` containing 10 lines (8 messy full names and 2 blank lines).
# 2. Process, problem by problem: #    - Blank lines: strip each line and skip it if it is empty (`if not cleaned_line: continue`).
#    - Leading/trailing spaces: remove extra outer whitespace with `.strip()` and collapse any accidental double spaces with `" ".join(line.split())`.
#    - Inconsistent capitalization: normalize each name to proper Title Case using `.title()` so every name follows "First Last" formatting.
#    - Multi-word last name & sorting: sort using a key function that splits the full name after the first word (`name.split(" ", 1)[1].lower()`), so "van rossum" is treated as one complete surname rather than just "van".
# 3. Out: A new file named `cleaned_names.txt` containing 8 clean, properly capitalized lines sorted alphabetically by last name (2 fewer lines than `names.txt` because the 2 blank lines were removed), while `names.txt` remains untouched.
# 4. How I decide which word is the last name: How I decide which word is the last name: In standard "First Last" order, the first word is the first name and everything after the first space (`split(" ", 1)[1]`) is the last name—this works for both two-word names (taking index 1) and multi-word surnames like "Van Rossum".


# Your code below

INPUT_FILE = "names.txt"
OUTPUT_FILE = "cleaned_names.txt"


def load_and_clean_names(filename: str) -> list[str]:
    """Reads raw lines from filename, skips blank lines, fixes spacing, and title-cases names."""
    cleaned_names = []
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            # Remove leading/trailing whitespace and normalize internal spacing
            normalized = " ".join(line.strip().split())
            if not normalized:
                continue
            cleaned_names.append(normalized.title())
    return cleaned_names


def get_last_name(full_name: str) -> str:
    """Returns the last name (everything after the first word) in lowercase for sorting."""
    parts = full_name.split(" ", 1)
    if len(parts) > 1:
        return parts[1].lower()
    return parts[0].lower()


def save_names(filename: str, names: list[str]) -> None:
    """Writes the cleaned, sorted names to a new output file, one per line."""
    with open(filename, mode="w", encoding="utf-8") as file:
        for name in names:
            file.write(name + "\n")


def main() -> None:
    names = load_and_clean_names(INPUT_FILE)
    sorted_names = sorted(names, key=get_last_name)
    save_names(OUTPUT_FILE, sorted_names)
    print(f"Saved {len(sorted_names)} cleaned names to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()