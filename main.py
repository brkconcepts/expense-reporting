# %%

import numpy as np
import pandas as pd
import sqlite3

filepath = 'data/activity.csv'
conn = sqlite3.connect("expense.db")

expense_keywords = ['SLACK', 'TWILIO', 'ZOOMVIDEO', 'GITHUB', 'MIXPANEL',
                    'GOOGLE', 'GOOGLE STORA', 'GSUITE_BRKCOC', 'GOOGLE*CLOUD']

expense_df = pd.read_csv(filepath)

filtered_expense_boolean = expense_df['Description'].str.contains('|'.join(expense_keywords), case=False)

filtered_expense_df = expense_df[filtered_expense_boolean]

# %%

filtered_expense_df = filtered_expense_df[['Date', 'Description', 'Amount']]

conditions = [
    filtered_expense_df['Description'].str.contains('SLACK', case=False),
    filtered_expense_df['Description'].str.contains('TWILIO', case=False),
    filtered_expense_df['Description'].str.contains('ZOOMVIDEO', case=False),
    filtered_expense_df['Description'].str.contains('GITHUB', case=False),
    filtered_expense_df['Description'].str.contains('MIXPANEL', case=False),
    filtered_expense_df['Description'].str.contains('GOOGLE', case=False),
    filtered_expense_df['Description'].str.contains('GOOGLE STORA', case=False),
    filtered_expense_df['Description'].str.contains('GSUITE_BRKCOC', case=False),
    filtered_expense_df['Description'].str.contains('GOOGLE*CLOUD', case=False)
]

filtered_expense_df['Product'] = np.select(conditions, expense_keywords,
                                             default='Unknown')


# %%
filtered_expense_df['Date'] = pd.to_datetime(filtered_expense_df['Date'])

# Extract month and year from the 'date' column
filtered_expense_df['month'] = filtered_expense_df['Date'].dt.month
filtered_expense_df['year'] = filtered_expense_df['Date'].dt.year

# Group the DataFrame by month and year
agg_expenses = filtered_expense_df.groupby(['month', 'year', 'Product'])
agg_expenses = agg_expenses['Amount'].sum()

agg_expenses.to_excel('data/expenses.xlsx')





# %%



