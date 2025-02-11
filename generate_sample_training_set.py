"""
Since there's not enough time to scrape or collect real training data during the hackathon we decided to create
a simulation of a machine learning model, i.e. train it on fake data (but still trying to be as close as possible
to reality based on data we scraped in a short amount of time) and include it in the pipeline of the product
we're going to pitch at the hackathon.

Here's what we did to generate the data to train the model:
1. Scraped real data from payscale with median entry salaries by university and degree
   that is available in median_entry_salary_by_degree.csv
2. Generated a random set of other features that we could potentially use
3. Generated a random set of 'true' entry salaries based on the median entry salaries from payscale (in production
   we'd have to collect real data from sources like paysa, our users or other)
"""

import random
from datetime import datetime
import numpy, time
import numpy
import pandas as pd
from collections import defaultdict


def generate_sample_entry_salary(median_salary):
    """Generates sample entry level salaries based on the true median salaries after graduating
       from a particular university and degree / main course. The way we generate that data is by
       picking a random percent between 0.1 and 10 and randomly choosing whether to decrease
       or increase the median salary by it to arrive at the randomized simulated entry level salary"""

    random.seed(datetime.now())
    random_percent_to_change_by = random.uniform(0.001, 0.15)
    increase = random.uniform(0, 1) >= 0.5

    if increase:
        sample_entry_salary = median_salary + median_salary * random_percent_to_change_by
    else:
        sample_entry_salary = median_salary - median_salary * random_percent_to_change_by
    return sample_entry_salary

"""
- olympiads
- courses you took
- scholarships (there may be some bias here)
- extra-curricular courses (there may be some bias here)
- work experience / internships
- papers
- demonstrating leadership skills (volunteering / positions at school)
- languages spoken?
- music school?
- sports awards
- articles about them
"""


def generate_random_feature(range, num_features, p):
    return numpy.random.choice(range, num_features, p)


