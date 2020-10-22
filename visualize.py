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

	"""
	Plot bar chart.

	Keyword arguments:
	df -- the dataframe to reference from
	x_col -- the variable to visualise
	target_col -- the target variable
	"""

	if x_col == 'day_of_month':
		new_df = pd.crosstab(df[x_col], df[target_col], normalize = 'all')


	elif x_col == 'job_type':
		new_df = pd.crosstab(df[x_col], df[target_col], normalize = 'all').sort_values(by = 1, ascending = False)


	else:
		new_df = pd.crosstab(df[x_col], df[target_col], normalize = 'all').reindex(months)


	new_df.plot(kind = 'bar', figsize = (14, 6))
	plt.xticks(range(0, len(new_df.index)), new_df.index, fontsize = 12)
	plt.xlabel(str(x_col).capitalize(), fontsize = 12)
	plt.ylabel('Frequency', fontsize = 12)
	plt.title('Subscription Outcome by ' + str(x_col).capitalize(), fontsize = 18)	

	return new_df


def subplot_bar(df, target_col, ncol):

	"""
	Plot multiple bar charts in subplot.

	Keyword arguments:
	df -- the dataframe to reference from
	x_col -- the variable to visualise
	target_col -- the target variable
	ncol -- number of columns in the subplot
	"""

	index = 0

	fig, axes = plt.subplots(nrows=1, ncols=ncol,figsize=(20, 12), sharey = True)
	fig.subplots_adjust(hspace=.3)

	if ncol == 4:

		for col in var_2:

			new_df = pd.crosstab(df[col], df[target_col], normalize = 'all').sort_values(by = 1, ascending = False)
			new_df.plot(kind = 'bar', ax=axes[index], fontsize = 12, title = str(col).capitalize())
			axes[index].title.set_size(14)

			print(new_df, '\n')

			index += 1

	else:

		for col in var_3:

			new_df = pd.crosstab(df[col], df[target_col], normalize = 'all').sort_values(by = 1, ascending = False)
			new_df.plot(kind = 'bar', ax=axes[index], fontsize = 14, title = str(col).capitalize())
			axes[index].title.set_size(14)

			print(new_df, '\n')

			index += 1