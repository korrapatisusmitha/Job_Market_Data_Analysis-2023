import matplotlib.pyplot as plt
import seaborn as sns


def visualize_top_jobs(df):
    if df.empty:
        print("⚠️ No data avaliable for visualization.")
        return
    df_sorted = df.sort_values(by = 'salary_year_avg', ascending = False)

    plt.figure(figsize=(12,6))
    sns.barplot(
        data = df_sorted,
        y = "job_title",
        x = "salary_year_avg",
        hue = "company_name",
        dodge = False,
        palette = "viridis"
    )

    plt.title("Top paying jobs by salary")
    plt.xlabel("Average Salary (USD/year)")
    plt.ylabel("Job Title")
    plt.legend(title="Company", bbox_to_anchor=(1.05,1), loc = 'upper left')
    plt.tight_layout()
    plt.savefig("output/top_paying_jobs.png")
    print("📊 Saved to output/top_payings_jobs.png")
    plt.show()

def visualize_skills_required(df):
    if df.empty:
        print("⚠️ No data found for visualization.")
        return
    
    plt.figure(figsize=(12,6))
    sns.countplot(
        data = df,
        y = "skills",
        order = df['skills'].value_counts().index,
        palette = "crest"
    )

    plt.title("Most Frequent Skills in Top Paying Jobs")
    plt.xlabel("Frequency")
    plt.ylabel("Skills")
    plt.tight_layout()
    plt.savefig("output/skills_required.png")
    print("📊 Saved to output/skills_required.png")
    plt.show()

def visualize_demand_skills(df):
    if df.empty:
        print("⚠️ No data found for visualization.")
        return
    
    df_sorted = df.sort_values("demand_count", ascending = False)

    plt.figure(figsize=(12,8))
    sns.barplot(
        data = df_sorted,
        x = "demand_count",
        y = "skills",
        palette="magma"
    )

    plt.title("Most In-Demand Skills")
    plt.xlabel("Job Postings Count")
    plt.ylabel("Skills")
    plt.tight_layout()
    plt.savefig("output/demand_skills.png")
    print("📊 Saved to output/demand_skills.png")
    plt.show()

def visualize_skills_salary(df):
    if df.empty:
        print("⚠️ No data available for visualization.")
        return

    df_sorted = df.sort_values("avg_salary", ascending=True)

    plt.figure(figsize=(12, 8))
    sns.barplot(
        data=df_sorted,
        x="avg_salary",
        y="skills",
        palette="viridis"
    )

    plt.title("Skills with Highest Average Salary")
    plt.xlabel("Average Salary (USD/year)")
    plt.ylabel("Skills")
    plt.tight_layout()
    plt.savefig("output/skills_salary.png")
    print("📊 Saved to output/skills_salary.png")
    plt.show()

def visualize_optimal_skills(df):
    if df.empty:
        print("⚠️ No data available for visualization.")
        return

    plt.figure(figsize=(12, 8))
    sns.scatterplot(
        data=df,
        x="demand_count",
        y="average_salary",
        hue="skills",
        size="demand_count",
        palette="tab10",
        legend=False
    )

    plt.title("Optimal Skills: Salary vs. Demand")
    plt.xlabel("Demand Count")  
    plt.ylabel("Average Salary")
    plt.tight_layout()
    plt.savefig("output/optimal_skills.png")
    print("📊 Saved to output/optimal_skills.png")
    plt.show()