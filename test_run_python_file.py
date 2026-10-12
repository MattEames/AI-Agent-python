from functions.run_python_file import run_python_file

print("--- Test 1: main.py ---")
print(run_python_file("calculator", "main.py"))

print("\n--- Test 2: main.py with args ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\n--- Test 3: tests.py ---")
print(run_python_file("calculator", "tests.py"))

print("\n--- Test 4: ../main.py ---")
print(run_python_file("calculator", "../main.py"))

print("\n--- Test 5: nonexistent.py ---")
print(run_python_file("calculator", "nonexistent.py"))

print("\n--- Test 6: lorem.txt ---")
print(run_python_file("calculator", "lorem.txt"))
