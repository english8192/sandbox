import os

# Directory containing the files
directory = "random/y"

# Prefix to remove
prefix = "[SPOTIFY-DOWNLOADER.COM] "

# Loop through all files in the directory
for filename in os.listdir(directory):
    # Check if the filename starts with the specified prefix
    if filename.startswith(prefix):
        # Create the new filename by removing the prefix
        new_filename = filename[len(prefix):]
        # Get full paths
        old_filepath = os.path.join(directory, filename)
        new_filepath = os.path.join(directory, new_filename)
        # Rename the file
        os.rename(old_filepath, new_filepath)
        print(f'Renamed: {filename} -> {new_filename}')

print("Renaming completed!")
