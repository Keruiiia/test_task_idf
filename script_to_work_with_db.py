import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
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
    df.to_csv(os.path.join('results', f'result_{sql_file[:-4]}.csv'), index=False)

    # If this is the 7th request, build a chart
    if sql_file == 'query_7.sql':
        print('Creating chart')

        df['growth_rate'] = df.groupby('product')['sales'].pct_change() * 100
        df['month'] = pd.to_datetime(df['month'], format='%Y-%m-%d')
        # Сгруппируйте данные по продукту и сумме продаж
        grouped_df = df.groupby('product')['sales'].sum().sort_values(ascending=False)

        # Получите общее количество уникальных товаров
        count_products = df['product'].nunique()

        # Создайте графики по 10 товаров в каждом
        for i in range(count_products // 10 + (count_products % 10 > 0)):
            print(f'ploting {i}st chart')
            # Выберите 10 товаров для этого графика
            products = grouped_df[i * 10:(i + 1) * 10].index
            filtered_df = df[df['product'].isin(products)]

            plt.figure(figsize=(12, 6))
            sns.lineplot(data=filtered_df, x='month', y='sales', hue='product')
            sns.scatterplot(data=filtered_df, x='month', y='sales', hue='product', legend=False)

            # Установите формат меток оси x на месяцы
            ax = plt.gca()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%B'))

            # Переместите легенду в верхний правый угол и уменьшите размер текста
            plt.legend(loc='upper right', fontsize='small')

            # Измените формат чисел на оси y на миллионы и используйте логарифмическую шкалу
            fmt = '{x:,.2f}'
            tick = mtick.StrMethodFormatter(fmt)
            ax.yaxis.set_major_formatter(tick)

            # Добавьте название графика для навигации
            name_chart = f'Chart {i + 1}: Sales from {grouped_df[min((i + 1) * 10 - 1, count_products - 1)]} to {grouped_df[i * 10]}'
            plt.title(name_chart)

            plt.savefig(os.path.join('results/charts', f'{name_chart}.png'))

