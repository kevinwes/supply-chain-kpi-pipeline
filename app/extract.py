import pandas as pd 
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR/"data"

def extract_data():
    suppliers_df = pd.read_csv(DATA_DIR/"suppliers.csv")
    warehouses_df = pd.read_csv(DATA_DIR/"warehouses.csv")
    products_df = pd.read_csv(DATA_DIR/"products.csv")
    inventory_df = pd.read_csv(DATA_DIR/"inventory.csv")
    shipments_df = pd.read_csv(DATA_DIR/"shipments.csv")

    print("Extract complete")

    return suppliers_df, warehouses_df , products_df , inventory_df , shipments_df

