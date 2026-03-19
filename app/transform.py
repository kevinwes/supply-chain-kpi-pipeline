import pandas as pd 

def transform_data(suppliers_df, warehouses_df , products_df , inventory_df , shipments_df) :
   
    products_suppliers_df = products_df.merge(suppliers_df, on ="supplier_id", how="left")
    final_df = shipments_df.merge(products_suppliers_df,on="product_id",how="left")
    final_df = final_df.merge(warehouses_df,on="warehouse_id",how="left")
    print(final_df.columns)
    final_df["revenue"] = final_df["quantity_delivered"] * final_df["unit_price"] 
    final_df["actual_delivery_date"] = pd.to_datetime(final_df["actual_delivery_date"])
    final_df["expected_delivery_date"] = pd.to_datetime(final_df["expected_delivery_date"])

    final_df["delay"] = (final_df["actual_delivery_date"] - final_df["expected_delivery_date"]).dt.days
    final_df["fill_rate"] = final_df["quantity_delivered"] / final_df["quantity_shipped"]
    final_df = final_df.dropna()

    print("Transform est complet")
    return final_df

   