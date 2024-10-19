import pandas as pd
import re

# Function to clean text by removing articles and common meaningless words
def clean_text(text):
    if pd.isna(text):
        return text
    # List of common meaningless words (you can expand this list as needed)
    stop_words = r'\b(the|a|an|of|and|to|is|in|for|on|with|by|that|this|it|as|at|be|from|was|were|are|has|had|have|or|but|which|who)\b'
    
    # Remove stop words and extra spaces
    cleaned_text = re.sub(stop_words, '', text, flags=re.IGNORECASE)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text

# List of columns to clean
text_columns = ['PNT_NM', 'QUALIFIER_TXT', 'PNT_ATRISKNOTES_TX', 'PNT_ATRISKFOLWUPNTS_TX']

# Apply cleaning function to the relevant columns
for col in text_columns:
    data[col] = data[col].apply(clean_text)

# Save the cleaned data to a new CSV file
cleaned_file_path = '/mnt/data/cleaned_CORE_HackOhio_subset.csv'
data.to_csv(cleaned_file_path, index=False)

cleaned_file_path
