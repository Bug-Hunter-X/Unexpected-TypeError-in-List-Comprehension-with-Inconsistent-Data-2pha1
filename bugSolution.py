def function_with_robust_error_handling(data):
    try:
        result = 0
        for item in data:
            if isinstance(item, dict) and 'value' in item and isinstance(item['value'], (int, float)):
                result += item['value']
            else:
                print(f"Warning: Skipping invalid item: {item}")
        return result
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
data = [{'value': 1}, {'value': 2}, {'value': 'a'}]
result = function_with_robust_error_handling(data)
print(result)  # Output: Warning: Skipping invalid item: {'value': 'a'}
              #         3

data2 = [{'value': 1}, {'value': 2}, {}]
result2 = function_with_robust_error_handling(data2)
print(result2)  # Output: Warning: Skipping invalid item: {}
              #         3