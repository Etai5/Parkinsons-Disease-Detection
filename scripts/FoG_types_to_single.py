""" Given the data of the format of the files from kaggle, this script takes the 3 different types of
    FoG event: StartHesitation, Turn, Walking and collapse them into a single column which indicate whether
    there was a FoG event or not of any kind.
    Given the folder where the files are at, it creates inside this folder a subfolder caleed "fog" which includes all
    the files in the new format.
"""

import pandas as pd
import os
import glob

# Define the directories
input_directory = r'D:\\University\\tdcsfog'
output_directory = os.path.join(input_directory, 'fog')

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Get a list of all CSV files in the input directory
csv_files = glob.glob(os.path.join(input_directory, '*.csv'))

# Function to process each CSV file
def process_file(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Create the new column based on the OR condition of columns StartHesitation, Turn, Walking
    df['FoG'] = df.iloc[:, 4] | df.iloc[:, 5] | df.iloc[:, 6]

    # Drop columns StartHesitation, Turn, Walking
    df.drop(df.columns[[4, 5, 6]], axis=1, inplace=True)

    # Get the filename without the directory
    file_name = os.path.basename(file_path)

    # Save the modified file to the output directory with the same name
    new_file_path = os.path.join(output_directory, file_name)
    df.to_csv(new_file_path, index=False)

# Process each CSV file
for file_path in csv_files:
    process_file(file_path)

print("Processing complete.")
