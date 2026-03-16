import pandas as pd
from sqlalchemy import create_engine
import os

# Full path to database
db_path = r"C:\Users\rohan\OneDrive\Desktop\Projects_AIML\Ecommerce_EDA_And_Dashboard\ecommerce.db"

engine = create_engine(f"sqlite:///{db_path}")

data_path = "Ecommerce_EDA_And_Dashboard/data/raw"

for file in os.listdir(data_path):
    
    if file.endswith(".csv"):
        
        table_name = file.replace(".csv","")
        
        file_path = os.path.join(data_path, file)
        
        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} table created with {len(df)} rows")