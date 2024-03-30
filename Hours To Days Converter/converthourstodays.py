import pandas as pd
from datetime import datetime, timedelta
import sys

def convert_timestamps(excel_path, output_path):
    # Read the Excel file
    df = pd.read_excel(excel_path)

    # Define the starting base date
    base_date = datetime(2010, 1, 1)

    # Select all columns starting from the third one, assuming the first two are not date-related
    timestamp_columns = df.columns[2:]  # This will include all columns from the third to the last

    # Determine the earliest timestamp across all timestamp columns
    earliest_time = df[timestamp_columns].apply(pd.to_datetime, errors='coerce').min().min()

    # Function to convert timestamps to fake dates
    def hours_to_days(timestamp, earliest_time, base_date):
        # Skip rows where timestamp is NaT or None
        if pd.isnull(timestamp):
            return timestamp
        # Calculate the difference in hours from the earliest timestamp
        hour_difference = int((timestamp - earliest_time).total_seconds() / 3600)
        # Add the difference as days to the base date
        fake_date = base_date + timedelta(days=hour_difference)
        return fake_date

    # Apply the conversion function to each timestamp column
    for col in timestamp_columns:
        df[col] = df[col].apply(pd.to_datetime, errors='coerce')  # ensure the data is in datetime format
        df[col] = df[col].apply(lambda x: hours_to_days(x, earliest_time, base_date))

    # Save the modified dataframe to a new Excel file
    df.to_excel(output_path, index=False)
    print(f'The file has been processed and saved as: {output_path}')



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_timestamps.py <input_excel_path> <output_excel_path>")
    else:
        input_excel_path = sys.argv[1]
        output_excel_path = sys.argv[2]
        convert_timestamps(input_excel_path, output_excel_path)
