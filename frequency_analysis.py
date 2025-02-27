import pandas as pd
import glob
import os
import re
from tabulate import tabulate

# Define Balanced Scorecard categories and keywords (Lowercase for case insensitivity)
bsc_keywords = {
    "Financial": ["shareholder", "investor", "risk", "revenue"],
    "Customers": ["customer", "consumer", "client", "services", "quality", "delivery"],
    "Internal Business": ["flexibility", "cost", "time", "improvement", "performance"],
    "Innovation and Learning": ["human capital", "employees", "workforce", "empowerment", 
                                "personnel", "education", "technology", "technologies", "AI"]
}


# Convert dictionary to list format for tabulate
bsc_table = [[category, ", ".join(keywords)] for category, keywords in bsc_keywords.items()]

# Add a title row
table_title = [["Balanced Scorecard Categories & Keywords"]]

# Print using tabulate with title
print(tabulate(table_title, tablefmt="fancy_grid"))  
print(tabulate(bsc_table, headers=["Category", "Keywords"], tablefmt="fancy_grid"))

# Initialize data storage
company_category_counts = {}
company_total_word_counts = {}

# Define the base directory where company folders are stored
base_dir = "./companies/"

# Get all company folders
company_folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))]

# Process each company folder
for company in company_folders:
    company_path = os.path.join(base_dir, company)
    md_files = glob.glob(os.path.join(company_path, "*.md"))

    total_words = 0
    category_counts = {category: 0 for category in bsc_keywords}

    # Process each Markdown file
    for md_file_path in md_files:
        with open(md_file_path, "r", encoding="utf-8") as file:
            text = file.read().lower()  # Convert text to lowercase
            total_words += len(text.split())

            # Count occurrences of keywords in each category using regex for partial matches
            for category, keywords in bsc_keywords.items():
                for keyword in keywords:
                    pattern = rf"\b{keyword}\w*\b"  # Matches keyword + possible word endings
                    category_counts[category] += len(re.findall(pattern, text))  # Count matches

    # Store aggregated results for the company
    company_total_word_counts[company] = total_words
    company_category_counts[company] = category_counts

# Convert results into a DataFrame
df = pd.DataFrame.from_dict(company_category_counts, orient="index")

# Convert raw counts into percentages of total words
df_percentage = df.div(pd.Series(company_total_word_counts), axis=0) * 100
df_percentage["Total BSC Focus"] = df_percentage.sum(axis=1)

# Format percentages
df_percentage = df_percentage.map(lambda x: f"{x:.3f}%" if pd.notna(x) else "0.000%")

# Add company names as a column instead of an index
df_percentage.insert(0, "Company/Perspective", df_percentage.index)

# Save results to CSV with proper formatting
output_csv = "company_word_frequency_analysis.csv"
df_percentage.to_csv(output_csv, index=False)

# Convert DataFrame to list format for tabulate
table_title = [["Word Frequency Analysis by Company (Percentage of Total Words)"]]
table_data = df_percentage.values.tolist()  # Convert DataFrame to list
headers = list(df_percentage.columns)  # Use DataFrame column names for headers

# Print table with title inside
print("\n")
print(tabulate(table_title, tablefmt="fancy_grid"))  
print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
