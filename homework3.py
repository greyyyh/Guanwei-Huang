# PPHA 30537
# Spring 2024
# Homework 3

# YOUR NAME HERE
# Guanwei Huang
# YOUR CANVAS NAME HERE
# Guanwei Huang
# YOUR GITHUB USER NAME HERE
# greyyyh

# Due date: Sunday May 5th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_1_plot.png" (for 1.1), "q1_2_plot.png" (for 1.2),
# etc. using fig.savefig. If a question calls for more than one plot, name them
# "q1_1a_plot.png", "q1_1b_plot.png",  etc.

# Question 1.1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW3 Q1.1".

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

plt.figure(figsize=(10, 6))

plt.scatter(x, y1, label='y1', color='blue')  
plt.plot(x, y2, label='y2', color='red')      

plt.xlabel('Date')
plt.ylabel('Values')
plt.title('HW3 Q1.1')
plt.legend()

plt.xticks(rotation=45)  

plt.tight_layout()
plt.savefig('q1_1_plot.png')  
plt.show()

# Question 1.2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x, y1, color='blue', label='sin(x)')

ax2 = ax.twinx()

ax2.plot(x, y2, color='red', label='cos(x)')

ax.set_xlabel('x')
ax.set_ylabel('sin(x)', color='blue')
ax2.set_ylabel('cos(x)', color='red')
plt.title('Question 2 Figure')

lines, labels = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper right')

plt.savefig('q1_2_plot.png')  
plt.show()


# Question 1.3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.
import pandas as pd
import matplotlib.pyplot as plt

mpg_data = pd.read_csv('mpg.csv')

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.scatter(mpg_data['displacement'], mpg_data['mpg'], alpha=0.3)
plt.xlabel('Engine Displacement (cu in)')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Gas Mileage vs. Engine Displacement')

plt.subplot(1, 3, 2)
plt.scatter(mpg_data['horsepower'], mpg_data['mpg'], alpha=0.3)
plt.xlabel('Horsepower')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Gas Mileage vs. Horsepower')

plt.subplot(1, 3, 3)
plt.scatter(mpg_data['weight'], mpg_data['mpg'], alpha=0.3)
plt.xlabel('Weight (lbs)')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Gas Mileage vs. Weight')

plt.tight_layout()

plt.savefig('q1_3a_plot.png')  
plt.savefig('q1_3b_plot.png')  
plt.savefig('q1_3c_plot.png')  
plt.show()


# Question 1.4: Continuing with the data from question 1.3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.
import matplotlib.pyplot as plt

plt.scatter(mpg_data['cylinders'], mpg_data['mpg'])
plt.xlabel('Cylinders')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Gas Mileage vs. Cylinders')
plt.savefig('q1_4a_plot.png') 
plt.show()

import seaborn as sns

plt.figure(figsize=(8, 6))
sns.boxplot(x='cylinders', y='mpg', data=mpg_data)
plt.xlabel('Cylinders')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Gas Mileage vs. Cylinders')
plt.savefig('q1_4b_plot.png')
plt.show()

# Question 1.5: Continuing with the data from question 1.3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.
import matplotlib.pyplot as plt

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))

axes[0, 0].scatter(mpg_data['displacement'], mpg_data['mpg'])
axes[0, 0].set_xlabel('Engine Displacement (cu in)')
axes[0, 0].set_ylabel('Miles per Gallon (mpg)')
axes[0, 0].set_title('Gas Mileage vs. Engine Displacement')

axes[0, 1].scatter(mpg_data['horsepower'], mpg_data['mpg'])
axes[0, 1].set_xlabel('Horsepower')
axes[0, 1].set_title('Gas Mileage vs. Horsepower')

axes[1, 0].scatter(mpg_data['weight'], mpg_data['mpg'])
axes[1, 0].set_xlabel('Weight (lbs)')
axes[1, 0].set_ylabel('Miles per Gallon (mpg)')
axes[1, 0].set_title('Gas Mileage vs. Weight')

axes[1, 1].scatter(mpg_data['acceleration'], mpg_data['mpg'])
axes[1, 1].set_xlabel('Acceleration (s)')
axes[1, 1].set_title('Gas Mileage vs. Acceleration')

axes[0, 1].tick_params(axis='y', labelleft=False)
axes[1, 1].tick_params(axis='y', labelleft=False)

fig.suptitle('Changes in MPG', fontsize=16)

