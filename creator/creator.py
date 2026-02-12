from pathlib import Path
import sys

from query import query


def main():
    current_file = Path(__file__).resolve()
    problems_dir = current_file.parent.parent / "problems"
    if not problems_dir.exists():
        try:
            user_response = input("Need 'problems' folder. Create it? [y/N]: ").lower()
            if user_response in ["y", "yes"]:
                problems_dir.mkdir()
                print("Created 'problems' folder.")
            elif user_response in ["n", "no", ""]:
                sys.exit("Exiting...")
            else:
                sys.exit("Wrong input.\nExiting...")
        except KeyboardInterrupt:
            sys.exit("\nExiting...")
    leetcode_options = ["Daily", "Random", "Search"]
    options = []
    for o, option in enumerate(leetcode_options, start=1):
        options.append({o: option})
        print(f"{o}. {option}")
    choice = int()
    while True:
        try:
            user_option = input("Choose an option (default 1): ")
            if user_option == "":
                choice = 1
                break
            user_option = int(user_option)
            for option in options:
                if user_option in option.keys():
                    choice = user_option
                    break
            if choice:
                break
            else:
                print("Give a valid option number.")
        except ValueError:
            print("Give an option number.")
        except KeyboardInterrupt:
            sys.exit("\nExiting")
    print(F"Choice is {choice}")


if "__main__" == __name__:
    main()

