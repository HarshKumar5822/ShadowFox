def format_number(value, format_type):
    result = format(value, format_type)
    return result

# Call the function with 145 and 'o'
formatted_result = format_number(145, 'o')

# Print the result
print("Formatted result:", formatted_result)
