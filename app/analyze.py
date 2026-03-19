import pandas as pd 
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR/"output"

def run_analysis ():
    conn = sqlite3.connect(OUTPUT_DIR/"supply_chain.db")

    query_1 =""" Select product_name, 
    SUM(revenue) AS total_revenue
     FROM supply_chain_final 
     GROUP BY product_name
       ORDER BY total_revenue DESC  """ 
    
    query_2 = """Select warehouse_name, SUM(revenue) AS warehouse_revenue
    FROM supply_chain_final
    GROUP BY warehouse_name"""

    query_3 = """ Select product_name, AVG(fill_rate) AS avg_fill_rate
     FROM supply_chain_final 
      GROUP BY product_name
       ORDER BY avg_fill_rate DESC """
    query_4 = """ SELECT 
    COUNT(*) * 1.0 / (SELECT COUNT(*) 
    FROM supply_chain_final) AS on_time_rate
    FROM supply_chain_final
    WHERE status = 'on_time'"""
    
    result_1 = pd.read_sql_query(query_1,conn)
    result_2 = pd.read_sql_query(query_2,conn)
    result_3 = pd.read_sql_query(query_3,conn)
    result_4 = pd.read_sql_query(query_4,conn)

    print("\n revenue par produit")
    print(result_1)


    print("\n revenue par entrepot")
    print(result_2)

    print("\n taux moyen de fill rate par produit")
    print(result_3)
    
    print("\n taux de livraison à l'heure")
    print(result_4)

    conn.close()

    


