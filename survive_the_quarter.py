"""
Name: Aastha Aastha
Group: C
Feature Chosen: Feature (c) - High score: at the end of the game, the program reads
results.csv and tells the player whether they beat the previous best budget. I chose
this feature because it adds replayability and directly uses the results.csv file
across multiple games.

1. What goes in?
My scenario file (scenarios_C.csv) uses a comma (,) as the separator and contains 14 columns:
Event, Day, Decision 1, Decision 2, Decision 3, Reputation 1, Reputation 2, Reputation 3,
Budget 1, Budget 2, Budget 3, Outcome 1, Outcome 2, Outcome 3.
The numbers are written as text with signs and units attached, such as "+15 pts" or "-10 pts"
for reputation, and "-800 EUR" or "+2500 EUR" for budget, so the code strips those text units
before converting them into integers.

2. What happens? (The steps of one day, in order)
- Display the current day number (1 to 10), current budget (EUR), and current reputation (/100).
- Display the day's situation (event) and options A, B, and C.
- Ask the player to choose A, B, or C, repeating until they enter a valid letter (case-insensitive).
- Unpack the chosen option tuple and apply its budget change and reputation change to the gauges.
- Clamp reputation so it never exceeds 100, and display the choice's outcome feedback and changes.
- Record the day's move as a tuple in the history list to track the best and worst moves.
- Check if budget or reputation is 0 or less; if so, fire the player and stop the game immediately.

3. What comes out?
At the end of the game, the player sees whether they were fired (and which gauge hit 0) or
survived all 10 days, their final budget, final reputation, final score, earned title
(Eternal Intern, Growth Hacker, CMO Material, or Viral Legend), their best and worst moves
based on reputation change, and whether they beat the best budget recorded in results.csv.
One line appended to results.csv looks like:
Aastha,6350,100,CMO Material,2026-11-16

4. What could go wrong?
- Missing scenario file: If scenarios_C.csv is not found, a try/except FileNotFoundError block
  catches the error and prints a clear message instead of crashing.
- Invalid user input: If the player types a number, blank space, or wrong letter instead of A, B,
  or C, a while loop rejects it and asks again without crashing.
- First game with no results.csv yet: When checking the high score (Feature c) on the very first
  run, results.csv does not exist yet or has no valid rows; the function checks os.path.exists
  and handles empty/missing data gracefully before writing the new result.
- Gauge dropping below zero or reputation going above 100: Reputation is capped at 100 with min(),
  and any budget or reputation <= 0 triggers an immediate break out of the 10-day loop.
"""

import csv
import os
import random
from datetime import date

SCENARIO_FILE = "scenarios_C.csv"
RESULTS_FILE = "results.csv"


def parse_number(raw_text: str, unit: str) -> int:
    """Strips units like 'pts' or 'EUR' and converts signed text into an integer."""
    cleaned = raw_text.replace(unit, "").strip()
    return int(cleaned)


def load_scenarios(filename: str) -> list[dict]:
    """Reads scenarios_C.csv and builds a list of scenario dictionaries with option tuples."""
    scenarios = []
    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Store each option as a tuple: (text, budget_change, reputation_change, feedback)
            option_a = (
                row["Decision 1"].strip(),
                parse_number(row["Budget 1"], "EUR"),
                parse_number(row["Reputation 1"], "pts"),
                row["Outcome 1"].strip(),
            )
            option_b = (
                row["Decision 2"].strip(),
                parse_number(row["Budget 2"], "EUR"),
                parse_number(row["Reputation 2"], "pts"),
                row["Outcome 2"].strip(),
            )
            option_c = (
                row["Decision 3"].strip(),
                parse_number(row["Budget 3"], "EUR"),
                parse_number(row["Reputation 3"], "pts"),
                row["Outcome 3"].strip(),
            )
            scenarios.append({
                "event": row["Event"].strip(),
                "options": {"A": option_a, "B": option_b, "C": option_c},
            })
    return scenarios


def get_valid_choice() -> str:
    """Keeps asking until the player enters A, B, or C (case-insensitive)."""
    choice = input("Your choice (A, B or C): ").strip().upper()
    while choice not in ("A", "B", "C"):
        choice = input("Please type A, B or C: ").strip().upper()
    return choice


def apply_choice(budget: int, reputation: int, option: tuple) -> tuple[int, int]:
    """Applies an option's budget and reputation changes and caps reputation at 100."""
    _, budget_change, rep_change, _ = option
    new_budget = budget + budget_change
    new_reputation = min(100, reputation + rep_change)
    return new_budget, new_reputation


