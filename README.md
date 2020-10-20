# Bank Marketing Strategy
An Exploratory Data Analysis (EDA) project on bank marketing campaign for a term deposit.

## Description
The dataset used for this project can be found [here](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing).

### The Problem
![Term Deposit](/Images/term_deposit.jpg)

The bank recently experienced a decline in the number of subcriptions for their [term deposit](https://www.investopedia.com/terms/t/termdeposit.asp). They have come up with ads for their existing clients to address this and would like to do a targeted marketing approach. They would like to predict which of their clients have a higher chance to subscribe for a term deposit.

### The Objective
- To understand what factors contributed most to term deposit subscription.

- To perform clustering to find any meaningful patterns of employee traits.

- To create a model that predicts the likelihood if a certain client will subscribe for a term deposit or not. 

- To create or improve different marketing strategies for clients that are least likely to subscribe for a term deposit.

The implementation of this model will allow the bank to identify which clients to target.

### Features and Target

#### Client data:
1 - age (numeric) <br>
2 - job : type of job (categorical: 'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self employed', 'services', 'student', 'technician', 'unemployed', 'unknown') <br>
3 - marital : marital status (categorical: 'divorced', 'married', 'single', 'unknown'; note: 'divorced' means divorced or widowed) <br>
4 - education (categorical: 'basic.4y', 'basic.6y', 'basic.9y', 'high.school', 'illiterate', 'professional.course', 'university.degree', 'unknown') <br>
5 - default: has credit in default? (categorical: 'no', 'yes', 'unknown') <br>
6 - balance: average yearly balance (numeric) <br>
7 - housing: has housing loan? (categorical: 'no', 'yes', 'unknown') <br>
8 - loan: has personal loan? (categorical: 'no', 'yes', 'unknown') <br>

#### Campaign data:
9 - contact: contact communication type (categorical: 'cellular','telephone') <br>
10 - day: last contact day of month (numeric) <br>
11 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec') <br>
12 - duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model. <br>
13 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact) <br>
14 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; -1 means client was not previously contacted) <br>
15 - previous: number of contacts performed before this campaign and for this client (numeric) <br>
16 - poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success') <br>


#### Target variable:
17 - deposit: has the client subscribed a term deposit? (binary: 'yes','no')

## EDA
### Correlation with target
![Correlation Heatmap](/Images/corr_heatmap.png)

Contact duration is highly correlated witht the subscription outcome.

### Kernel Density Estimate plot of clients' age
![Age KDE](/Images/EDA_age_KDE.png)

A higher proportion of clients below 30 years old and above 60 years old subscribed for a term deposit.

### Distribution of contact duration
![Contact Duration](/Images/EDA_duration.png)

The longer the contact duration, it is more likely for the client to subscribe for a term deposit.

### Subscription outcome based on month of contact
![Month](/Images/EDA_month.png)

More than **60%** of the clients were contacted from May to August but the clients tend to not subscribe for a term deposit during this period.

### Subscription outcome based on job type
![Job](/Images/EDA_job.png)

Most of the bank's clients are working in management and slightly more than half of them subscribed for a term deposit.
Clients that are students and retirees have a higher chance of subscribing for a term deposit.

## Data pre-processing

### Cyclical features - convert day_of_month and month_of_year
'''python
df['day_sin'] = np.sin(df.day*(2.*np.pi/24))
df['day_cos'] = np.cos(df.day*(2.*np.pi/24))
df['month_sin'] = np.sin((df.month-1)*(2.*np.pi/12))
df['month_cos'] = np.cos((df.month-1)*(2.*np.pi/12))
'''

## Modelling

### Base model - Logistic Regression
F1 score - 0.784

### Random Forest Classifier
Mean F1 score from 5-fold cross validation - 0.844

### Gradient Boosting Classifier
Mean F1 score from 5-fold cross validation - 0.839
