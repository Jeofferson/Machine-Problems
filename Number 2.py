input_string = original_input_string = input("Input string: ")
substring_to_search = input("Substring to search: ")

input_string_length = 0
for i in input_string:
    input_string_length += 1

substring_to_search_length = 0
for i in substring_to_search:
    substring_to_search_length += 1

for i in range(input_string_length - substring_to_search_length, -1, -1):
    if original_input_string[i:i + substring_to_search_length] == substring_to_search:
        print("Output:", i)
        break
