input_string = input("Input string: ")
substring_to_remove = input("Substring to remove: ")

output_string = ""

substring_to_remove_length = 0
for i in substring_to_remove:
    substring_to_remove_length += 1

should_repeat = True

while should_repeat:
    should_repeat = False

    original_input_string = input_string
    input_string_length = 0
    for i in input_string:
        input_string_length += 1
    
    index_where_they_matched = 0

    for i in range(0, input_string_length - (substring_to_remove_length - 1)):
        if input_string[0:substring_to_remove_length] == substring_to_remove:
            should_repeat = True
            index_where_they_matched = i
            break
        
        input_string = input_string[1:]

    if not should_repeat:
        input_string = original_input_string
        break
    else:
        first_part = original_input_string[0:index_where_they_matched]
        last_part = original_input_string[index_where_they_matched + substring_to_remove_length:]
        output_string = first_part + last_part
        input_string = output_string

print("Output:", input_string)
