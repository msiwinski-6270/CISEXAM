import pandas as pd

cambridge = pd.read_csv('Cambridge_Salaries.csv') #importing cambridge dataset

general = cambridge.describe() #creating a variable with general statistics

grouped = cambridge.groupby("Division")
totalgroupby = grouped.sum("Total Salary")

print("The dataset has the following statistics")
print(general)
print ("The total salary budget for each division is:")
print(totalgroupby)