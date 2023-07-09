# %%

import numpy as np
import pandas as pd

filepath = 'data/activity.csv'

expense_keywords = ['SLACK', 'TWILIO', 'GITHUB', 'MIXPANEL', 'GOOGLE']

expense_df = pd.read_csv(filepath)

filtered_expense_boolean = expense_df['Description'].str.contains('|'.join(expense_keywords), case=False)

filtered_expense_df = expense_df[filtered_expense_boolean]

# %%

filtered_expense_df = filtered_expense_df[['Date', 'Description', 'Amount']]

conditions = [
    filtered_expense_df['Description'].str.contains('SLACK', case=False),
    filtered_expense_df['Description'].str.contains('TWILIO', case=False),
    filtered_expense_df['Description'].str.contains('GITHUB', case=False),
    filtered_expense_df['Description'].str.contains('MIXPANEL', case=False),
    filtered_expense_df['Description'].str.contains('GOOGLE', case=False)
]

filtered_expense_df['Product'] = np.select(conditions, expense_keywords,
                                             default='Unknown')

filtered_expense_df.to_excel('test.xlsx')





# %%



