import pandas as pd
import datetime


def calculate_total_age_for_date(date, data):
    # Filter items that are in progress on the given date
    in_progress = data[(data['Started'] <= date) & ((data['Done'].isna()) | (data['Done'] > date))]
    # Calculate age for each item and sum up, adding 1 to each to account for the start day but not including the 'Done' date
    total_age = ((date - in_progress['Started']).dt.days + 1).sum()
    return total_age

def main():
    # Specify the file path
    file_path = '/Users/troy.lightfoot/Documents/wiaXMR.xlsx'

    # Load the specific sheet you want to update
    sheet_name = 'Data'
    data = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

    # Check if 'Started' column exists
    if 'Started' not in data.columns:
        raise ValueError("Column 'Started' not found in the 'Data' sheet")

    # Create a date range
    start_date = data['Started'].min()
    end_date = data['Done'].max()
    date_range = pd.date_range(start=start_date, end=end_date)

    # Convert the 'Date' column to datetime if it's not already
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

    # Format the 'Date' column to display only year-month-day
    data['Date'] = data['Date'].dt.strftime('%Y-%m-%d')

    # Calculate total age for each date and update the DataFrame
    for date in date_range:
        total_age = calculate_total_age_for_date(date, data)

        # Update the 'Total Age' column for rows where 'Date' matches the current date
        data.loc[data['Date'] == date.strftime('%Y-%m-%d'), 'Total Age'] = total_age

    # Save the updated DataFrame to Excel
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        data.to_excel(writer, sheet_name=sheet_name, index=False)

    print("The file has been updated and saved as", file_path)

if __name__ == "__main__":
    main()
