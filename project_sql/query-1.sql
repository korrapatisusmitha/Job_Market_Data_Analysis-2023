-- Top 10 highest-paying data analyst jobs 
SELECT 
     job_id,
     job_title,
	name as company_name,
	job_country,
     job_location, 
     job_schedule_type,
	job_via,
     job_posted_date,
     salary_year_avg
from 
    job_postings_fact
left join company_dim on company_dim.company_id = job_postings_fact.company_id
where job_title_short = 'Data Analyst' 
	and job_location = 'Anywhere'
	and salary_year_avg is not null
order by salary_year_avg desc
limit 10