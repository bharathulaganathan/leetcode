from pathlib import Path
import sys

from query import query


def main():
    problems_dir = get_problems_dir()
    title_slug = str()
    question = dict()
    while not title_slug or not question:
        question, title_slug = leetcode_options()


def get_problems_dir():
    current_file = Path(__file__).resolve()
    problems_dir = current_file.parent.parent / "problems"
    while not problems_dir.exists():
        try:
            user_response = input("Need 'problems' folder. Create it? [y/N]: ").lower()
            if user_response in ["y", "yes"]:
                problems_dir.mkdir()
                print("Created 'problems' folder.")
            elif user_response in ["n", "no", ""]:
                sys.exit("Exiting...")
            else:
                print("Wrong input. Try again.")
        except KeyboardInterrupt:
            sys.exit("\nExiting...")
    return problems_dir


def leetcode_options():
    available_options = ["Daily", "Random", "Search"]
    options = {}
    for o, option in enumerate(available_options, start=1):
        options[o] = option
        print(f"{o}. {option}")
    choice = 1
    while True:
        try:
            user_option = input("Choose an option (default 1): ")
            if user_option == "":
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
    choice = options[choice]
    title_slug = ""
    if choice == "Daily":
        title_slug = query.questionOfTodayV2()["data"]["activeDailyCodingChallengeQuestion"]["question"]["titleSlug"]
    elif choice == "Random":
        title_slug = leetcode_random()
    elif choice == "Search":
        title_slug = leetcode_search()
    if not title_slug:
        sys.exit("Couldn't find the problem.\nExiting...")
    question = query.questionDetail(title_slug)["data"]["question"]
    title = question["title"]
    title_id = question["questionFrontendId"]
    print(f"The {choice} Problem is:\n{title_id}. {title}")
    return (question, title_slug)


def leetcode_random():
    while True:
        title_slug = query.randomQuestionV2()["data"]["randomQuestionV2"]["titleSlug"]
        question = query.questionDetail(title_slug)["data"]["question"]
        title = question["title"]
        title_id = question["questionFrontendId"]
        print(f"{title_id}. {title}")
        response = False
        while not response:
            try:
                user_input = input("Get another Random Problem? [y/N]: ").lower()
                if user_input in ["y", "yes"]:
                    break
                elif user_input in ["n", "no", ""]:
                    response = True
                    break
                else:
                    continue
            except KeyboardInterrupt:
                sys.exit("\nExiting")
        if response:
            return title_slug


def leetcode_search():
    title_slug = ""
    while not title_slug:
        try:
            search = input("Problem Search: ")
            if search == "":
                continue
            variables = {"limit": 5}
            result = query.problemsetPanelQuestionList(search, variables)
            result = result["data"]["problemsetPanelQuestionList"]
            result_len = len(result["questions"])
            if result_len < 1:
                print("No result found for the search term.")
            else:
                title_slug = result_select(result)
            if title_slug:
                break
        except KeyboardInterrupt:
            sys.exit("\nExiting...")
    if not title_slug:
        print("Couldn't find the problem. Try again.")
    return title_slug


def result_select(result):
    title_slug = ""
    search_problems = {}
    problem_count = max(5, len(result["questions"]))
    print(f"Top {problem_count} results:")
    for p in range(problem_count):
        p_num = result["questions"][p]["questionFrontendId"]
        p_title = result["questions"][p]["title"]
        p_title_slug = result["questions"][p]["titleSlug"]
        search_problems[p_num] = p_title_slug
        print(f"{p_num}. {p_title}")
    while True:
        try:
            user_option = input("Choose a problem number (Enter for first option): ")
            if user_option == "":
                title_slug = result["questions"][0]["titleSlug"]
                break
            if user_option in search_problems.keys():
                title_slug = search_problems[user_option]
                break
            else:
                print("Give a valid option number.")
        except KeyboardInterrupt:
            print("")
            break
    return title_slug


if "__main__" == __name__:
    main()
