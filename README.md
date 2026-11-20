# Week 1 Assessment: Employee Analysis and Repository Workflow

This beginner-friendly project uses Git, a Jupyter notebook, and Pandas to
explore a small employee dataset.

## Setup

Run these commands from the repository folder in PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the notebook

```powershell
jupyter notebook notebooks\week1_analysis.ipynb
```

The notebook loads the CSV, checks the data, filters Chennai employees, and
compares department salaries. It uses `%timeit` once to time the average-salary
calculation.

## Export the notebook

```powershell
jupyter nbconvert --to script --output-dir src notebooks\week1_analysis.ipynb
```

The exported Python file is `src\week1_analysis.py`.

## Five findings

- The dataset contains 8 employees.
- 4 employees are based in Chennai.
- IT has the largest headcount, with 3 employees.
- Finance has the highest average salary, at 90000.
- The overall average salary is 58500.
