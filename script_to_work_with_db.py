import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Загрузил переменные окружения из файла .env
load_dotenv()

# Создал подключение к базе данных
engine = create_engine(os.getenv('DB_DSN'))

# Получил список всех SQL-файлов в папке 'queries'
sql_files = [f for f in os.listdir('queries/') if f.endswith('.sql')]

for sql_file in sql_files:
    # Прочитал SQL-запрос из файла
    with open(os.path.join('queries', sql_file)) as f:
        query = text(f.read())

    # Выполнил SQL-запрос и преобразуй результат в DataFrame
    with engine.connect() as connection:
        result = connection.execute(query)
        df = pd.DataFrame(result.fetchall(), columns=result.keys())

    # Сохранил DataFrame в файл CSV
    df.to_csv(os.path.join('results', f'{sql_file}.csv'), index=False)

    # Если это 7-й запрос, построй график
    if sql_file == 'query_7.sql':
        df['growth_rate'] = df.groupby('product')['sales'].pct_change(fill_method='bfill')
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x='month', y='sales', hue='product')
        plt.title('Monthly Sales Trend for Each Product in 2020')
        plt.savefig(os.path.join('results', 'monthly_sales_report.png'))


