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
from sklearn.metrics import r2_score


rf = RandomForestRegressor()
rf.fit(train_features, train_price)
predictions = rf.predict(test_features)
print(r2_score(test_price, predictions))



