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
    options = {}
    for o, option in enumerate(leetcode_options, start=1):
        options[o] = option
        print(f"{o}. {option}")
    choice = int()
    while True:
        try:
            user_option = input("Choose an option (default 1): ")
            if user_option == "":
                choice = 1
                break
            user_option = int(user_option)
            if user_option in options.keys():
                choice = user_option
                break
            else:
                print("Give a valid option number.")
        except ValueError:
            print("Give an option number.")
        except KeyboardInterrupt:
            sys.exit("\nExiting")
    title_slug = str()
    found_problem = False
    if options[choice] == "Daily":
        title_slug = query.questionOfTodayV2()["data"]["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]
        if not title_slug:
            sys.exit("Couldn't find Daily Question.\nExiting...")
        found_problem = True
    elif options[choice] == "Random":
        title_slug = query.randomQuestionV2()["data"]["randomQuestionV2"]["titleSlug"]
        if not title_slug:
            sys.exit("Couldn't find a Random problem.\nExiting...")
        found_problem = True
    while not found_problem and not title_slug:
        try:
            search = input("Problem Search: ")
            variables = {"limit": 5}
            search_result = query.problemsetPanelQuestionList(search, variables)["data"]["problemsetPanelQuestionList"]
            if search_result["totalLength"] == 0:
                print("No result found for the search term.")
                continue
            elif search_result["totalLength"] == 1:
                title = search_result["questions"][0]["title"]
                title_slug = search_result["questions"][0]["titleSlug"]
                while True:
                    try:
                        print(f"Problem found: {title}")
                        confirm = input("Is this the problem? [Y/n]: ").lower()
                        if confirm in ["y", "yes", ""]:
                            found_problem = True
                            break
                        elif confirm in ["n", "no"]:
                            break
                    except KeyboardInterrupt:
                        print("")
                        break
                if found_problem:
                    break
            else:
                search_problems = {}
                problem_count = len(search_result["questions"])
                print(f"Top {problem_count} results:")
                for p in range(problem_count):
                    p_num = search_result["questions"][p]["questionFrontendId"]
                    p_title = search_result["questions"][p]["title"]
                    p_title_slug = search_result["questions"][p]["titleSlug"]
                    search_problems[p_num] = p_title_slug
                    print(f"{p_num}. {p_title}")
                while True:
                    try:
                        user_option = input("Choose a problem number (Enter to search again): ")
                        if user_option == "":
                            break
                        if user_option in search_problems.keys():
                            title_slug = search_problems[user_option]
                            break
                        else:
                            print("Give a valid option number.")
                    except ValueError:
                        print("Give an option number.")
                    except KeyboardInterrupt:
                        print("")
                        break
        except KeyboardInterrupt:
            sys.exit("\nExiting...")
    if not title_slug:
        print("Couldn't find the problem. Try again.")

    print(f"{choice}: {title_slug}")





if "__main__" == __name__:
    main()

