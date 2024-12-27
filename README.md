
## Table of Contents
1. [Project Overview](#project-overview)
2. [Objectives](#objectives)
3. [Key Features](#key-features)
4. [Step-by-Step Process](#step-by-step-process)
5. [Usage Example](#usage-example)
6. [Project Requirements](#project-requirements)
7. [Conclusion](#conclusion)


## Project Overview
Data cleaning is a critical step in any data analysis or machine learning project. The **Data Cleaning App** provides an efficient and user-friendly way to clean datasets, saving you time and effort. Built with Python and leveraging popular libraries like Pandas, this tool is perfect for data professionals, analysts, and enthusiasts.

The app supports CSV and Excel files, removes duplicate records, handles missing values, and exports cleaned data to a new file. It also includes interactive prompts and simulated processing delays for a more realistic user experience.

## Objectives
The primary objectives of the **Data Cleaning App** are:
- **Automate Data Cleaning**: Simplify the process of cleaning datasets by automating common tasks.
- **Handle Duplicates**: Identify and remove duplicate records, saving them for review if needed.
- **Manage Missing Values**: Fill missing values in numeric columns and drop rows with missing values in non-numeric columns.
- **User-Friendly Interface**: Provide an interactive and intuitive experience for users.
- **Export Cleaned Data**: Save the cleaned dataset to a new file for further analysis or use.

## Key Features
- **Supports Multiple File Formats**: Works with CSV and Excel files.
- **Duplicate Removal**: Identifies and removes duplicate records, saving duplicates to a separate file for review.
- **Missing Value Handling**: Automatically fills missing values in numeric columns (mean, median, or mode) and drops rows with missing values in non-numeric columns.
- **Interactive Prompts**: Guides users through the cleaning process with clear instructions.
- **Random Delays**: Simulates processing time for a more realistic experience.
- **Export Cleaned Data**: Saves the cleaned dataset to a new file for further use.

## Step-by-Step Process
The **Data Cleaning App** follows these steps to clean a dataset:

1. **Input Dataset Details**:
   - The user provides the path to the dataset and a preferred name for the output files.

2. **File Validation**:
   - The app checks if the file path exists and validates the file type (CSV or Excel).

3. **Read Dataset**:
   - The dataset is read into a Pandas DataFrame.

4. **Check Duplicates**:
   - Duplicate records are identified and saved to a separate file (`<data_name>_duplicates.csv`).

5. **Remove Duplicates**:
   - Duplicate records are removed from the dataset.

6. **Check Missing Values**:
   - Missing values are identified and summarized by column.

7. **Handle Missing Values**:
   - For numeric columns, missing values are filled with the mean, median, or mode.
   - For non-numeric columns, rows with missing values are dropped.

8. **Export Cleaned Data**:
   - The cleaned dataset is saved to a new file (`<data_name>_clean_data.csv`).

9. **Completion**:
   - The app displays a summary of the cleaned dataset and notifies the user that the process is complete.
  
## Usage Example
1. Run the application using a Python environment.
2. Input the dataset path and name when prompted.
3. The application will automatically clean the dataset and save the results.

```terminal
Welcome to Data Cleaning Master!
Please enter dataset path: /usr/Dekstop/amazon.csv
Please enter dataset name: amazon_sales_data
```

4. Example of output

```terminal
Welcome to Data Cleaning App!
Please enter dataset path: data/Walmart.csv
Please enter dataset name (your preference name): walmart_cleaned
Thank you for giving the details.
Please wait for 3 seconds! Checking file path.
Dataset is CSV!
Please wait for 2 seconds! Checking total rows and columns.
Dataset contains total rows: 1000, Total columns: 10
Please wait for 4 seconds! Checking for duplicates.
Dataset has total duplicate records: 50
Please wait for 3 seconds! Saving duplicate rows.
Please wait for 5 seconds! Checking for missing values.
Dataset has total missing records: 20
Missing values by column:
Column1    0
Column2    5
...
Please wait for 4 seconds! Cleaning dataset.
Congratulations! Dataset is cleaned!
Number of rows: 950, Number of columns: 10
Dataset is saved!
```

5. Expected output
- Duplicated records saved as: `walmart_2024_duplicate.csv`
- CLeaned data saved as: `walmart_2024_cleaned.csv`

## Project Requirements
- **Python:** Core programming language.
- **Pandas:** Data manipulation and analysis.
- **NumPy:** Numerical operations.
- **Openpyxl & xlrd:** Excel file handling.
- **OS Module:** File path validation.

## Conclusion
The Data Cleaning Master simplifies the data preparation process by automating essential cleaning tasks. With features like duplicate removal, missing value handling, and seamless file export, it ensures datasets are ready for analysis or modeling. This tool is a reliable solution for improving data quality and efficiency in any data-driven workflow.
