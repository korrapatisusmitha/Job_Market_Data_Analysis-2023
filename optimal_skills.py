import os
import pandas as pd
from db_utils import get_db_connection
import argparse
import warnings

warnings.filterwarnings("ignore")

os.makedirs("output", exist_ok = True)

def load_query(file_path):
    with open (file_path, 'r') as file:
        return file.read()
    
def fetch_optimal_skills(role = None):
    query = load_query("queries/optimal_skills.sql")
    params = (role, role)

    try:
        conn = get_db_connection()
        df = pd.read_sql_query(query, conn, params = params)
        conn.close()

        if df.empty:
            print("⚠ No data found for the given role")
        else:
            print("📃 Optimal skills and salary for the role:", role if role else "All Roles")
            print(df)
            df.to_csv("output/optimal_skills.csv", index = False)
        
        return df
        
    except Exception as e:
        print("Error❌:", e)
        return pd.DataFrame()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description= "High demand Skills and Salary")
#     parser.add_argument('--role', type= str, help="optimal skills and salary", default= None )
#     args = parser.parse_args()

#     role_input = args.role.strip() if args.role and args.role.strip() else None

#     fetch_optimal_skills(role = role_input)