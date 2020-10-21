#!/usr/bin/python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

var_2 = ['marital', 'contact_mode', 'education', 'previous_outcome']
var_3 = ['default', 'loan', 'housing']

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

def plot_hist(df, x_col, target_col):

	"""
	Plot distribution of selected variables.

	Keyword arguments:
	df -- the dataframe to reference from
	x_col -- the variable to visualise
	target_col -- the target variable
	"""

	new_plot = sns.FacetGrid(df, col = target_col, height = 6)
	new_plot.map(sns.histplot, x_col, bins = 30)
	new_plot.set_axis_labels(str(x_col).capitalize(), 'Count')
	plt.subplots_adjust(top = 0.85)
	new_plot.fig.suptitle('Distribution of Client ' + str(x_col).capitalize(), fontsize = 18)

	return new_plot



def plot_bar(df, x_col, target_col):

	if x_col == 'day':
		new_df = pd.crosstab(df[x_col], df[target_col], normalize = 'all')
		new_df.plot(kind = 'bar', figsize = (14, 6))
		plt.xticks(range(0, len(new_df.index)), new_df.index, fontsize = 12)
		plt.xlabel('Day-of-Month', fontsize = 12)
		plt.ylabel('Frequency', fontsize = 12)
		plt.title('Subscription Outcome by Day-of-Month', fontsize = 18)

	elif x_col == 'job':
		new_df = pd.crosstab(df[x_col], df[target_col], normalize = 'all').sort_values(by = 1, ascending = False)
		new_df.plot(kind = 'bar', figsize = (14, 6))
		plt.xticks(range(0, len(new_df.index)), new_df.index, fontsize = 12)
		plt.xlabel('Job Type', fontsize = 12)
		plt.ylabel('Frequency', fontsize = 12)
		plt.title('Subscription Outcome by Job Type', fontsize = 18)

	else:
		new_df = pd.crosstab(df[x_col], df[target_col], normalize = 'all').reindex(months)
		new_df.plot(kind = 'bar', figsize = (14, 6))
		plt.xticks(range(0, len(new_df.index)), new_df.index, fontsize = 12)
		plt.xlabel('Month-of-Year', fontsize = 12)
		plt.ylabel('Frequency', fontsize = 12)
		plt.title('Subscription Outcome by Month-of-Year', fontsize = 18)

	return new_df


def subplot_bar(df, target_col, ncol):

	index = 0

	fig, axes = plt.subplots(nrows=1, ncols=ncol,figsize=(20, 12), sharey = True)
	fig.subplots_adjust(hspace=.3)

	if ncol == 4:

		for col in var_2:

			new_df = pd.crosstab(df[col], df[target_col], normalize = 'all').sort_values(by = 1, ascending = False)
			new_df.plot(kind = 'bar', ax=axes[index], fontsize = 14, title = str(col).capitalize())

			print(new_df, '\n')

			index += 1

	else:

		for col in var_3:

			new_df = pd.crosstab(df[col], df[target_col], normalize = 'all').sort_values(by = 1, ascending = False)
			new_df.plot(kind = 'bar', ax=axes[index], fontsize = 14, title = str(col).capitalize())

			print(new_df, '\n')

			index += 1

