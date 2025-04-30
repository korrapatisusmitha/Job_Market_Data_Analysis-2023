-- top paying jobs for data analysts with the skills needed

select 
    top_paying_jobs.*,
    string_agg(skills.skills, ', ') as skills 
from (
        SELECT 
            job_id,
            job_title,
            name as company_name,
            salary_year_avg
        from 
            job_postings_fact
        left join company_dim as company on company.company_id = job_postings_fact.company_id
        where 
            (job_title_short = %s or %s is null)
            -- and  job_location = 'Anywhere'
            and salary_year_avg is not null

        order by salary_year_avg desc
        limit 10
) as top_paying_jobs
inner join skills_job_dim skills_job on skills_job.job_id = top_paying_jobs.job_id
inner join skills_dim skills on skills.skill_id = skills_job.skill_id
group by 
	top_paying_jobs.job_id,
	top_paying_jobs.job_title,
	top_paying_jobs.company_name,
	top_paying_jobs.salary_year_avg
order by 
    salary_year_avg desc


-- ===========================================================================
/*
select 
    top_paying_jobs.*,
    skills 
from (
        SELECT 
            job_id,
            job_title,
            name as company_name,
            job_country,
            job_location, 
            job_schedule_type,
            salary_year_avg
        from 
            job_postings_fact
        left join company_dim as company on company.company_id = job_postings_fact.company_id
        where job_title_short = 'Data Analyst' and  
              job_location = 'Anywhere' and 
              salary_year_avg is not null
        order by salary_year_avg desc
        limit 10
) as top_paying_jobs
inner join skills_job_dim skills_job on skills_job.job_id = top_paying_jobs.job_id
inner join skills_dim skills on skills.skill_id = skills_job.skill_id
order by 
    salary_year_avg desc


-- ==================================================================================
with top_paying_jobs as (
    
        SELECT 
            job_id,
            job_title,
            name as company_name,
            job_country,
            job_location, 
            job_schedule_type,
            salary_year_avg
        from 
            job_postings_fact
        left join company_dim as company on company.company_id = job_postings_fact.company_id
        where 
            job_title_short = 'Data Analyst' 
            and job_location = 'Anywhere'
            and salary_year_avg is not null
        order by 
            salary_year_avg desc
        limit 10
)

select 
    top_paying_jobs.*,
    skills
from 
    top_paying_jobs
inner join skills_job_dim skills_job on skills_job.job_id = top_paying_jobs.job_id
inner join skills_dim skills on skills.skill_id = skills_job.skill_id
order by 
    salary_year_avg desc
*/