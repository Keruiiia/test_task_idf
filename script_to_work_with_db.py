import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv



# Load the environment variables from the .env file(as default)
load_dotenv()

# Create a connection to the database
engine = create_engine(os.getenv('DB_DSN'))

# List of all SQL files in the 'queries' folder
sql_files = [f for f in os.listdir('queries/') if f.endswith('.sql')]
sql_files.sort()

for sql_file in sql_files:
    # Read SQL query from a file
    with open(os.path.join('queries', sql_file)) as f:
        query = text(f.read())
    print(f'Processing {sql_file}')

    # Execute an SQL query and convert the result to a DataFrame
    with engine.connect() as connection:
        result = connection.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    # Save the DataFrame to a CSV file
    df.to_csv(os.path.join('results', f'{sql_file}.csv'), index=False)

    # If this is the 7th request, build a chart
    if sql_file == 'query_7.sql':
        print('Creating chart')

        df['growth_rate'] = df.groupby('product')['sales'].pct_change(fill_method='bfill')
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x='month', y='sales', hue='product')
        plt.title('Monthly Sales Trend for Each Product in 2020')
        plt.savefig(os.path.join('results', 'monthly_sales_report.png'))

