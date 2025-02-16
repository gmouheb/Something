import json

def get_all_keys(obj, prefix="", result=None):
    """
    Extract all keys from a JSON structure into a flat list
    
    Args:
        obj: The JSON object
        prefix: Current key path
        result: List to collect keys
    
    Returns:
        List of all keys with their full paths
    """
    if result is None:
        result = []
    
    if isinstance(obj, dict):
        for key, value in obj.items():
            current_key = f"{prefix}.{key}" if prefix else key
            result.append(current_key)
            get_all_keys(value, current_key, result)
    
    elif isinstance(obj, list) and obj:
        # For lists, we add just the first item's structure as example
        get_all_keys(obj[0], f"{prefix}[0]", result)
    
    return result

# Specific file to read
filename = "outputNew.json"

try:
    # Open and read the JSON file
    with open(filename, 'r') as f:
        data = json.load(f)
    
    # Get all keys
    keys = get_all_keys(data)
    
    # Print the keys
    print(f"Found {len(keys)} keys in '{filename}':")
    for i, key in enumerate(keys, 1):
        print(f"{i}. {key}")
        
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except json.JSONDecodeError:
    print(f"Error: '{filename}' is not a valid JSON file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")