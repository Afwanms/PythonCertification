def add_setting(dictionary, setting):
    key = str(setting[0]).lower()
    value = str(setting[1]).lower()
    
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else: 
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, setting):
    key = str(setting[0]).lower()
    value = str(setting[1]).lower()
    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, setting):
    key = str(setting).lower()
    if key in dictionary:
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else: 
        return f'Setting not found!'

def view_settings(dictionary):  
    if not dictionary:
        return "No settings available."
    lines = ["Current User Settings:"]
    for key, value in dictionary.items():
        lines.append(f"{str(key).capitalize()}: {value}")
    return "\n".join(lines) + "\n"

test_settings = {
    'theme' : 'dark',
    'volume': 'low'
}

# Example usage:
print(add_setting(test_settings, ('language', 'english')))
print(update_setting(test_settings, ('volume', 'high')))
print(delete_setting(test_settings, 'theme'))