import pandas as pd
from rapidfuzz import process
from scripts.fetch_roles import fetch_job_roles, get_valid_roles
from scripts.top_paying_jobs import fetch_top_paying_jobs
from scripts.skills_required import fetch_skills_required
from scripts.skills_demand import fetch_skills_demand
from scripts.skills_salary_map import fetch_skills_salary_map
from scripts.optimal_skills import fetch_optimal_skills
from scripts.visualizations import(
    visualize_top_jobs,
    visualize_skills_required,
    visualize_skills_demand,
    visualize_skills_salary,
    visualize_optimal_skills
)

def suggest_closest_role(user_input, valid_roles):
    # Ensure user_input is a string and strip extra spaces
    user_input = str(user_input).strip().lower()

    # Extract best match from the valid roles
    match, score, _ = process.extractOne(user_input, valid_roles)
    
    # Return match if the score is above threshold, else return None
    if score >= 70:  # 70+ is a reasonable match threshold
        return match
    return None

def prompt_visualization():
    response = input("\n📊 Do you wan to visualize the resultls? (y/n): ").lower().strip()
    return response == 'y'

def main():
    # Fetch and display job roles
    fetch_job_roles()
    valid_roles = get_valid_roles()  # Fetch valid roles from DB
    valid_roles_clean = [r.lower().strip() for r in valid_roles]

    # User input for job role
    role = input("\n💼 Enter the Job Role you're interested in (or press enter for all roles): ").strip()
    role_clean = role.lower().strip()

    if role and role_clean not in valid_roles_clean:
        suggestion = suggest_closest_role(role_clean, valid_roles)
        if suggestion:
            print(f"\n🤔 Did you mean '{suggestion}'? Running with suggested role.")
            role_param = suggestion
        else:
            print(f"\n❌ '{role}' not found in available roles. Please check and try again.")
            return
    else:
        role_param = role if role else None

    # Proceed with the rest of the script (Fetching data, visualization, etc.)
    print(f"Proceeding with the role: {role_param}")
            
    
    print("\nChoose an Analysis to run: ")
    print("1. 🔝 Top Paying Jobs")
    print("2. 🛠  Skills Required for Top Paying Jobs")
    print("3. 📊 Most In-Demand Skills")
    print("4. 💰 Skills Based on Salary")
    print("5. 🎯 Most Optimal SKills to Learn")
    choice = input("Enter your Choice (1 - 5): ").strip()

    if choice == '1':
        df = fetch_top_paying_jobs(role_param)
        if prompt_visualization():
            visualize_top_jobs(df)

    elif choice == '2':
        df = fetch_skills_required(role_param)
        if prompt_visualization():
            visualize_skills_required(df)

    elif choice == '3':
        df = fetch_skills_demand(role_param)
        if prompt_visualization():
            visualize_skills_demand(df)

    elif choice == '4':
        df = fetch_skills_salary_map(role_param)
        if prompt_visualization():
            visualize_skills_salary(df)

    elif choice == '5':
        df = fetch_optimal_skills(role_param)
        if prompt_visualization():
            visualize_optimal_skills(df)

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()



