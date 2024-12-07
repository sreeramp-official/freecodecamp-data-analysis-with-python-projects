
# Demographic Data Analyzer

This project involves analyzing demographic data to calculate key statistics such as age averages, education levels, income distributions, and occupations, among other factors. The analysis is performed on a dataset of adult individuals, examining various demographic aspects.


## Features

The calculate_demographic_data() function computes the following statistics for a given demographic dataset:

- **Race count:** Distribution of races in the dataset.
- **Average age of men:** The average age for male individuals.
- **Percentage with Bachelor's degrees:** Percentage of people who hold a Bachelor's degree.
- **Percentage with higher education earning >50K:** Percentage of individuals with higher education (Bachelors, Masters, Doctorate) earning more than $50,000.
- **Percentage without higher education earning >50K:** Percentage of individuals without advanced education earning more than $50,000.
- **Minimum work hours:** Minimum number of hours worked per week.
- **Percentage of rich among those who work fewest hours:** Percentage of people earning more than $50,000 who work the minimum number of hours per week.
- **Country with highest percentage of people earning >50K:** The country with the highest percentage of individuals earning more than $50,000.
- **Most popular occupation for those earning >50K in India:** The most frequent occupation in India among those earning more than $50,000.



## Usage

### Input
- The function reads data from a CSV file (`adult.data.csv`), which contains demographic information about adults.

### Output

A dictionary with the following keys and computed values:

```python
{
  "race_count": race_count,
  "average_age_men": average_age_men,
  "percentage_bachelors": percentage_bachelors,
  "higher_education_rich": higher_education_rich,
  "lower_education_rich": lower_education_rich,
  "min_work_hours": min_work_hours,
  "rich_percentage": rich_percentage,
  "highest_earning_country": highest_earning_country,
  "highest_earning_country_percentage": highest_earning_country_percentage,
  "top_IN_occupation": top_IN_occupation,
}
```



## Setup
1. Install Python if it is not already installed.
2. Install dependencies using the `requirements.txt`:
```bash
pip install -r requirements.txt
```
3. Make sure the dataset file `adult.data.csv` is available in the correct directory.
4. Run the `main.py`.


