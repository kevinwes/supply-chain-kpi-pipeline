from extract import extract_data
from transform import transform_data
from load import load_data
from analyze import run_analysis



def main():
    suppliers_df,warehouses_df,products_df,inventory_df,shipments_df = extract_data() 
    
    final_df = transform_data(suppliers_df,warehouses_df,products_df,inventory_df,shipments_df)
    load_data(final_df)

    run_analysis()


if __name__ == "__main__":
    main()