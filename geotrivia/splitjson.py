import json

# Load the JSON data from the file
with open('geotrivia/outputlist2.json', 'r', encoding = 'utf-8') as file:
    data = json.load(file)

# Function to split the list into chunks of size x
def split_into_chunks(data, x):
    return [data[i:i + x] for i in range(0, len(data), x)]

# Define the size of each chunk
x = 5  # Set the number of question-answer pairs per file

# Split the data into chunks
chunks = split_into_chunks(data, 50)

# Save each chunk into a separate file
for idx, chunk in enumerate(chunks):
    filename = f'group_{idx + 1}.json'
    with open(f"geotrivia/groups/{filename}", 'w') as outfile:
        json.dump(chunk, outfile, indent=4)
    print(f'Saved {filename}')

