# PPHA 30537
# Spring 2024
# Homework 4

# YOUR NAME HERE

# YOUR CANVAS NAME HERE
# YOUR GITHUB USER NAME HERE

# Due date: Sunday May 12th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

# Question 1: Explore the data APIs available from Pandas DataReader. Pick
# any two countries, and then 
#   a) Find two time series for each place
#      - The time series should have some overlap, though it does not have to
#        be perfectly aligned.
#      - At least one should be from the World Bank, and at least one should
#        not be from the World Bank.
#      - At least one should have a frequency that does not match the others,
#        e.g. annual, quarterly, monthly.
#      - You do not have to make four distinct downloads if it's more appropriate
#        to do a group of them, e.g. by passing two series titles to FRED.
import pandas_datareader as pdr
import datetime

start_date = datetime.datetime(2000, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

us_gdp = pdr.data.DataReader('GDP_USA', 'fred', start=start_date, end=end_date)
us_unemployment = pdr.data.DataReader('UNRATE', 'fred', start=start_date, end=end_date)

china_gdp = pdr.data.DataReader('GDP_CHINA', 'fred', start=start_date, end=end_date)
china_cpi = pdr.data.DataReader('CHNCPIALLMINMEI', 'fred', start=start_date, end=end_date)  # China CPI All Items Index

print("US GDP:")
print(us_gdp.head())
print("\nUS Unemployment Rate:")
print(us_unemployment.head())
print("\nChina GDP:")
print(china_gdp.head())
print("\nChina Consumer Price Index:")
print(china_cpi.head())

#   b) Adjust the data so that all four are at the same frequency (you'll have
#      to look this up), then do any necessary merge and reshaping to put
#      them together into one long (tidy) format dataframe.
import pandas as pd

us_gdp_monthly = us_gdp.resample('M').mean()
china_gdp_monthly = china_gdp.resample('M').mean()
us_unemployment_monthly = us_unemployment.resample('M').mean()
china_cpi_monthly = china_cpi.resample('M').mean()

us_data = pd.merge(us_gdp_monthly, us_unemployment_monthly, left_index=True, right_index=True, how='outer')
china_data = pd.merge(china_gdp_monthly, china_cpi_monthly, left_index=True, right_index=True, how='outer')

us_data.columns = ['US_GDP', 'US_Unemployment_Rate']
china_data.columns = ['China_GDP', 'China_CPI']

combined_data = pd.merge(us_data, china_data, left_index=True, right_index=True, how='outer')

combined_data.reset_index(inplace=True)
combined_data = pd.melt(combined_data, id_vars='DATE', var_name='Indicator', value_name='Value')

print(combined_data.head())

#   c) Finally, go back and change your earlier code so that the
#      countries and dates are set in variables at the top of the file. Your
#      final result for parts a and b should allow you to (hypothetically) 
#      modify these values easily so that your code would download the data
#      and merge for different countries and dates.
#      - You do not have to leave your code from any previous way you did it
#        in the file. If you did it this way from the start, congrats!
#      - You do not have to account for the validity of all the possible 
#        countries and dates, e.g. if you downloaded the US and Canada for 
#        1990-2000, you can ignore the fact that maybe this data for some
#        other two countries aren't available at these dates.
import pandas_datareader as pdr
import datetime
import pandas as pd

countries = ['USA', 'CHN']
start_date = datetime.datetime(2000, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

def fetch_data(country_code):
    gdp = pdr.data.DataReader(f'GDP_{country_code}', 'fred', start=start_date, end=end_date)
    unemployment = pdr.data.DataReader('UNRATE', 'fred', start=start_date, end=end_date)
    return gdp, unemployment

def adjust_and_merge(gdp, unemployment):
    gdp_monthly = gdp.resample('M').mean()
    unemployment_monthly = unemployment.resample('M').mean()
    data = pd.merge(gdp_monthly, unemployment_monthly, left_index=True, right_index=True, how='outer')
    return data

def main():
    all_data = pd.DataFrame()
    for country in countries:
        gdp, unemployment = fetch_data(country)
        country_data = adjust_and_merge(gdp, unemployment)
        country_data.columns = ['GDP', 'Unemployment_Rate']  # Rename columns
        all_data = pd.concat([all_data, country_data], axis=0)

    all_data.reset_index(inplace=True)
    all_data = pd.melt(all_data, id_vars='DATE', var_name='Indicator', value_name='Value')
    
    print(all_data.head())

if __name__ == "__main__":
    main()


#   d) Clean up any column names and values so that the data is consistent
#      and clear, e.g. don't leave some columns named in all caps and others
#      in all lower-case, or some with unclear names, or a column of mixed 
#      strings and integers. Write the dataframe you've created out to a 
#      file named q1.csv, and commit it to your repo.
import pandas_datareader as pdr
import datetime
import pandas as pd

countries = ['USA', 'CHN']
start_date = datetime.datetime(2000, 1, 1)
end_date = datetime.datetime(2023, 12, 31)

def fetch_data(country_code):
    gdp = pdr.data.DataReader(f'GDP_{country_code}', 'fred', start=start_date, end=end_date)
    unemployment = pdr.data.DataReader('UNRATE', 'fred', start=start_date, end=end_date)
    return gdp, unemployment

def adjust_and_merge(gdp, unemployment):
    gdp_monthly = gdp.resample('M').mean()
    unemployment_monthly = unemployment.resample('M').mean()
    data = pd.merge(gdp_monthly, unemployment_monthly, left_index=True, right_index=True, how='outer')
    return data

def main():
    all_data = pd.DataFrame()
    for country in countries:
        gdp, unemployment = fetch_data(country)
        country_data = adjust_and_merge(gdp, unemployment)
        country_data.columns = ['GDP', 'Unemployment_Rate']  # Rename columns
        all_data = pd.concat([all_data, country_data], axis=0)

    all_data.reset_index(inplace=True)
    all_data = pd.melt(all_data, id_vars='DATE', var_name='Indicator', value_name='Value')

    all_data['Country'] = all_data['Indicator'].str.split('_').str[1].str.upper()  # Extract country from indicator
    all_data['Indicator'] = all_data['Indicator'].str.split('_').str[0].str.title()  # Capitalize indicator names

    all_data.to_csv('q1.csv', index=False)
    print("Data written to q1.csv")

if __name__ == "__main__":
    main()



# Question 2: On the following Harris School website:
# https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics
# There is a list of six bullet points under "Required courses" and 12
# bullet points under "Elective courses". Using requests and BeautifulSoup: 
#   - Collect the text of each of these bullet points
#   - Add each bullet point to the csv_doc list below as strings (following 
#     the columns already specified). The first string that gets added should be 
#     approximately in the form of: 
#     'required,PPHA 30535 or PPHA 30537 Data and Programming for Public Policy I'
#   - Hint: recall that \n is the new-line character in text
#   - You do not have to clean up the text of each bullet point, or split the details out
#     of it, like the course code and course description, but it's a good exercise to
#     think about.
#   - Using context management, write the data out to a file named q2.csv
#   - Finally, import Pandas and test loading q2.csv with the read_csv function.
#     Use asserts to test that the dataframe has 18 rows and two columns.

csv_doc = ['type,description']
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

url = "https://harris.uchicago.edu/academics/design-your-path/certificates/certificate-data-analytics"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

required_section = soup.find("h3", text="Required courses")
required_text = []
if required_section:
    required_courses = required_section.find_next("ul").find_all("li")
    required_text = [course.get_text(strip=True) for course in required_courses]

elective_section = soup.find("h3", text="Elective courses")
elective_text = []
if elective_section:
    elective_courses = elective_section.find_next("ul").find_all("li")
    elective_text = [course.get_text(strip=True) for course in elective_courses]

course_data = [("required", course) for course in required_text] + [("elective", course) for course in elective_text]

with open("q2.csv", "w", newline="", encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["type", "description"])  # Write header
    csv_writer.writerows(course_data)  # Write course data

df = pd.read_csv("q2.csv")

print(df)
print("Dataframe shape:", df.shape)

assert df.shape == (18, 2)
