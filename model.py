"""
# How to exclude factors that may introduce discrimination or bias?
- don't take into account any geographical info
- don't take into account family's background / whether they went to college / their salary


# Features:
- olympiads
- courses you took
- university you got accepted to
- department / course you got accepted to
- scholarships (there may be some bias here)
- extra-curricular courses (there may be some bias here)
- work experience / internships
- papers
- demonstrating leadership skills (volunteering / positions at school)
- languages spoken?
- music school?
- sports awards
- articles about them


# Predict:
- base salary right after college

# Warning:
- the predictions can't be visible to the investees

"""

import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    data = pd.read_csv('simulated_training_data.csv')

    # Need to limit to 10k otherwise it takes too long to train
    data = data.sample(10000)
    data.reset_index(inplace=True, drop=True)

    # TODO: get dummies for uni names

    actuals = np.array(data['entry_salary'])

    features = data.drop('entry_salary', axis=1)
    features = pd.get_dummies(features)
    feature_list = list(features.columns)
    features = np.array(features)

    train_features, test_features, train_labels, test_labels = train_test_split(features, actuals, test_size=0.33,
                                                                                random_state=42)
    rf = RandomForestRegressor(n_estimators=1000, random_state=42)
    rf.fit(train_features, train_labels)

    predictions = rf.predict(test_features)
    errors = abs(predictions - test_labels)
    print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

    mape = 100 * (errors / test_labels)
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')

    importances = list(rf.feature_importances_)
    feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(feature_list, importances)]
    feature_importances = sorted(feature_importances, key=lambda x: x[1], reverse=True)

    for pair in feature_importances:
        print('Variable: {:20} Importance: {}'.format(*pair))





