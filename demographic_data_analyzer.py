import pandas as pd
def demographic_data_analyzer():
    df = pd.read_csv("adult.data.csv")  # ensure the CSV path is correct

    columns = [
    "age", "workclass", "fnlwgt", "education", "education-num",
    "marital-status", "occupation", "relationship", "race", "sex",
    "capital-gain", "capital-loss", "hours-per-week", "native-country", "salary"
     ]

    df = pd.read_csv("adult.data.csv", names=columns, skipinitialspace=True)
    
    race_count = df['race'].value_counts()

    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)

    higher_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_edu = ~higher_edu

    higher_edu_rich = round((df[higher_edu]['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((df[lower_edu]['salary'] == '>50K').mean() * 100, 1)

    min_work_hours = df['hours-per-week'].min()

    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = round((num_min_workers['salary'] == '>50K').mean() * 100, 1)

    country_salary_ratio = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts()
    highest_earning_country = country_salary_ratio.idxmax()
    highest_earning_country_percentage = round(country_salary_ratio.max() * 100, 1)

    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


print(demographic_data_analyzer())