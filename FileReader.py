import pandas as pd

# Load the CSV file
file_path = '/home/nick/Documents/AEPData/CORE_HackOhio_subset_cleaned_downsampled 1.csv'
data = pd.read_csv(file_path)

# Build frequency counters for the PNT_NM and QUALIFIER_TXT columns
pnt_nm_counter = data['PNT_NM'].value_counts()
qualifier_txt_counter = data['QUALIFIER_TXT'].value_counts()

# Print the results
print("PNT_NM Frequency Counter:")
print(pnt_nm_counter)

# print("\nQUALIFIER_TXT Frequency Counter:")
# print(qualifier_txt_counter)

