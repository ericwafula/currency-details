import json

# Load the JSON file
with open('currencies.json') as f:
    data = json.load(f)

# Iterate over the data
for currency in data:
    # Check if the 'png' key exists in the 'flag' object
    if 'png' in currency['flag']:
        # Replace 'flag_png' with 'flags_png' in the URL
        currency['flag']['png'] = currency['flag']['png'].replace('flag_png', 'flags_png')

# Save the updated data back to the JSON file
with open('currencies.json', 'w') as f:
    json.dump(data, f, indent=4)