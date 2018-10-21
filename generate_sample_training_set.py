"""
Since there's not enough time to scrape or collect real training data during the hackathon we decided to create
a simulation of a machine learning model, i.e. train it on fake data (but still trying to be as close as possible
to reality based on data we scraped in a short amount of time) and include it in the pipeline of the product
we're going to pitch at the hackathon.

Here's what we did to generate the data to train the model:
1. Scraped real data from payscale with median entry salaries by university and degree
2. Generated a random set of other features that we could potentially use
3. Generated a random set of 'true' entry salaries based on the median entry salaries from payscale (in production
   we'd have to collect real data from sources like paysa, our users or other)
"""

