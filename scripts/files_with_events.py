""" Given data which have the 3 label columns:"StartHesitation","Turn","Walking" label columns,
    this script run over all the files and filter
    out the files which doesnt have any FoG event at all inside their data.
    Given the folder of the output of the script: "FoG_types_to_single.py", it creates inside this folder
    a subfolder called "files_with_events" which includes only the files which has at least one FoG event.
"""

import os
import glob
import shutil
import pandas as pd

# Function to process and copy files with at least one relevant event
def process_fog_files(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Get a list of all CSV files in the input directory
    csv_files = glob.glob(os.path.join(input_directory, '*.csv'))

    # Function to process each CSV file
    for file_path in csv_files:
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)

            # Check if any of the columns have a value of 1
            if ((df['StartHesitation'] == 1).any() or 
                (df['Turn'] == 1).any() or 
                (df['Walking'] == 1).any()):
                # Get the filename without the directory
                file_name = os.path.basename(file_path)

                # Copy the file to the output directory with the same name
                new_file_path = os.path.join(output_directory, file_name)
                shutil.copy(file_path, new_file_path)
                print(f"Copied file: {file_name}")
            else:
                print(f"No relevant event in file: {file_name}")
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    print("Processing complete.")

# Set your input and output directories here
input_directory = r'D:\\University\\tdcsfog'
output_directory = os.path.join(input_directory, 'files_with_fog_events')

process_fog_files(input_directory, output_directory)
