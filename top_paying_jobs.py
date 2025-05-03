import pandas as pd
import os
from db_utils import get_db_connection
import argparse
import warnings 

# to surpass the warnings
warnings.filterwarnings("ignore")

# to create the folder if not exists
os.makedirs("output", exist_ok = True)

def load_query(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def fetch_top_paying_jobs(role = None):
    query = load_query("queries/top_paying_jobs.sql")
    params = (role, role)

    try:
        conn = get_db_connection()
        df = pd.read_sql_query(query, conn, params = params)
        conn.close()

        if df.empty:
            print("⚠ No data found for the given role.")

        else:
            print("📃 Top Paying Job for the role:", role if role else "All Roles")
            print(df)
            df.to_csv("output/top_paying_job_role.csv", index = False)
        
        return df 
    
    except Exception as e:
        print("Error❌:", e)
        return pd.DataFrame()

"""
CLI usage: python top_payingjobs.py --role "Data Analyst" for particular role 
                                (or)
python top_payingjobs.py --role "" provides for all the roles
"""

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description =" Fetch top paying jobs.")
#     parser.add_argument("--role", type = str, help = "Job role to analyze", default = None)
#     args = parser.parse_args()

#     # Clean up whitespace — treat empty input as None
#     role_input = args.role.strip() if args.role and args.role.strip() else None

#     fetch_top_paying_jobs(role = role_input)
