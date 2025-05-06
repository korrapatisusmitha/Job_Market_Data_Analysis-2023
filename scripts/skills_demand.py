import os
import pandas as pd
from scripts.db_utils import get_db_connection
# import argparse
import warnings

# to surpass the warnings
warnings.filterwarnings("ignore")

# to create the folder if not exists
os.makedirs("output", exist_ok = True)

def load_query(file_path):
    with open (file_path, 'r') as file:
        return file.read()
    
def fetch_skills_demand(role = None):
    query = load_query("queries/skills_demand.sql")
    params = (role, role)
    try:
        conn = get_db_connection()
        df = pd.read_sql_query(query, conn, params = params)
        conn.close()

        if df.empty:
            print("⚠ No data found for the given role.")
        else:
            print("📃 Skills demand for role:", role if role else "All Roles")
            print(df)
            df.to_csv("output/skills_demand.csv", index = False)
        
        return df

    except Exception as e:
        print("Error❌:", e)
        return pd.DataFrame()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description = "Fetch the skills demand.")
#     parser.add_argument("--role", type = str, help = "Skills Count", default = None)
#     args = parser.parse_args()

#     role_input = args.role.strip() if args.role and args.role.strip() else None

#     fetch_skills_required(role = role_input)