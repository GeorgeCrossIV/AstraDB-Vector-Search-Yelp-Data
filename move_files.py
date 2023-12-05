# Moves files from the review.csv folder and distributes them to subfolders in the upload-data folder that
#  contain 1,000 files each
import os
import shutil

source_dir = '/home/gcross/demos/yelp/review.csv'  # Replace with the path to your source directory
batch_size = 100
batch_number = 1

files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
files.sort()  # Optional, sort files if needed

while files:
    batch_files = files[:batch_size]
    files = files[batch_size:]

    # Use the older string formatting method
    dest_dir = '/home/gcross/demos/yelp/upload-data/review-{}.csv'.format(batch_number)  # Destination directory
    os.makedirs(dest_dir, exist_ok=True)

    for file in batch_files:
        shutil.move(os.path.join(source_dir, file), os.path.join(dest_dir, file))

    batch_number += 1

print("Files moved successfully.")