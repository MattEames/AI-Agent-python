from functions.get_file_content import get_file_content

# 1. Test lorem.txt truncation
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

# 2. Test small files and error cases
print("\nmain.py:")
print(get_file_content("calculator", "main.py"))

print("\npkg/calculator.py:")
print(get_file_content("calculator", "pkg/calculator.py"))

print("\n/bin/cat:")
print(get_file_content("calculator", "/bin/cat"))

print("\npkg/does_not_exist.py:")
print(get_file_content("calculator", "pkg/does_not_exist.py"))
