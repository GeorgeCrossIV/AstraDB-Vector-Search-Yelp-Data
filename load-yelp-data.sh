# Load data into Astra via the dsbulk tool
#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <folder-name>"
    exit 1
fi

# Extract the folder name from the arguments
folder_name="$1"
username=<insert Astra DB clientId here>
password=<insert Astra DB secret here>
secureconnectbundle=/home/gcross/secure-connect-cassio-db.zip
url=/home/gcross/demos/yelp/upload-data/$folder_name # path to csv files. 

dsbulk load -k yelp -t review -b $secureconnectbundle -u $username -p $password -header true -url $url  --dsbulk.connector.c
sv.maxCharsPerColumn 9000 --codec.timestamp "yyyy-MM-dd HH:mm:ss"