def generate_example(median_salary_data):
    random.seed(datetime.now())
    numpy.random.seed(int(time.time()))

    # For each university / degree example generate a random number of rows with simulated data:
    simulated_data = []
    for index, row in median_salary_data.iterrows():
        # random.seed(datetime.now())
        num_examples_per_uni_degree = random.randint(1, 101)
        print("Generate %s examples for uni %s and degree %s" % (num_examples_per_uni_degree, row['university'], row['degree']))
        for i in range(num_examples_per_uni_degree):
            example = defaultdict()
            example['university'] = row['university']
            example['degree'] = row['degree']
            example['median_entry_salary'] = row['median_entry_salary']
            example['entry_salary'] = generate_sample_entry_salary(row['median_entry_salary'])

            # numpy.random.seed(int(time.time()))

            # Simulate the chance of being a gold/silver/brown medal winner of an international olympiad (e.g. in Math)
            # TODO: Simulate that for all possible subjects
            # TODO: Use a count feature, rather than a boolean (e.g. count the number of gold medals in x olympiad of y type)
            example['has_gold_medals_in_international_olympiads'] = generate_random_feature(2, 1, p=[0.99999, 0.00001])[0]
            example['has_silver_medals_in_international_olympiads'] = generate_random_feature(2, 1, p=[0.99998, 0.00002])[0]
            example['has_brown_medals_in_international_olympiads'] = generate_random_feature(2, 1, p=[0.99997, 0.00003])[0]
            example['was_in_finals_in_international_olympiads'] = generate_random_feature(2, 1, p=[0.99995, 0.00005])[0]

            example['has_gold_medals_in_national_olympiads'] = generate_random_feature(2, 1, p=[0.9999, 0.0001])[0]
            example['has_silver_medals_in_national_olympiads'] = generate_random_feature(2, 1, p=[0.9998, 0.0002])[0]
            example['has_brown_medals_in_national_olympiads'] = generate_random_feature(2, 1, p=[0.9997, 0.0003])[0]
            example['was_in_finals_in_national_olympiads'] = generate_random_feature(2, 1, p=[0.9995, 0.0005])[0]

            example['has_gold_medals_in_regional_olympiads'] = generate_random_feature(2, 1, p=[0.999, 0.001])[0]
            example['has_silver_medals_in_regional_olympiads'] = generate_random_feature(2, 1, p=[0.998, 0.002])[0]
            example['has_brown_medals_in_regional_olympiads'] = generate_random_feature(2, 1, p=[0.997, 0.003])[0]
            example['was_in_finals_in_regional_olympiads'] = generate_random_feature(2, 1, p=[0.995, 0.005])[0]

            example['has_gold_medal_winner_in_international_sports_competition'] = generate_random_feature(2, 1, p=[0.99999, 0.00001])[0]
            example['has_silver_medals_in_international_sports_competition'] = generate_random_feature(2, 1, p=[0.99998, 0.00002])[0]
            example['has_brown_medals_in_international_sports_competition'] = generate_random_feature(2, 1, p=[0.99997, 0.00003])[0]
            example['was_in_finals_in_international_sports_competition'] = generate_random_feature(2, 1, p=[0.99995, 0.00005])[0]

            example['has_gold_medals_in_national_sports_competition'] = generate_random_feature(2, 1, p=[0.9999, 0.0001])[0]
            example['has_silver_medals_in_national_sports_competition'] = generate_random_feature(2, 1, p=[0.9998, 0.0002])[0]
            example['has_brown_medals_in_national_sports_competition'] = generate_random_feature(2, 1, p=[0.9997, 0.0003])[0]
            example['was_in_finals_in_national_sports_competition'] = generate_random_feature(2, 1, p=[0.9995, 0.0005])[0]

            example['has_gold_medals_in_regional_sports_competition'] = generate_random_feature(2, 1, p=[0.999, 0.001])[0]
            example['has_silver_medals_in_regional_sports_competition'] = generate_random_feature(2, 1, p=[0.998, 0.002])[0]
            example['has_brown_medals_in_regional_sports_competition'] = generate_random_feature(2, 1, p=[0.997, 0.003])[0]
            example['was_in_finals_in_regional_sports_competition'] = generate_random_feature(2, 1, p=[0.995, 0.005])[0]

            example['num_years_high_school_president'] = generate_random_feature(4, 1, p=[0.88, 0.06, 0.03, 0.03])[0]
            example['num_years_high_school_class_president'] = generate_random_feature(4, 1, p=[0.60, 0.20, 0.10, 0.10])[0]

            example['has_fluent_in_english'] = generate_random_feature(2, 1, p=[0.80, 0.20])[0]
            example['has_fluent_in_spanish'] = generate_random_feature(2, 1, p=[0.85, 0.15])[0]
            example['has_fluent_in_german'] = generate_random_feature(2, 1, p=[0.92, 0.08])[0]
            example['has_fluent_in_chinese'] = generate_random_feature(2, 1, p=[0.85, 0.15])[0]
            example['has_fluent_in_french'] = generate_random_feature(2, 1, p=[0.95, 0.05])[0]

            example['num_papers_published'] = generate_random_feature(4, 1, p=[0.96, 0.02, 0.01, 0.01])[0]

            example['num_months_of_work_experience'] = generate_random_feature(10, 1, p=[0.05, 0.20, 0.20, 0.15,
                                                                                     0.10, 0.10, 0.07, 0.07, 0.03, 0.03])
            example_df = pd.DataFrame(example, index=[0])
            simulated_data.append(example_df)

    simulated_data_df = pd.concat(simulated_data)
    return simulated_data_df


def get_sample_data():
    median_salaries = pd.read_csv('median_entry_salary_by_degree.csv')
    median_salaries = median_salaries[['university', 'degree', 'median_entry_salary']]
    simulated_training_data = generate_example(median_salaries)
    simulated_training_data.to_csv('simulated_training_data.csv', index=False)
    return simulated_training_data









