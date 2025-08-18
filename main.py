import os
from dotenv import load_dotenv

# load env variables before anything else
load_dotenv()
import pandas as pd
from superstore.python.cleanandoperations import (
    load_and_clean as ld,
    sales_by_region_and_cat as sl,
    data_to_sql as dq,
    chart_region_and_cat as cht
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)

cl = ''

if __name__ == "__main__":
    while True:
        print("\n------ Superstore Menu ------")
        print('1. Clean data and save to new file')
        print('2. See region & category-wise performance')
        print('3. Load cleaned data to SQL')
        print('4. Visualize sales by region and category')
        print('5. Exit')

        try:
            ch = int(input('Enter your choice: '))
        except ValueError as e:
            print('❌ Invalid input, please enter a number.', e)
            continue

        if ch == 1:
            file_path = os.path.join(DATA_DIR, "Superstore.csv")
            ob = ld(file_path)
            if ob is not None:
                print(ob.head())
                cl = os.path.join(DATA_DIR, "Cleaned.csv")
                ob.to_csv(cl, index=False)
                print(f'✅ Cleaned data saved to {cl}')
            else:
                print("⚠️ Could not load data.")

        elif ch == 2:
            cleaned_path = os.path.join(DATA_DIR, "Cleaned.csv")
            if  os.path.exists(cleaned_path):
                df = pd.read_csv(cleaned_path)
                ob = sl(df)
                summary_path = os.path.join(DATA_DIR, "Sales_by_reg_cat.csv")
                ob.to_csv(summary_path,index=False)
                print(f'✅ Result saved to {summary_path}')
            else:
                print('⚠️ First clean the data.')

        elif ch == 3:
            cleaned_path = os.path.join(DATA_DIR, "Cleaned.csv")

            if  os.path.exists(cleaned_path):
                df = pd.read_csv(cleaned_path)
                dq(df)
            else:
                print('⚠️ First clean the data.')

        elif ch == 4:
            summary_path = os.path.join(DATA_DIR, "Sales_by_reg_cat.csv")
            if os.path.exists(summary_path):
                df = pd.read_csv(summary_path)
                cht(df)
            else:
                print('⚠️ Run option 2 first to generate summary file.')

        elif ch == 5:
            print("👋 Exiting program.")
            break
