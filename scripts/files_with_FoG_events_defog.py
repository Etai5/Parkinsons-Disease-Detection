import pandas as pd
import os

# Conversion factor from g to m/s²
G_TO_MPS2 = 9.80665

# Directory containing CSV files
input_dir = r'D:\\University\\project_data_files\\defog'
output_dir = os.path.join(input_dir, 'files_with_fog_events')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Process each CSV file in the directory
for file_name in os.listdir(input_dir):
    if file_name.endswith(".csv"):  # Only process CSV files
        file_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)

        # Load the CSV file
        df = pd.read_csv(file_path)

        # Convert acceleration values to m/s²
        df[['AccV', 'AccML', 'AccAP']] = df[['AccV', 'AccML', 'AccAP']] * G_TO_MPS2

        # Remove rows where 'Valid' is False
        df_filtered = df[df['Valid'] == True].drop(columns=['Valid'])

        # Check if any of the columns have a value of 1
        if ((df_filtered['StartHesitation'] == 1).any() or 
            (df_filtered['Turn'] == 1).any() or 
            (df_filtered['Walking'] == 1).any()):
            
            # Save the processed data
            df_filtered.to_csv(output_path, index=False)
            print(f"Processed and saved: {output_path}")
        
        else:
            print(f"No relevant event in file: {file_name}")

print("All files have been processed successfully.")