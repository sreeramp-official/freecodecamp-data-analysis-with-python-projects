
# Medical Examination Data Visualization

This project visualizes and performs calculations on medical examination data using pandas, matplotlib, and seaborn. The dataset contains information from medical exams and includes various patient characteristics, test results, and lifestyle choices.



## Dataset Description

The dataset consists of the following columns:
- **Age**: Patient's age (in days)
- **Height**: Patient's height (in cm)
- **Weight**: Patient's weight (in kg)
- **Gender**: Gender of the patient (categorical)
- **Systolic blood pressure**: Systolic blood pressure (mm Hg)
- **Diastolic blood pressure**: Diastolic blood pressure (mm Hg)
- **Cholesterol**: Cholesterol level (1: normal, 2: above normal, 3: well above normal)
- **Glucose**: Glucose level (1: normal, 2: above normal, 3: well above normal)
- **Smoking**: Whether the patient smokes (binary)
- **Alcohol intake**: Whether the patient consumes alcohol (binary)
- **Physical activity**: Whether the patient is physically active (binary)
- **Cardiovascular disease**: Target variable indicating the presence or absence of cardiovascular disease (binary)
## Features

- **Overweight Column**: Added to the dataset by calculating the Body Mass Index (BMI) from weight and height. A BMI > 25 is considered overweight.
- **Normalization**: Cholesterol and Glucose values are normalized (1 = normal, 2 or 3 = abnormal).
- **Visualization**:
  - **Categorical Plot**: A count plot visualizing features like cholesterol, glucose, smoking, alcohol intake, physical activity, and overweight status, split by whether the patient has cardiovascular disease.
  - **Heat Map**: A heat map showing the correlation matrix of the dataset with cleaned data.



## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
    ```bash
    pip install pandas seaborn matplotlib
    ```
    
## Usage

Run `main.py`

This will generate:

- `catplot.png`: The categorical plot showing the counts of various features by cardiovascular disease status.
- `heatmap.png`: The heat map showing correlations between numerical features in the dataset.