fig.text(0.06, 0.5, 'mpg', va='center', rotation='vertical', fontsize=14)

plt.tight_layout()

plt.savefig('q1_5a_plot.png')  
plt.savefig('q1_5b_plot.png')  
plt.savefig('q1_5c_plot.png')  
plt.savefig('q1_5d_plot.png')  
plt.show()

# Question 1.6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8, 6))
sns.boxplot(x='origin', y='mpg', data=mpg_data)
plt.xlabel('Region of Origin')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Fuel Efficiency by Region')
plt.savefig('q1_6_plot.png') 
plt.show()
# The region with the lowest median miles per gallon (mpg) value in the box plot 
# indicates the least fuel-efficient cars, on average.

# Question 1.7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 1.6.
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.scatterplot(x='displacement', y='mpg', hue='origin', data=mpg_data)
plt.xlabel('Engine Displacement (cu in)')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Scatter Plot of MPG versus Displacement by Country of Origin')
plt.legend(title='Country of Origin')
plt.savefig('q1_7_plot.png') 
plt.show()

# Question 2: The file unemp.csv contains the monthly seasonally-adjusted unemployment
# rates for US states from January 2020 to December 2022. Load it as a dataframe, as well
# as the data from the policy_uncertainty.xlsx file from homework 2 (you do not have to make
# any of the changes to this data that were part of HW2, unless you need to in order to 
# answer the following questions).
import pandas as pd
unemp_data = pd.read_csv('unemp.csv')
policy_uncertainty_data = pd.read_excel('policy_uncertainty.xlsx')

#    2.1: Merge both dataframes together
unemp_data['STATE'] = policy_uncertainty_data['state']
merged_data = pd.merge(unemp_data, policy_uncertainty_data, left_on='STATE', right_on='state')
print(merged_data.head())

#    2.2: Calculate the log-first-difference (LFD) of the EPU-C data
import numpy as np
merged_data.sort_values(by=['state', 'year', 'month'], inplace=True)

merged_data['EPU_C_LFD'] = merged_data.groupby('state')['EPU_Composite'].diff().apply(lambda x: np.log(x) if x != 0 else None)

print(merged_data.head())

#    2.2: Select five states and create one Matplotlib figure that shows the unemployment rate
#         and the LFD of EPU-C over time for each state. Save the figure and commit it with 
#         your code.
import matplotlib.pyplot as plt

selected_states = ['California', 'Texas', 'New York', 'Florida', 'Illinois']

fig, axes = plt.subplots(nrows=len(selected_states), ncols=1, figsize=(10, 6), sharex=True)

for i, state in enumerate(selected_states):
    state_data = merged_data[merged_data['state'] == state]

    axes[i].plot(state_data['DATE'], state_data['unemp_rate'], label='Unemployment Rate', color='blue')
    axes[i].set_ylabel('Unemployment Rate')
    axes[i].set_title(f'Unemployment Rate and LFD of EPU-C for {state}')

    axes2 = axes[i].twinx()
    axes2.plot(state_data['DATE'], state_data['EPU_C_LFD'], label='LFD of EPU-C', color='red')
    axes2.set_ylabel('LFD of EPU-C')

    axes[i].legend(loc='upper left')
    axes2.legend(loc='upper right')

plt.tight_layout()
plt.savefig('q2_2_plot.png')
plt.show()

#    2.3: Using statsmodels, regress the unemployment rate on the LFD of EPU-C and fixed
#         effects for states. Include an intercept.
from linearmodels.panel import PanelOLS

dependent_var = 'unemp_rate'
independent_vars = ['EPU_C_LFD']

model = PanelOLS.from_formula(f'{dependent_var} ~ 1 + {" + ".join(independent_vars)} + EntityEffects', data=merged_data)
results = model.fit()

print(results)


#    2.4: Print the summary of the results, and write a 1-3 line comment explaining the basic
#         interpretation of the results (e.g. coefficient, p-value, r-squared), the way you 
#         might in an abstract.
# Print summary of the regression results
print(results.summary)

# Interpretation:
# The regression results suggest a statistically significant negative relationship 
# between the unemployment rate and the log-first-difference (LFD) of Economic Policy 
# Uncertainty Composite (EPU_C_LFD) (coefficient: -2.481e-16, p-value: 0.0000).
# However, the R-squared values are negative, indicating that the model does not 
# fit the data well. Additionally, the F-test for Poolability indicates that the 
# fixed effects for states are statistically significant.
