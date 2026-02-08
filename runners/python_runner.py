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
        print(f" > {problems[p][1]}")

    choice = choose_problem(problems)
    print(f" > {choice}")

    problem_dir = problems_dir / choice

    if not (problem_dir / "input.json").exists():
        sys.exit("No input.json in the problem directory")

    with open(problem_dir / "input.json") as input_file:
        inputs = json.load(input_file)
        callable = inputs.get("call", "class")
        call_name = inputs.get("name", "Solution")
        if callable == "class":
            problem_method = inputs.get("method")
        else:
            problem_method = None
        testcases = inputs.get("testcases")

    req_module = find_module(problem_dir)

    req_call = find_call(req_module, call_name)

    req_method = None
    if callable == "class":
        req_method = find_method(req_call, problem_method)
    elif callable == "function":
        req_method = None

    testcases.sort(key=lambda t: t["case"])
    for testcase in testcases:
        if callable == "class":
            test_solution = req_call()
        elif callable == "function":
            test_solution = req_call
        case = testcase.pop("case")
        run_test(test_solution, callable, req_method, testcase, case)

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

def find_module(problem_dir):
    spec = importlib.util.spec_from_file_location("solution", problem_dir / "solution.py")
    if spec is None or spec.loader is None:
        sys.exit("Could not load module from solution.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def find_call(module, name):
    for attr_name in dir(module):
        if attr_name == name:
            attr = getattr(module, name)
            if callable(attr):
                return attr
    if hasattr(module, name):
        return getattr(module, name)
    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and not attr_name.startswith('_'):
            return attr
    sys.exit("No callable found in solution.py")

def find_method(req_call, problem_method):
    methods = []
    for method in dir(req_call):
        if not method.startswith("_") and callable(getattr(req_call, method)):
            if method == problem_method:
                return method
            methods.append(method)
    if methods:
        return methods[0]
    sys.exit("No suitable method found in Solution class")

def run_test(test, callable, class_method, testcase, case_num):
    try:
        if "input" in testcase:
            input = testcase["input"]
        elif "inputs" in testcase:
            input = testcase["inputs"]
        else:
            input = {k: v for k, v in testcase.items()
            if k not in ["expected", "output", "method", "case"]}
            
        expected = testcase.get("expected")
        if expected is None:
            expected = testcase.get("output")

        if callable == "class":
            method = getattr(test, class_method)
            if isinstance(input, dict):
                result = method(**input)
            elif isinstance(input, list):
                result = method(*input)
            else:
                result = method(input)
        elif callable == "function":
            result = test(input)
        else:
            sys.exit("Callable neither class nor function")

        if not result == expected:
            sys.exit(f"Testcase {case_num} Failed!\nExpected : {expected}\nGot      : {result}")

        return

    except Exception as e:
        sys.exit(f"Testcase {case_num} ERROR!\nError    : {str(e)}")

if "__main__" == __name__:
    main()
