# Creates CSV files that contain 1,000 embeddings each in a folder named Review.csv
import os
import logging
import torch
from decouple import config

from transformers import AutoTokenizer, AutoModel, tokenization_utils
import pandas as pd

#configure logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# keys and tokens here
token = config('token') # hugging face token
data_directory=config('data_directory')
review_data_file = "yelp_academic_dataset_review.json"

# Function to get embedding from a model and tokenizer
def get_embedding(text, model, tokenizer):
    # Tokenize input text
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")

    # Get model output
    with torch.no_grad():
        outputs = model(**inputs)

    # Get the embeddings from the last hidden state
    # You might also consider using pooled output for sentence-level embeddings
    embeddings = outputs.last_hidden_state.mean(dim=1)

    # Convert the tensor embeddings into a flat list of floats
    float_embeddings = embeddings.numpy().flatten().tolist()
    float_embeddings = [round(num, 8) for num in float_embeddings]

    return float_embeddings
    
def load_yelp_review_data():
    """
    Load Yelp data from a JSON file into a pandas DataFrame.
    """
    chunk_size = 1000
    file_path = 'yelp_academic_dataset_review.json'
 
    logging.info('Loading data ...')  
       
    chunk_number = 0 # initialize chunk number
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunk_size):
        chunk_number += 1
        #create_embeddings(chunk, chunk_number)
        process_chunk(chunk, chunk_number)
            
    logging.info('Finished loading data')
       
def process_chunk(chunk, chunk_number):
    logging.info(f'Process chunk: {chunk_number}')
    # Update the 'minilm_description_embedding' field for each row
    chunk['minilm_description_embedding'] = chunk['text'].apply(lambda x: get_embedding(x, model, tokenizer))
    chunk['text'] = chunk['text'].str.replace('"',"'", regex=False)  # remove the double quotes

    # Reorder the columns
    columns_order = [
        'review_id', 'business_id', 'cool', 'date', 'funny',
        'minilm_description_embedding', 'stars', 'text', 'useful', 'user_id'
    ]
    chunk = chunk[columns_order]
    
    # Write the updated chunk to a CSV file
    output_file = os.path.join(data_directory,f'output_chunk_{chunk_number}.csv')
    chunk.to_csv(output_file, index=False)
    #chunk.to_csv(output_file, sep='|', index=False)
    logging.info(f"Chunk {chunk_number} written to {output_file}")
        
# Load pretrained MiniLM model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2", token=token)
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2", token=token)

load_yelp_review_data()

