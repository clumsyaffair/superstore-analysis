import os

import pandas as pd
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.exc import DatabaseError
import matplotlib.pyplot as plt
from dotenv import load_dotenv


def load_and_clean(fl):
    try:
        try:
            df = pd.read_csv(fl, encoding='utf-16')
        except UnicodeDecodeError:
            df = pd.read_csv(fl, encoding='latin1')
        print('✅ File loaded successfully')

        # Handle nulls
        for col, count in df.isna().sum().items():
            if count > 0:
                if col in ['Order ID', 'Order Date']:
                    df[col] = df[col].fillna('unknown')
                    print(f'Filled nulls in {col}')
                else:
                    df.dropna(subset=[col], inplace=True)
                    print(f'Dropped nulls in {col}')

        # Date formatting
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Ship Date'] = pd.to_datetime(df['Ship Date'])

        # Derived fields
        df['Ship_Duration'] = (df['Ship Date'] - df['Order Date']).dt.days
        df['Profit_Margin'] = df['Profit'] / df['Sales']

        print(f"✅ Cleaning done | Rows left: {len(df)}")
        return df
    except Exception as e:
        print(f"❌ Error: {e}")


def sales_by_region_and_cat(df):
    return df.groupby(['Region','Category'], as_index=False)['Sales'].sum()


def data_to_sql(df):
    try:
        user=os.getenv("DB_USER")
        pas=os.getenv("DB_PASSWORD")
        host=os.getenv("DB_HOST")
        port=int(os.getenv("DB_PORT"))
        dbname=os.getenv('DB_NAME')
        eng = create_engine(f"mysql+pymysql://{user}:{pas}@{host}:{port}/{dbname}")
        df.to_sql(name='superstore', con=eng, if_exists='replace', index=False)
        print('✅ Data loaded to MySQL Workbench')
    except (FileNotFoundError, DatabaseError, Exception) as e:
        print(f"❌ SQL Error: {e}")


def chart_region_and_cat(df):
    try:
        pivot = df.pivot(index='Region', columns='Category', values='Sales').fillna(0)
        pivot.plot(kind='bar', stacked=True)
        plt.title("Sales by Region & Category")
        plt.xlabel('Region')
        plt.ylabel("Sales")
        plt.show(block=False)
        plt.pause(3)
        plt.close()
    except Exception as e:
        print(f"❌ Chart error: {e}")
