# I used AI to create how the code is outputted (I am not responsible for any misuse of this code).
import os
import json

IP = input("Enter the Target's IP: ")
data = os.popen(f"curl -s https://ipinfo.io/{IP}/json").read()

#importing the data as json strings to control it
json_data = json.loads(data)
# Delete the 'readme' and 'anycast' keys if they exist
json_data.pop('readme', None)  # Remove 'readme' if it exists
json_data.pop('anycast', None)  # Remove 'anycast' if it exists

# Rename 'loc' to 'location'
if 'loc' in json_data:
    json_data['location'] = json_data.pop('loc')

# Print the modified data without braces
for key, value in json_data.items():
    print(f"{key}: {value}")

input("\nPress Enter to exit...")
