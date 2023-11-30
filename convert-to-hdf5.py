## This is to help convert a csv of vector embeddings to an hdf5 file ##

import pandas as pd
import h5py

# Replace these with your CSV and HDF5 file paths
csv_file_path = 'embeddings.txt'
hdf5_file_path = 'vectors.hdf5'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Extract the vectors as a NumPy array
vectors = df.values

# Create an HDF5 file and write the vectors to it
with h5py.File(hdf5_file_path, 'w') as hdf5_file:
    hdf5_file.create_dataset('vectors', data=vectors)

print(f"CSV file '{csv_file_path}' converted to HDF5 file '{hdf5_file_path}'.")