def get_title(budget: int, reputation: int) -> tuple[int, str]:
    """Calculates final score and returns (score, title) based on game rules."""
    if budget <= 0 or reputation <= 0:
        return 0, "Fired"
    score = reputation + (budget // 200)
    if score < 95:
        title = "Eternal Intern"
    elif score <= 119:
        title = "Growth Hacker"
    elif score <= 139:
        title = "CMO Material"
    else:
        title = "Viral Legend"
    return score, title


def get_best_previous_budget(filename: str) -> int | None:
    """Reads results.csv (Feature c) and returns the highest surviving budget recorded."""
    if not os.path.exists(filename):
        return None
    best_budget = None
    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 4 and row[0] != "name":
                try:
                    saved_budget = int(row[1])
                    saved_title = row[3].strip()
                    if saved_title != "Fired":
                        if best_budget is None or saved_budget > best_budget:
                            best_budget = saved_budget
                except ValueError:
                    continue
    return best_budget


def save_result(filename: str, name: str, budget: int, reputation: int, title: str) -> None:
    """Appends one completed game summary row to results.csv."""
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0
    today_str = date.today().isoformat()
    with open(filename, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        writer.writerow([name, budget, reputation, title, today_str])


def play_game() -> None:
    """Runs the 10-day Croissant Rocket marketing simulation."""
    try:
        scenarios = load_scenarios(SCENARIO_FILE)
    except FileNotFoundError:
        print(f"Error: Could not find '{SCENARIO_FILE}'. Make sure it is in the same folder.")
        return

    if len(scenarios) < 10:
        print("Error: Not enough scenarios in the file to play 10 days.")
        return

    print("=== SURVIVE THE QUARTER: CROISSANT ROCKET ===")
    player_name = input("Enter your name: ").strip()
    while not player_name:
        player_name = input("Name cannot be empty. Enter your name: ").strip()

    # Shuffle scenarios and pick 10 for the quarter
    random.shuffle(scenarios)
    game_scenarios = scenarios[:10]

    budget = 10000
    reputation = 50
    history = []  # Stores tuples: (rep_change, day, option_text)
    fired_reason = ""

    # Main 10-day game loop
    for day in range(1, 11):
        scenario = game_scenarios[day - 1]
        options = scenario["options"]

        print("\n" + "-" * 45)
        print(f"Day {day}")
        print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
        print(scenario["event"])
        print(f"A: {options['A'][0]}")
        print(f"B: {options['B'][0]}")
        print(f"C: {options['C'][0]}")

        choice = get_valid_choice()
        chosen_option = options[choice]
        opt_text, budget_delta, rep_delta, feedback = chosen_option

        # Unpack returned tuple from apply_choice
        budget, reputation = apply_choice(budget, reputation, chosen_option)

        # Record move in history (rep_delta first so min/max compares reputation change)
        history.append((rep_delta, day, opt_text))

        print(feedback)
        print(f"Budget {budget_delta:+d} EUR, Reputation {rep_delta:+d}")

        # Check immediate firing condition
        if budget <= 0:
            fired_reason = "Your budget hit 0 EUR. The company is out of money!"
            break
        if reputation <= 0:
            fired_reason = "Your reputation hit 0/100. Everyone hates Croissant Rocket!"
            break

    # End-of-game summary
    print("\n" + "=" * 30)
    score, title = get_title(budget, reputation)

    if title == "Fired":
        print("YOU ARE FIRED!")
        print(fired_reason)
        print(f"Final gauges -> Budget: {budget} EUR | Reputation: {reputation}/100")
    else:
        print("Quarter survived!")
        print(f"Budget left: {budget} EUR, reputation: {reputation}/100")
        print(f"Final score: {score}")
        print(f"{player_name}, your title: {title}")

    # Best and worst moves (compared by first element of tuple: rep_delta)
    if history:
        best_move = max(history)
        worst_move = min(history)
        print(f'Best move: day {best_move[1]}, "{best_move[2]}" ({best_move[0]:+d})')
        print(f'Worst move: day {worst_move[1]}, "{worst_move[2]}" ({worst_move[0]:+d})')

    # Feature (c): Compare against best previous surviving budget in results.csv
    previous_best = get_best_previous_budget(RESULTS_FILE)
    if title != "Fired":
        if previous_best is None:
            print(f"High score check: New record! {budget} EUR is the first surviving budget.")
        elif budget > previous_best:
            print(f"High score check: New record! You beat the previous best budget ({previous_best} EUR)!")
        else:
            print(f"High score check: You did not beat the best budget ({previous_best} EUR).")
    else:
        if previous_best is not None:
            print(f"High score check: Best surviving budget to beat is {previous_best} EUR.")

    # Save game outcome to results.csv
    save_result(RESULTS_FILE, player_name, budget, reputation, title)
    print(f"Saved in {RESULTS_FILE}")


if __name__ == "__main__":
    play_game()