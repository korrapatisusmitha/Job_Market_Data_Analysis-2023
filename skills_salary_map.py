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
    
def fetch_skills_salary_map(role = None):
    query = load_query("queries/skills_salary_map.sql")
    params = (role, role)
    try:
        conn = get_db_connection()
        df = pd.read_sql_query(query, conn, params = params)
        conn.close()

        if df.empty:
            print("⚠ No data found for the given role.")
        else:
            print("📃 Skills and Salary range for the role:", role if role else "All Roles")
            print(df)
            df.to_csv("output/skills_salary_map.csv", index = False)
        
        return df

    except Exception as e:
        print("Error❌:", e)
        return pd.DataFrame()

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description = "Fetch the skills and salary range for seeking role")
#     parser.add_argument("--role", type = str, help = "Skills, salary map", default = None)
#     args = parser.parse_args()

#     role_input = args.role.strip() if args.role and args.role.strip() else None

#     fetch_skills_salary_map(role = role_input)