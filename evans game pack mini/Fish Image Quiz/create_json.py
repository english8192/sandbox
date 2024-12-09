import os
import json

# Get the current directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Path to the images folder relative to the script
images_folder = os.path.join(script_dir, 'images')

# List to store the JSON data
data = []

# Loop through all jpg files in the folder
for filename in os.listdir(images_folder):
    if filename.endswith('.jpg'):
        # Extract the answer from the filename (before the underscore)
        answer = filename.split('_')[0]
        
        # Construct the JSON object
        data.append({
            "question": "",
            "answer": answer,
            "image": os.path.join('images', filename)  # Relative path to image
        })

# Write the data to a JSON file
output_path = os.path.join(script_dir, 'quiz_data.json')
with open(output_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file created successfully at", output_path)
