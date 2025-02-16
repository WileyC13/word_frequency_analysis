import pandas as pd
import glob
import os
from tabulate import tabulate

# Define Balanced Scorecard categories and keywords
bsc_keywords = {
    "Shareholders": ["Shareholder", "Investor", "Risk"],
    "Customers": ["Customer", "Consumer", "Client", "Services", "Quality", "Delivery"],
    "Internal Processes": ["Flexibility", "Cost", "Time", "Improvement", "Performance"],
    "Human Capital": [
        "Human capital", "Employees", "Workforce", "Empowerment", 
        "Personnel", "Education", "People", "Knowledge"
    ],
    "Technology and Growth": ["Innovation", "Technology", "Growth and Learning", "Information", "Internet"],
    "International Scope": ["Global", "Multinational", "International", "Transnational", "National Culture"],
    "Others": ["Environment", "Competitors", "Alliance", "Outsourcing", "Merger", "Acquisition"]
}

# Convert dictionary to list format for tabulate
bsc_table = [[category, ", ".join(keywords)] for category, keywords in bsc_keywords.items()]

# Add a title row
table_title = [["Balanced Scorecard Categories & Keywords"]]

# Print using tabulate with title
print(tabulate(table_title, tablefmt="fancy_grid"))  # Title formatted as a table
print(tabulate(bsc_table, headers=["Category", "Keywords"], tablefmt="fancy_grid"))

# Initialize data storage
file_category_counts = {}
total_word_counts = {}

# Get all Markdown files excluding README.md
md_files = [f for f in glob.glob("./files_to_analyze/*.md") if "readme" not in f.lower()]

# Process each Markdown file
for md_file_path in md_files:
    file_name = os.path.splitext(os.path.basename(md_file_path))[0]  # Extract file name without path and extension
    
    with open(md_file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
        total_words = len(text.split())
        total_word_counts[file_name] = total_words
        
        category_counts = {category: 0 for category in bsc_keywords}
        for category, keywords in bsc_keywords.items():
            for keyword in keywords:
                category_counts[category] += text.count(keyword.lower())
        
        file_category_counts[file_name] = category_counts

# Convert results into a DataFrame
df = pd.DataFrame.from_dict(file_category_counts, orient="index")

df_percentage = df.div(pd.Series(total_word_counts), axis=0) * 100
df_percentage["Total"] = df_percentage.sum(axis=1)

# Use `map()` instead of `applymap()`
df_percentage = df_percentage.map(lambda x: f"{x:.3f}%")

# Save results to CSV
df_percentage.to_csv("word_frequency_analysis.csv")

from tabulate import tabulate

# Add a title row to the table
table_title = [["Word Frequency Analysis (Percentage of Total Words in Each File)"]]
table_data = df_percentage.reset_index().values.tolist()  # Convert DataFrame to a list
headers = ["File Name"] + list(df_percentage.columns)  # Add column headers

# Print table with title inside
print("\n")
print(tabulate(table_title, tablefmt="fancy_grid"))  # Title formatted as a table
print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
