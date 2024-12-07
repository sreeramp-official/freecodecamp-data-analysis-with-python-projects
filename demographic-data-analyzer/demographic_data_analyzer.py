import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file with proper column names
    df = pd.read_csv(
        "demographic-data-analyzer/adult.data.csv",
        header=None,
        names=[
            "age",
            "workclass",
            "fnlwgt",
            "education",
            "education-num",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital-gain",
            "capital-loss",
            "hours-per-week",
            "native-country",
            "salary",
        ],
    )

    # Ensure proper data types
    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["hours-per-week"] = pd.to_numeric(df["hours-per-week"], errors="coerce")

    # Drop rows with invalid or missing critical data
    df.dropna(subset=["age", "hours-per-week"], inplace=True)

    # Race count
    race_count = df["race"].value_counts()

    # Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # Percentage of people with Bachelor's degree
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # Higher and lower education filters
    higher_education = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_education = ~higher_education

    # Percentage of people with advanced education earning >50K
    higher_education_rich = round(
        (
            df[higher_education & (df["salary"] == ">50K")].shape[0]
            / df[higher_education].shape[0]
        )
        * 100,
        1,
    )

    # Percentage of people without advanced education earning >50K
    lower_education_rich = round(
        (
            df[lower_education & (df["salary"] == ">50K")].shape[0]
            / df[lower_education].shape[0]
        )
        * 100,
        1,
    )

    # Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # Percentage of people working minimum hours per week earning >50K
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    if num_min_workers.shape[0] > 0:
        rich_percentage = round(
            (
                num_min_workers[num_min_workers["salary"] == ">50K"].shape[0]
                / num_min_workers.shape[0]
            )
            * 100,
            1,
        )
    else:
        rich_percentage = 0

    # Country with the highest percentage of people earning >50K
    country_counts = df["native-country"].value_counts()
    country_rich_counts = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_rich_percentages = (country_rich_counts / country_counts * 100).dropna()
    highest_earning_country = country_rich_percentages.idxmax()
    highest_earning_country_percentage = round(country_rich_percentages.max(), 1)

    # Most popular occupation for those earning >50K in India
    top_IN_occupation = df[
        (df["native-country"] == "India") & (df["salary"] == ">50K")
    ]["occupation"].mode()
    top_IN_occupation = top_IN_occupation[0] if not top_IN_occupation.empty else "N/A"

    # Print results if requested
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelor's degrees: {percentage_bachelors}%")
        print(
            f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
            f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
            f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
            f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
        print("Top occupations in India:", top_IN_occupation)

    return {
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
