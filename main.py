import pandas as pd
from fetch_roles import fetch_job_roles
from top_paying_jobs import fetch_top_paying_jobs
from skills_required import fetch_skills_required
from skills_demand import fetch_skills_demand
from skills_salary_map import fetch_skills_salary_map
from optimal_skills import fetch_optimal_skills
from visualizations import(
    visualize_top_jobs,
    visualize_skills_required,
    visualize_demand_skills,
    visualize_skills_salary,
    visualize_optimal_skills
)

def prompt_visualization():
    response = input("\n📊 Do you wan to visualize the resultls? (y/n): ").lower().strip()
    return response == 'y'

def main():
    print("\n🔎 Avaliable Job Roles are: \n")
    fetch_job_roles()

    role = input("\n💼 Enter the Job Role You're interested in (or press enter for all the avaliable Roles): ").strip()
    role = role if role else None
    print(role)
    
    print("\nChoose an Analysis to run: ")
    print("1. Top Paying Jobs")
    print("2. Skills Required for Top Paying Jobs")
    print("3. Most In-Demand Skills")
    print("4. Skills Based on Salary")
    print("5. Most Optimal SKills to Learn")
    choice = input("Enter your Choice (1 - 5): ").strip()

    if choice == '1':
        df = fetch_top_paying_jobs(role)
        if prompt_visualization():
            visualize_top_jobs(df)

    elif choice == '2':
        df = fetch_skills_required(role)
        if prompt_visualization():
            visualize_skills_required(df)

    elif choice == '3':
        df = fetch_skills_demand(role)
        if prompt_visualization():
            visualize_demand_skills(df)

    elif choice == '4':
        df = fetch_skills_salary_map(role)
        if prompt_visualization():
            visualize_skills_salary(df)

    elif choice == '5':
        df = fetch_optimal_skills(role)
        if prompt_visualization():
            visualize_optimal_skills(df)

    else:
        print("❌ Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()



