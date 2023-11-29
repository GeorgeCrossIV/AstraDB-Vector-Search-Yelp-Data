# AstraDB-Vector-Search-Yelp-Data
Notebook that provides an example of loading and embedding Yelp review data into Astra DB Vector Search database

## Run performance tests against the yelp.review table via NoSqlBench
Required files:
- run.sh -> a script that runs the NoSqlBench script
- select-reviews.yaml -> a YAML file that contains the script and configuration to select random embeddings in the yelp.review table
- embeddings.txxt -> a file of embeddings. The script will randomly pull embeddings to search against
