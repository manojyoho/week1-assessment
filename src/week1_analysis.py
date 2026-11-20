#!/usr/bin/env python
# coding: utf-8

# # Week 1 Assessment: Employee Analysis
# 
# A small beginner-friendly analysis using Pandas and the employee CSV file.

# ## 1. Load the data
# 
# Run this notebook from the project folder or from the `notebooks` folder.

# In[1]:


from pathlib import Path
import pandas as pd

data_file = Path("data/employees.csv")
if not data_file.exists():
    data_file = Path("../data/employees.csv")

employees = pd.read_csv(data_file)
print("Rows and columns:", employees.shape)


# ## 2. Inspect the data
# 
# Use `head()` to preview the rows and `info()` to check columns and types.

# In[2]:


display(employees.head())
employees.info()


# ## 3. Filter and summarize
# 
# Find employees in Chennai and calculate the average salary for each department.

# In[3]:


chennai_employees = employees.loc[employees["city"] == "Chennai"]
print("Employees in Chennai:", len(chennai_employees))
display(chennai_employees[["name", "department", "city"]])

average_salary = employees.groupby("department")["salary"].mean()
display(average_salary)


# ## 4. Time one calculation
# 
# This command repeats the calculation and reports its execution time.

# In[4]:


get_ipython().run_line_magic('timeit', 'employees["salary"].mean()')


# ## 5. Findings
# 
# - The dataset contains 8 employees.
# - 4 employees are based in Chennai.
# - IT has the largest headcount, with 3 employees.
# - Finance has the highest average salary, at 90000.
# - The overall average salary is 58500.
