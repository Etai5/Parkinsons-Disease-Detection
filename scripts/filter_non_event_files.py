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

# Function to process and copy files with at least one relevant event per label
def process_fog_files(input_directory):
    # Labels to check and create subfolders for
    labels = ['StartHesitation', 'Turn', 'Walking']
    
    # Create subdirectories for each label
    for label in labels:
        label_output_directory = os.path.join(input_directory, f'files_with_{label}_events')
        os.makedirs(label_output_directory, exist_ok=True)

    # Get a list of all CSV files in the input directory
    csv_files = glob.glob(os.path.join(input_directory, '*.csv'))

    # Process each CSV file
    for file_path in csv_files:
        try:
            # Read the CSV file
            df = pd.read_csv(file_path)

            # Get the filename without the directory
            file_name = os.path.basename(file_path)

            # Check each label column and copy the file to the respective folder if it contains an event
            for label in labels:
                if (df[label] == 1).any():
                    label_output_directory = os.path.join(input_directory, f'files_with_{label}_events')
                    new_file_path = os.path.join(label_output_directory, file_name)
                    shutil.copy(file_path, new_file_path)
                    print(f"Copied file: {file_name} to folder for {label} events")
        
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")

    print("Processing complete.")

# Set your input directory here
input_directory = r'D:\\University\\tdcsfog'

process_fog_files(input_directory)
