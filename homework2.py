# PPHA 30537
# Spring 2024
# Homework 2

# YOUR NAME HERE
# Guanwei Huang
# YOUR GITHUB USER NAME HERE
# greyyyh
# Due date: Sunday April 21st before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.  Using functions for organization will be rewarded.

##################

# To answer these questions, you will use the csv document included in
# your repo.  In nst-est2022-alldata.csv: SUMLEV is the level of aggregation,
# where 10 is the whole US, and other values represent smaller geographies. 
# REGION is the fips code for the US region. STATE is the fips code for the 
# US state.  The other values are as per the data dictionary at:
# https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2020-2022/NST-EST2022-ALLDATA.pdf
# Note that each question will build on the modified dataframe from the
# question before.  Make sure the SettingWithCopyWarning is not raised.

# PART 1: Macro Data Exploration

# Question 1.1: Load the population estimates file into a dataframe. Specify
# an absolute path using the Python os library to join filenames, so that
# anyone who clones your homework repo only needs to update one for all
# loading to work.
import pandas as pd
import os
data_directory = "C:/Users/Hgw thunderobot/python hw"
filename = "NST-EST2022-ALLDATA.csv"
file_path = os.path.join(data_directory, filename)
population_df = pd.read_csv(file_path)
print(population_df.head())

# Question 1.2: Your data only includes fips codes for states (STATE).  Use 
# the us library to crosswalk fips codes to state abbreviations.  Drop the
# fips codes.
import pandas as pd
import os
import us

def fips_to_state(fips_code):
    state = us.states.lookup(fips_code)
    if state:
        return state.abbr
    else:
        return None

population_df['STATE'] = population_df['STATE'].apply(fips_to_state)

population_df.drop(columns=['FIPS'], inplace=True)

print(population_df.head())

# Question 1.3: Then show code doing some basic exploration of the
# dataframe; imagine you are an intern and are handed a dataset that your
# boss isn't familiar with, and asks you to summarize for them.  Do not 
# create plots or use groupby; we will do that in future homeworks.  
# Show the relevant exploration output with print() statements.

print("First few rows of the dataframe:")
print(population_df.head())

print("\nShape of the dataframe:")
print(population_df.shape)

print("\nData types of each column:")
print(population_df.dtypes)

print("\nSummary statistics for numerical columns:")
print(population_df.describe())

print("\nUnique values in the 'STATE' column:")
print(population_df['STATE'].unique())

print("\nNumber of missing values in each column:")
print(population_df.isnull().sum())


# Question 1.4: Subset the data so that only observations for individual
# US states remain, and only state abbreviations and data for the population
# estimates in 2020-2022 remain.  The dataframe should now have 4 columns.

state_population_df = population_df[population_df['STATE'].notnull()]

state_population_df = state_population_df[['STATE', 'POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022']]

print(state_population_df.head())


# Question 1.5: Show only the 10 largest states by 2021 population estimates,
# in decending order.

largest_states_2021 = state_population_df.sort_values(by='POPESTIMATE2021', ascending=False)

top_10_largest_states_2021 = largest_states_2021.head(10)

print("Top 10 largest states by 2021 population estimates:")
print(top_10_largest_states_2021)


# Question 1.6: Create a new column, POPCHANGE, that is equal to the change in
# population from 2020 to 2022.  How many states gained and how many lost
# population between these estimates?

state_population_df['POPCHANGE'] = state_population_df['POPESTIMATE2022'] - state_population_df['POPESTIMATE2020']

gained_population_count = (state_population_df['POPCHANGE'] > 0).sum()
lost_population_count = (state_population_df['POPCHANGE'] < 0).sum()

print("Number of states that gained population: ", gained_population_count)
print("Number of states that lost population: ", lost_population_count)


# Question 1.7: Show all the states that had an estimated change in either
# direction of smaller than 1000 people. 

small_change_states = state_population_df[abs(state_population_df['POPCHANGE']) < 1000]

print("States with an estimated change in population smaller than 1000 people:")
print(small_change_states)


# Question 1.8: Show the states that had a population growth or loss of 
# greater than one standard deviation.  Do not create a new column in your
# dataframe.  Sort the result by decending order of the magnitude of 
# POPCHANGE.
import numpy as np

std_dev = state_population_df['POPCHANGE'].std()

significant_change_states = state_population_df[abs(state_population_df['POPCHANGE']) > std_dev]

print("States with population growth or loss greater than one standard deviation:")
print(significant_change_states.sort_values(by='POPCHANGE', ascending=False))

#PART 2: Data manipulation

# Question 2.1: Reshape the data from wide to long, using the wide_to_long function,
# making sure you reset the index to the default values if any of your data is located 
# in the index.  What happened to the POPCHANGE column, and why should it be dropped?
# Explain in a brief (1-2 line) comment.

state_population_df.reset_index(inplace=True)

long_state_population_df = pd.wide_to_long(state_population_df, stubnames='POPESTIMATE', i='index', j='Year')

long_state_population_df.drop(columns='POPCHANGE', inplace=True)

print(long_state_population_df.head())


# Question 2.2: Repeat the reshaping using the melt method.  Clean up the result so
# that it is the same as the result from 2.1 (without the POPCHANGE column).

state_population_df.reset_index(drop=True, inplace=True)

melted_state_population_df = state_population_df.melt(id_vars=['STATE'], 
            value_vars=['POPESTIMATE2020', 'POPESTIMATE2021', 'POPESTIMATE2022'],
            var_name='Year', value_name='POPESTIMATE')

melted_state_population_df.sort_values(by='STATE', inplace=True)

melted_state_population_df.reset_index(drop=True, inplace=True)

