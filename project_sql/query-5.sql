with skill_demand as (
    SELECT 
        skills.skill_id,
        skills.skills,
        count(skills_job.job_id) as demand_count
    FROM 
        job_postings_fact
    inner join skills_job_dim skills_job on job_postings_fact.job_id = skills_job.job_id
    inner join skills_dim skills on skills.skill_id = skills_job.skill_id
    where 
        job_title_short = 'Data Analyst' AND
        salary_year_avg is not  null AND
        job_work_from_home = True
    group by 
        skills.skill_id
) , average_salary as (
    select 
        skills_job.skill_id,
        round(avg(salary_year_avg), 2 )as avg_salary
    from job_postings_fact
    inner join skills_job_dim skills_job on job_postings_fact.job_id = skills_job.job_id
    inner join skills_dim skills on skills.skill_id = skills_job.skill_id
    where 
        job_title_short = 'Data Analyst' AND  
        salary_year_avg is not null AND
        job_work_from_home = TRUE
    GROUP BY 
        skills_job.skill_id
)
select
    skill_demand.skill_id,
    skill_demand.skills,
    demand_count,
    avg_salary
from skill_demand
inner join average_salary on average_salary.skill_id = skill_demand.skill_id
where demand_count > 10
order BY
    avg_salary desc,
    demand_count desc
limit 25;

-- ================================================================================

SELECT
    skills_dim.skill_id,
    skills_dim.skills,
    count(skills_job_dim.job_id) as demand_count,
    round(avg(job_postings_fact.salary_year_avg), 2) as average_salary
from job_postings_fact
inner join skills_job_dim on job_postings_fact.job_id = skills_job_dim.job_id
inner join skills_dim on skills_job_dim.skill_id = skills_dim.skill_id
where 
    job_title_short = 'Data Analyst' AND
    salary_year_avg is not null AND
    job_work_from_home = TRUE
group by
    skills_dim.skill_id
HAVING
    count(skills_job_dim.job_id) > 10
order by 
    average_salary DESC,
    demand_count DESC
limit 25;