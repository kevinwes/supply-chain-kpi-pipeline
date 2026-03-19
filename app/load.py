import pandas as pd 
from pathlib import Path
import sqlite3

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR/"output"

def load_data(final_df):
    OUTPUT_DIR.mkdir(exist_ok=True) 
    final_df.to_csv(OUTPUT_DIR/"final_supply_chain.csv",index=False)
    conn = sqlite3.connect(OUTPUT_DIR/"supply_chain.db")
    final_df.to_sql("supply_chain_final",conn,if_exists="replace",index=False)
    conn.close()

    print("Load est complet")