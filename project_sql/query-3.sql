-- demand count of skills for data analyst jobs 

SELECT 
    skills,
    count(skills_job.job_id) as demand_count
FROM 
    job_postings_fact
inner join skills_job_dim skills_job on job_postings_fact.job_id = skills_job.job_id
inner join skills_dim skills on skills.skill_id = skills_job.skill_id
where job_title_short = 'Data Analyst'
group by 
    skills
order by  
    demand_count DESC
limit 5;