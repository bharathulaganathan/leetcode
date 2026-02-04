from pathlib import Path
import sys
import importlib.util
import json

def main():
    current_dir = Path(__file__).resolve()
    problems_dir = current_dir.parent.parent / "problems"

    problems = []
    for problem in problems_dir.iterdir():
        if problem.is_dir():
            solution = problem / "solution.py"
            if solution.exists():
                mod_time = solution.stat().st_mtime
                problems.append((mod_time, problem.name))

    if not problems:
        sys.exit('No problem available in "problems" directory with solution.py')

    problems.sort(key=lambda x: x[0], reverse=True)

    print("Recently modified problems:")
    for p in range(min(3, len(problems))):
        print(problems[p][1])

    choice = choose_problem(problems)
    print(choice)

    problem_dir = problems_dir / choice

    solution_module = find_solution_module(problem_dir)

    solution_class = find_solution_class(solution_module)

    if not (problem_dir / "input.json").exists():
        sys.exit("No input.json in the problem directory")

    with open(problem_dir / "input.json") as input_file:
        inputs = json.load(input_file)
        input_method = inputs.get("method")
        testcases = inputs.get("testcases")

    solution_method = find_solution_method(solution_class, input_method)

    testcases.sort(key=lambda t: t["case"])
    for testcase in testcases:
        test_solution = solution_class()
        case = testcase.pop("case")
        run_test(test_solution, solution_method, testcase, case)

    print("All testcases Passed!")


def choose_problem(problems):
    while True:
        try:
            problem_number = input("Give a problem number or press 'Enter' for the latest problem: ")
            if problem_number == "":
                return problems[0][1]
            problem_number = int(problem_number)
            found = False
            for problem in problems:
                if int(problem[1].split(".")[0]) == problem_number:
                    return problem[1]
            print("No solution.py exists for the given problem number.")
        except ValueError:
            print("Problem number should be an integer.")
        except KeyboardInterrupt:
            sys.exit("")

def find_solution_module(problem_dir):
    spec = importlib.util.spec_from_file_location("solution", problem_dir / "solution.py")
    if spec is None or spec.loader is None:
        sys.exit("Could not load module from solution.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def find_solution_class(module):
    if hasattr(module, "Solution"):
        return module.Solution
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and not attr_name.startswith('_'):
            return attr
    sys.exit("No Solution class found in solution.py")

def find_solution_method(solution_class, input_method):
    methods = []
    for method in dir(solution_class):
        if not method.startswith("_") and callable(getattr(solution_class, method)):
            if method == input_method:
                return method
            methods.append(method)
    if methods:
        return methods[0]
    sys.exit("No suitable method found in Solution class")

def run_test(test_solution, solution_method, testcase, case):
    try:
        if "input" in testcase:
            inputs = testcase["input"]
        elif "inputs" in testcase:
            inputs = testcase["inputs"]
        else:
            inputs = {k: v for k, v in testcase.items()
            if k not in ["expected", "output", "method", "case"]}

        expected = testcase.get("expected") or testcase.get("output")

        method = getattr(test_solution, solution_method)

        if isinstance(inputs, dict):
            result = method(**inputs)
        elif isinstance(inputs, list):
            result = method(*inputs)
        else:
            result = method(input)

        if not result == expected:
            sys.exit(f"Testcase {case} Failed!\nExpected : {expected}\nGot      : {result}")

        return

    except Exception as e:
        print(f"Testcase {case} ERROR!")
        print(f"Error: {str(e)}")
        sys.exit("")

if "__main__" == __name__:
    main()
