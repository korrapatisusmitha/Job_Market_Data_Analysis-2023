-- skill based on salary

select 
    skills,
    round(avg(salary_year_avg), 2 )as avg_salary
from job_postings_fact
inner join skills_job_dim skills_job on job_postings_fact.job_id = skills_job.job_id
inner join skills_dim skills on skills.skill_id = skills_job.skill_id
where 
    (job_title_short = %s or %s is null )
    AND salary_year_avg is not null
GROUP BY 
    skills
order by 
    avg_salary DESC
-- limit 25;