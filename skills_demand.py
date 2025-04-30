import os
import pandas as pd
from db_utils import get_db_connection
import argparse
import warnings

warnings.filterwarnings("ignore")

os.makedirs("output", exist_ok = True )

def load_query(file_path):
    with open (file_path, 'r') as file:
        return file.read()
    
def fetch_skills_required(role = None):
    query = load_query("queries/demand_skills.sql")
    params = (role, role)
    try:
        conn = get_db_connection()
        df = pd.read_sql_query(query, conn, params = params)
        conn.close()
        print("📃 Skills demand for role:", role if role else "All Roles")
        print(df)
        df.to_csv("output/skills_demand.csv", index = False)
        if df.empty:
            print("⚠ No data found for the given role.")

    except Exception as e:
        print("Error❌:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Fetch the skills demand.")
    parser.add_argument("--role", type = str, help = "Skills Count", default = None)
    args = parser.parse_args()

    role_input = args.role.strip() if args.role and args.role.strip() else None

    fetch_skills_required(role = role_input)