from pathlib import Path
import sys
import json

from query import query


def main():
    problems_dir = get_problems_dir()
    title_slug = str()
    question = dict()
    while not title_slug or not question:
        question, title_slug = leetcode_options()
    create_problem(problems_dir, question)


def get_problems_dir():
    current_file = Path(__file__).resolve()
    problems_dir = current_file.parent.parent / "problems"
    while not problems_dir.is_dir():
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
    problem_id = question["questionFrontendId"]
    print(f"The {choice} Problem is:\n{problem_id}. {title}")
    return (question, title_slug)


def leetcode_random():
    while True:
        title_slug = query.randomQuestionV2()["data"]["randomQuestionV2"]["titleSlug"]
        question = query.questionDetail(title_slug)["data"]["question"]
        title = question["title"]
        problem_id = question["questionFrontendId"]
        print(f"{problem_id}. {title}")
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


def create_problem(problems_dir, question):
    title = question["title"]
    problem_id = question["questionFrontendId"]
    problem_folder = f"{problem_id}. {title}"
    problem_dir = problems_dir / problem_folder
    if not problem_dir.is_dir():
        problem_dir.mkdir()
        print(f"Problem folder created as '{problem_folder}'")
    create_solution(problem_dir, question)
    create_input(problem_dir, question)
    create_readme(problem_dir, question)


def create_solution(problem_dir, question):
    langs = {'cpp': {'id': 0, 'name': 'C++', 'extension': 'cpp'}, 'java': {'id': 1, 'name': 'Java', 'extension': 'java'}, 'python': {'id': 2, 'name': 'Python', 'extension': 'py'}, 'mysql': {'id': 3, 'name': 'MySQL', 'extension': 'sql'}, 'c': {'id': 4, 'name': 'C', 'extension': 'c'}, 'csharp': {'id': 5, 'name': 'C#', 'extension': 'cs'}, 'javascript': {'id': 6, 'name': 'JavaScript', 'extension': 'js'}, 'ruby': {'id': 7, 'name': 'Ruby', 'extension': 'rb'}, 'bash': {'id': 8, 'name': 'Bash', 'extension': 'sh'}, 'swift': {'id': 9, 'name': 'Swift', 'extension': 'swift'}, 'golang': {'id': 10, 'name': 'Go', 'extension': 'go'}, 'python3': {'id': 11, 'name': 'Python3', 'extension': 'py'}, 'scala': {'id': 12, 'name': 'Scala', 'extension': 'scala'}, 'kotlin': {'id': 13, 'name': 'Kotlin', 'extension': 'kt'}, 'mssql': {'id': 14, 'name': 'MS SQL Server', 'extension': 'sql'}, 'oraclesql': {'id': 15, 'name': 'Oracle', 'extension': 'sql'}, 'rust': {'id': 18, 'name': 'Rust', 'extension': 'rs'}, 'php': {'id': 19, 'name': 'PHP', 'extension': 'php'}, 'typescript': {'id': 20, 'name': 'TypeScript', 'extension': 'ts'}, 'racket': {'id': 21, 'name': 'Racket', 'extension': 'rkt'}, 'erlang': {'id': 22, 'name': 'Erlang', 'extension': 'erl'}, 'elixir': {'id': 23, 'name': 'Elixir', 'extension': 'ex'}, 'dart': {'id': 24, 'name': 'Dart', 'extension': 'dart'}, 'pythondata': {'id': 25, 'name': 'Pandas', 'extension': 'py'}, 'react': {'id': 26, 'name': 'React', 'extension': 'jsx'}, 'vanillajs': {'id': 27, 'name': 'Vanilla JS', 'extension': 'js'}, 'postgresql': {'id': 28, 'name': 'PostgreSQL', 'extension': 'sql'}, 'cangjie': {'id': 29, 'name': 'Cangjie', 'extension': 'cj'}}
    id_len = 1
    for lang in langs.keys():
        id_len = max(id_len, len(str(langs[lang]["id"]))) + 1
    options = {}
    question["codeSnippets"].reverse()
    for snip in question["codeSnippets"]:
        lang = snip["langSlug"]
        options[langs[lang]["id"]] = lang
        default = ""
        if lang == "python3":
            default = " (default)"
        print(f"{" "*(id_len-len(str(langs[lang]["id"])))}{langs[lang]["id"]}. {langs[lang]["name"]}{default}")
    print("Give the Language choices as numbers saperated by commas ','.")
    choices = set()
    while True:
        try:
            choice = input("> ")
            if choice == "":
                choices.add("python3")
                break
            choice = choice.split(",")
            choice = list(map(int, choice))
            invalid = False
            for c in choice:
                lang = options.get(c, None)
                if lang:
                    choices.add(lang)
                else:
                    print(f"{c} is invalid language number. Try again.")
                    invalid = True
            if invalid:
                continue
            if len(choices) > 0:
                break
            print("Give atleast one valid language number.")
        except ValueError:
            print("Invalid input. Give the numbers next to the languages of choice saperated by comma ','.")
        except KeyboardInterrupt:
            sys.exit("\nExiting...")
    for snip in question["codeSnippets"]:
        if snip["langSlug"] in choices:
            file_name = f"solution_{snip["lang"]}.{langs[snip["langSlug"]]["extension"]}"
            write_file(problem_dir, file_name, snip["code"])


def create_input(problem_dir, question):
    metadata = json.loads(question["metaData"])
    input_json = {}
    input_json["call"] = "class"
    input_json["name"] = metadata.get("classname", "Solution")
    input_json["method"] = metadata.get("name", "")
    input_json["order"] = ""
    input_string = "{\n"
    for key in ["call", "name", "method", "order"]:
        input_string += f'{" "*4}"{key}": "{input_json[key]}",\n'
    if question["exampleTestcaseList"]:
        input_string += f'{" "*4}"testcases": [\n'
        for c, case in enumerate(question["exampleTestcaseList"], start=1):
            input_string += f'{" "*8}{{"case": {c}, "input": '
            if "params" in metadata:
                input_string += "{"
                case = case.split("\n")
                for i in range(len(metadata["params"])):
                    input_string += f'"{metadata["params"][i]["name"]}": {case[i]}, '
                input_string = input_string[:-2]
                input_string += "}"
            else:
                case = case.split("\n")
                if len(case) == 1:
                    input_string += case[0]
                else:
                    input_string += "["
                    for line in case:
                        input_string += "[" + str(line)[1:-1] + "]" + ", "
                    input_string = input_string[:-2]
                    input_string += "]"
            input_string += ', "expected": },\n'
        input_string = input_string[:-2]
        input_string += f"\n{" "*4}]\n"
    input_string += "}"
    file_name = "input.json"
    write_file(problem_dir, file_name, input_string)


def create_readme(problem_dir, question):
    content = question["content"]
    md = html_md(content)
    md = "TEST"
    write_file(problem_dir, "README.md", md)


def write_file(problem_dir, file_name, content):
    file = problem_dir / file_name
    if file.is_file():
        if file.stat().st_size != 0 and not overwrite(file):
            print(f"Writing to {file.name} skipped.")
            return
    else:
        file.touch()
        print(f"Created {file.name}")
    with open(file, "w") as f:
        f.write(content)


def overwrite(file):
    while True:
        try:
            confirmation = input(f"Do You want to overwrite {file.name}? [y/N]: ").lower()
            if confirmation in ["n", "no", ""]:
                return None
            elif confirmation in ["y", "yes"]:
                return file
        except KeyboardInterrupt:
            sys.exit("\nExiting...")


def html_md(html):
    pass


if "__main__" == __name__:
    main()
