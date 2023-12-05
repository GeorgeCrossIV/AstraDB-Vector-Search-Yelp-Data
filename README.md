# Astra DB/Vector Search with Yelp Review Data

This repository offers a comprehensive guide for embedding and querying Yelp review data using Astra DB, a vector database. It's designed to work with a large dataset of over seven million Yelp reviews, leveraging Hugging Face models for embedding and tools like dsbulk and NoSql Bench for data loading and performance testing.

## Activities Covered

### Getting Started
- Tools for using Astra DB.
- Sample Yelp review data.
- Google Colab notebook for embedding, loading, and querying data.

### Large-scale Embedding
- Embed over 7 million Yelp reviews using a Hugging Face model.
- Load data into Astra DB with the dsbulk tool.

### Performance Testing
- Employ NoSql Bench for performance metrics of the Yelp.Review table.
- Use the ANN function for querying.

## Prerequisites
- Set up an Astra DB database.
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

### Performance Testing
- `run.sh`: Runs NoSqlBench script.
- `select-reviews.yaml`: Configuration for random embeddings selection.
- `embeddings.txt`: List of embeddings for search queries.
- `convert-to-hdf5.py`: Converts embeddings to hdf5 format.
- `vectors.hdf5`: Example hdf5 file.

---

This repository is well-suited for anyone looking to work with large-scale text data in a vector database, providing an end-to-end solution from data preparation to querying and performance evaluation.
