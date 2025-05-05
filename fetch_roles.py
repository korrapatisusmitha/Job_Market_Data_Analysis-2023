import pandas as pd
import os
from db_utils import get_db_connection
import warnings

# surpass the warnings
warnings.filterwarnings("ignore")

# Auto-create output-folder
os.makedirs("output", exist_ok = True)

def fetch_job_roles():
    query = """
        select distinct job_title_short
        from job_postings_fact
        where job_title_short is not null
        order by job_title_short;
    """

    try:
        conn = get_db_connection()
        df_roles = pd.read_sql_query(query, conn)
        conn.close()
        print("📃 Unique Job Roles Found: ")
        print(df_roles)
        df_roles.to_csv("output/job_roles.csv", index = False)
    except Exception as e:
        print(f"Error❌: {e}")

def get_valid_roles():
    """Returns a set of valid roles for validation process"""

    query = """
        select distinct job_title_short
        from job_postings_fact
        where job_title_short is not null;
    """
    try:
        conn = get_db_connection()
        df = pd.read_sql_query(query, conn)
        conn.close()

        return df['job_title_short'].tolist()
    except Exception as e:
        print("❌ Error fetching valid roles: ", e)
        return []
    
# if __name__ == "__main__":
#     fetch_job_roles()