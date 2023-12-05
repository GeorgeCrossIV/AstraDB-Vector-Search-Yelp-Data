#!/bin/bash

# Directory containing the folders to process
data_dir="/home/gcross/demos/yelp/upload-data"

# Iterate over each folder in the directory
for folder in "$data_dir"/*; do
    if [ -d "$folder" ]; then
        folder_name=$(basename "$folder")
        echo "Loading data from folder: $folder_name"
        ./load-yelp-data.sh "$folder_name"
    fi
done

echo "Data loading complete for all folders."