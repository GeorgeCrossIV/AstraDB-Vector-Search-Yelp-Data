# Get the count of the yelp.review table in Astra via the dsbulk tool

username=<username goes here>
password=<password goes here>
secureconnectbundle=/home/gcross/secure-connect-cassio-db.zip

dsbulk count -k yelp -t review -b $secureconnectbundle -u $username -p $password