print(melted_state_population_df.head())



# Question 2.3: Open the state-visits.xlsx file in Excel, and fill in the VISITED
# column with a dummy variable for whether you've visited a state or not.  If you
# haven't been to many states, then filling in a random selection of them
# is fine too.  Save your changes.  Then load the xlsx file as a dataframe in
# Python, and merge the VISITED column into your original wide-form population 
# dataframe, only keeping values that appear in both dataframes.  Are any 
# observations dropped from this?  Show code where you investigate your merge, 
# and display any observations that weren't in both dataframes.
import pandas as pd
os.chdir("C:/Users/Hgw thunderobot/python hw")

visited_df = pd.read_excel("state-visits.xlsx")
print(visited_df.head())

merged_df = pd.merge(population_df, visited_df[['STATE', 'VISITED']], on='STATE', how='inner')

print(merged_df.head())

# Check if any observations are dropped during the merge
print("Number of rows in original population dataframe:", len(population_df))
print("Number of rows in visited dataframe:", len(visited_df))
print("Number of rows in merged dataframe:", len(merged_df))

# Display any observations that weren't in both dataframes
observations_not_in_both = pd.concat([population_df, visited_df]).loc[
    pd.concat([population_df, visited_df]).duplicated(subset=['STATE'], keep=False)
]
print("Observations not in both dataframes:")
print(observations_not_in_both)


# Question 2.4: The file policy_uncertainty.xlsx contains monthly measures of 
# economic policy uncertainty for each state, beginning in different years for
# each state but ending in 2022 for all states.  The EPU_National column esimates
# uncertainty from national sources, EPU_State from state, and EPU_Composite 
# from both (EPU-N, EPU-S, EPU-C).  Load it as a dataframe, then calculate 
# the mean EPU-C value for each state/year, leaving only columns for state, 
# year, and EPU_Composite, with each row being a unique state-year combination.
import pandas as pd

policy_df = pd.read_excel("policy_uncertainty.xlsx")

policy_df['EPU_Composite'] = (policy_df['EPU_National'] + policy_df['EPU_State']) / 2

policy_mean_df = policy_df[['state', 'year', 'EPU_Composite']]

policy_mean_df.drop_duplicates(inplace=True)

print(policy_mean_df.head())


# Question 2.5) Reshape the EPU data into wide format so that each row is unique 
# by state, and the columns represent the EPU-C values for the years 2022, 
# 2021, and 2020. 

policy_df = pd.read_excel("policy_uncertainty.xlsx")

policy_df = policy_df[policy_df['year'].isin([2020, 2021, 2022])]

epu_wide_df = policy_df.pivot_table(index='state', columns='year', values='EPU_Composite', aggfunc='mean')

epu_wide_df.reset_index(inplace=True)

epu_wide_df.columns.name = None
epu_wide_df.columns = ['state', 'EPU_C_2020', 'EPU_C_2021', 'EPU_C_2022']

print(epu_wide_df.head())


# Question 2.6) Finally, merge this data into your merged data from question 2.3, 
# making sure the merge does what you expect.

final_merged_df = pd.merge(merged_df, epu_wide_df, left_on='STATE', right_on='state', how='inner')

final_merged_df.drop(columns='state', inplace=True)

print(final_merged_df.head())


# Question 2.7: Using groupby on the VISITED column in the dataframe resulting 
# from the previous question, answer the following questions and show how you  
# calculated them: a) what is the single smallest state by 2022 population  
# that you have visited, and not visited?  b) what are the three largest states  
# by 2022 population you have visited, and the three largest states by 2022 
# population you have not visited? c) do states you have visited or states you  
# have not visited have a higher average EPU-C value in 2022?

grouped_df = final_merged_df.groupby('VISITED')

#a)
smallest_state = final_merged_df.loc[final_merged_df.groupby('VISITED')['POPESTIMATE2022'].idxmin(), ['STATE', 'VISITED', 'POPESTIMATE2022']]
print("Smallest state by 2022 population:")
print(smallest_state)

#b)
for visited, group in grouped_df:
    print(f"Top three largest states by 2022 population in visited: {visited}")
    if visited == 'Yes':
        largest_states_visited = group.nlargest(3, 'POPESTIMATE2022')[['STATE', 'POPESTIMATE2022']]
        print(largest_states_visited)
    else:
        largest_states_not_visited = group.nlargest(3, 'POPESTIMATE2022')[['STATE', 'POPESTIMATE2022']]
        print(largest_states_not_visited)

#c)
average_epuc_visited = final_merged_df[final_merged_df['VISITED'] == 'Yes']['EPU_C_2022'].mean()
average_epuc_not_visited = final_merged_df[final_merged_df['VISITED'] == 'No']['EPU_C_2022'].mean()

print("Average EPU-C value in 2022 for visited states:", average_epuc_visited)
print("Average EPU-C value in 2022 for not visited states:", average_epuc_not_visited)



# Question 2.8: Transforming data to have mean zero and unit standard deviation
# is often called "standardization", or a "zscore".  The basic formula to 
# apply to any given value is: (value - mean) / std
# Return to the long-form EPU data you created in step 2.4 and then, using groupby
# and a function you write, transform the data so that the values for EPU-C
# have mean zero and unit standard deviation for each state.  Add these values
# to a new column named EPU_C_zscore.

def calculate_zscore(group):
    mean = group['EPU_Composite'].mean()
    std = group['EPU_Composite'].std()
    group['EPU_C_zscore'] = (group['EPU_Composite'] - mean) / std
    return group

policy_mean_df_zscore = policy_mean_df.groupby('state').apply(calculate_zscore)

print(policy_mean_df_zscore.head())
