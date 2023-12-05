# Astra DB/Vector Search with Yelp Review Data

This repository offers a comprehensive guide for embedding and querying Yelp review data using [Astra DB](https://www.datastax.com/products/datastax-astra), a vector database. It's designed to work with a large dataset of over seven million Yelp reviews, leveraging Hugging Face models for embedding and tools like dsbulk and [NoSql Bench](https://github.com/nosqlbench/nosqlbench) for data loading and performance testing.

## Activities Covered

### Getting Started
- Get started quickly by connecting to Astra DB to embed and load a subset of Yelp review data.
- Sample Yelp review data. [Yelp review data download](https://www.yelp.com/dataset).
- Google Colab notebook for embedding, loading, and querying data.

#### Steps
- Start by opening the Vector_Search_Yelp_Data.ipynb notebook.
- Click the Open in Colab button and follow the instructions in the notebook.
- Be sure to upload your secure connect bundle in Colab.

### Large-scale Embedding
- Embed over 7 million Yelp reviews using a Hugging Face model (sentence-transformers/all-MiniLM-L6-v2).
- Load data into Astra DB with the dsbulk tool.

#### Steps
- Create the .env file from the .env.sample file and update the configuration file.
- Download the Yelp review dataset.
- Run the embed.py script to embed the Yelp reviews.
- Run the move_files.py script to distribute the csv files into manageable upload chunks for the dsbulk tool.
- Run the load-all-yelp-data.sh to load the data via dsbulk.
- Note: This process is very process intensive and time consuming. 

### Performance Testing
- Employ [NoSql Bench](https://github.com/nosqlbench/nosqlbench) for performance metrics of the Yelp.Review table.
- Use the ANN function for querying.

#### Steps
- Download the sample vectors.hdf5 file.
- Run the run.sh script to start the NoSql Bench test

## Prerequisites
- Set up an [Astra DB](https://www.datastax.com/products/datastax-astra) database.
- Create a keyspace (named "yelp" in examples).
- Use the provided CQL script for creating the review table.
- Download a secure connect bundle.
- Generate an application token (record clientId and secret).
- Obtain a Hugging Face token.

## File Descriptions

### Getting Started
- `Vector_Search_Yelp_Data.ipynb`: Notebook for initial steps.
- `yelp_academic_dataset_review-short.json`: Sample Yelp review data.

### Large-scale Embedding
- `embed.py`: Script for creating embeddings.
- `move_files.py`: Organizes csv files for efficient data loading.
- `load-yelp-data.sh`: Loads csv files into Astra DB.
- `load-all-yelp-data.sh`: Bulk load script for entire dataset.
- `env.sample`: sample .env file. Save as .env

### Performance Testing
- `run.sh`: Runs NoSqlBench script.
- `select-reviews.yaml`: Configuration for random embeddings selection.
- `embeddings.txt`: List of embeddings for search queries.
- `convert-to-hdf5.py`: Converts embeddings to hdf5 format.
- `vectors.hdf5`: Example hdf5 file.

---

This repository is well-suited for anyone looking to work with large-scale text data in a vector database, providing an end-to-end solution from data preparation to querying and performance evaluation.
