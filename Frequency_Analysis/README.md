This project was written by Adam Burke (burke.101@wright.edu) with the assitance of ChatGPT

# **Content Analysis of 10-K Reports**

This project performs **keyword frequency analysis** on a **10-K financial report** using the **Balanced Scorecard (BSC) framework**. It extracts key terms from an **MD (Markdown) file** and categorizes them into:
- **Financial Performance**
- **Customer Perspective**
- **Internal Business Processes**
- **Learning & Growth**

---

## **Project Structure**
```
│── Content_Analysis_10K.py   # Python script for content analysis
│── Example_10K.md            # Sample 10-K report in Markdown format
│── requirements.txt          # Dependencies for the project
│── README.md                 # This documentation
```

---

## **Installation Instructions**
### **1. Install Dependencies**
First, ensure you have **Python (≥ 3.7)** installed, then install required libraries:

```bash
pip install -r requirements.txt
```

**OR** manually install:
```bash
pip install pandas
```

---

## **Usage Instructions**

### **1. Get a 10-k file**
- Navigate to https://www.sec.gov
- Search for a company
- Select 10-K -> 10-K: Annual report ... 
- Copy/Paste the text into a *.md file and add it to Company_10Ks


### **1. Run the Analysis Script**
Execute the script with a **10-K Markdown file**:

```bash
python Content_Analysis_10K.py Example_10K.md
```

### **2. Output**
- The script **prints the top three keywords** in each Balanced Scorecard category.
- Remaining keywords are grouped under **"Other"**.

---

## **Example Output**
```
               Financial Performance  Customer Perspective  Internal Business Processes  Learning & Growth
revenue                        158.0                   0.0                          0.0                0.0
investment                     148.0                   0.0                          0.0                0.0
shareholder                     27.0                   0.0                          0.0                0.0
Other                           47.0                   3.0                         60.0               27.0
```
Each **Balanced Scorecard category** contains:
✅ **Top 3 most frequent words**  
✅ **All remaining words under "Other"**  

---

## **Customization**
To modify **keywords analyzed**, edit the `bsc_keywords` dictionary in **Content_Analysis_10K.py**.
