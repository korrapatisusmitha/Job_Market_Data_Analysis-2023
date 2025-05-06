# 📃 Data Job Market Analysis
Analyze 2023 job postings data to uncover 🤑top paying job roles, 🔥in-demand skills, and 💹salary trends using using SQL + Python + PostgreSQL + Pandas + Seaborn.

# 📂 Project Structure
```pgsql
job-market-analysis/
├── main.py
├── scripts/
│   ├── db_utils.py
│   ├── fetch_roles.py
│   ├── top_paying_jobs.py
│   ├── skills_required.py
│   ├── skills_demand.py
│   ├── skills_salary_map.py
│   ├── optimal_skills.py
│   └── visualizations.py
├── queries/
│   ├── top_paying_jobs.sql
│   ├── skills_required.sql
│   ├── skills_demand.sql
│   ├── skills_salary_map.sql
│   ├── optimal_skills.sql
├── output/
│   └── (csv files and generated charts)
├── requirements.txt
├── sql_load 
```
# 📁 Dataset Source

The dataset used in this project is from Data With [Luke Barousse 2023 Job Postings SQL Case Study](https://drive.google.com/drive/folders/1moeWYoUtUklJO6NJdWo9OV8zWjRn0rjN), part of his tutorials to analyse the data with SQL. All credit to [Luke Barousse](https://www.lukebarousse.com/) for curating this valuable resource.

# ⚙️ Setup Instructions

### 1. Clone the repository
```bash

  git clone https://github.com/your-username/sql_project_data_job_analysis.git

```
### 2. Install dependencies
```bash

  pip install -r requirements.txt

```
### 3. Set up your environment variables
```ini
DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432
```
✅ Note: Your .env file is excluded from Git using .gitignore for security.
# 🚀 Running the project
```bash

  python main.py

```
* You'll be shown a list of job roles.
* Then prompted to select from the 5 analysis options:
  1. 🔝 Top Paying Jobs
  2. 🛠  Skills Required for Top Paying Jobs
  3. 📊 Most In-Demand Skills
  4. 💰 Skills Based on Salary
  5. 🎯 Most Optimal SKills to Learn
* You’ll also be asked if you'd like to visualize the results (charts are saved in output/).
## ✅ Example
  ```bash
  💼 Enter the Job Role youre interested in (or press enter for all roles): Data Engineer

  Choose an Analysis to run:
  1. 🔝 Top Paying Jobs
  2. 🛠 Skills Required
  ...
  
  📊 Do you want to visualize the results? (y/n): y
  📊 Saved to output/top_paying_jobs.png
  ```

# 📊 Visualizations
This project uses `matplotlib` and `seaborn` for data visualizations. Charts include:
- **Bar Charts** (Top-paying jobs, Skills demand)

- **Horizontal Bars** (Skills required)

- **Scatter Plots** (Optimal Skills: Salary vs Demand)

# 🛠 Tools I used
For my deep dive into the job market analysis, I harnessed the power of several robust tools and technologies:

- **SQL:** The backbone of the analysis — used to extract, filter, and aggregate critical insights from structured job posting data.

- **PostgreSQL:** A powerful open-source relational database management system (RDBMS) chosen for storing and managing large-scale job postings data efficiently.

- **Python** (Pandas, Seaborn, Matplotlib): Used for data handling, analysis, and visualization — allowing for a smooth transition from raw data to compelling charts and insights.

- **Visual Studio Code:** My primary development environment — providing intelligent code editing, extensions, and seamless Git integration.

- **Git & GitHub:** Essential tools for version control and collaboration — Git for tracking changes locally, and GitHub for sharing and managing the project remotely.

- **dotenv:** For securely managing database credentials and configurations via environment variables.

- **RapidFuzz:** Integrated to enhance user input handling with fuzzy string matching, improving role suggestions even with minor typos.

- **Command-Line Interface (CLI):** Built using argparse to allow flexible and reusable script execution from the terminal, including dynamic role-based analysis and visualization prompts.

# 📚 What I Learned
This project was a comprehensive learning experience where I deepened my understanding of:

- **Data Engineering Practices:** Writing clean, modular, and maintainable code by separating logic, queries, and configurations.

- **Database Interaction:** Leveraging psycopg2 and SQL to extract structured insights from relational databases.

- **Data Analysis with Python:** Using pandas for data manipulation and performing role-based filtering and aggregation.

- **Visual Storytelling:** Creating impactful visualizations with matplotlib and seaborn to highlight trends in salary, skill demand, and optimal career paths.

- **User-Friendly CLI:** Building a smooth command-line experience using argparse, enabling both novice and technical users to analyze data interactively.

- **Error Handling and UX:** Implementing fuzzy string matching (via rapidfuzz) to gracefully handle typos in user inputs and improve the user experience.

# 🥁 Conclusion

  ## 📌 Insights
  The project extracted meaningful insights through five core analyses:

1. 🔝 **Top Paying Jobs:** Identified the highest-paying job titles across different roles and locations, helping users understand where premium compensation lies.

2. 🛠 **Skills Required for Top Paying Jobs:** Revealed which technical and soft skills are most frequently associated with high-paying positions.

3. 📈 **Most In-Demand Skills:** Measured skill popularity based on demand frequency, allowing job seekers to align with market needs.

4. 💰 **Skills Based on Salary:** Showcased which skills are linked with higher average salaries, supporting smarter upskilling decisions.

5. 🎯 **Optimal Skills to Learn:** Combined demand and salary data to highlight the best-value skills to learn — high reward, high opportunity.

  ## 💭 Closing Thoughts
This project gave me a real-world perspective on how data science and analytics can power career strategy. By blending SQL, Python, and visualization, I transformed raw job data into actionable intelligence. In a job market that evolves rapidly, such insights can empower individuals to make data-driven career decisions and stay ahead of industry trends.
