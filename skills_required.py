import os
import pandas as pd
from db_utils import get_db_connection
import warnings
import argparse

# to surpass the warnings
warnings.filterwarnings("ignore")

# to create the "output" folder it not exists
os.makedirs("output", exist_ok = True)

def load_query(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def fetch_skills_required(role = None):
    query = load_query("queries/skills_required.sql")
    params = (role, role)
    try:
        conn = get_db_connection()
        df = pd.read_sql_query(query, conn, params = params)
        conn.close()

        if df.empty:
            print("⚠ No data found for the given role.")

        else:
            print("📃 Skills required for the role:", role if role else "All Roles")
            print(df)
            df.to_csv("output/skills_required.csv", index = False)
        
        return df

    except Exception as e:
        print("Error❌:", e)
        return pd.DataFrame()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description = "Most IN-Demand skills for the seeking role.")
#     parser.add_argument("--role", type = str, help = "Skills requirement", default = None)
#     args = parser.parse_args()

#     role_input = args.role.strip() if args.role and args.role.strip() else None

#     fetch_skills_required(role = role_input)