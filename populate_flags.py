import json
import requests

# Load the JSON file
with open('currencies.json') as f:
    data = json.load(f)

# Iterate over the data
for currency in data:
    code = currency['code'].lower()  # 'code' is the key for currency code

    png = "https://raw.githubusercontent.com/ericwafula/currency-flags/main/assets/flags_png_rectangle/{code}.png"
    svg = "https://raw.githubusercontent.com/ericwafula/currency-flags/6cb2908c2077a257e0aac26f13ea884d965c074a/assets/flags_svg/{code}.svg"

    pngResponse = requests.get("https://raw.githubusercontent.com/ericwafula/currency-flags/main/assets/flags_png_rectangle/{code}.png")
    svgResponse = requests.get("https://raw.githubusercontent.com/ericwafula/currency-flags/6cb2908c2077a257e0aac26f13ea884d965c074a/assets/flags_svg/{code}.svg")

    # Check if the response is successful
    if pngResponse.status_code == 404:
        png = None
    else:
        png = "https://raw.githubusercontent.com/ericwafula/currency-flags/main/assets/flags_png_rectangle/{code}.png"

    if svgResponse.status_code == 404:
        svg = None
    else:
        svg = "https://raw.githubusercontent.com/ericwafula/currency-flags/6cb2908c2077a257e0aac26f13ea884d965c074a/assets/flags_svg/{code}.svg"

    currency['flag']['png'] = f"https://raw.githubusercontent.com/ericwafula/currency-flags/main/assets/flags_png_rectangle/{code}.png"
    currency['flag']['svg'] = f"https://raw.githubusercontent.com/ericwafula/currency-flags/6cb2908c2077a257e0aac26f13ea884d965c074a/assets/flags_svg/{code}.svg"

# Save the updated data back to the JSON file
with open('currencies.json', 'w') as f:
    json.dump(data, f, indent=4)