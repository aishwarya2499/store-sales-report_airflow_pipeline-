An Apache Airflow pipeline for automating the ETL workflow of store sales data being the Point Of Sales(POS) with raw csv data file as input.
The DAG orchestrates extraction from source systems, applies transformations and loads cleaned data as a csv file

🔹 Arhitecture:

  •	Reading the input csv file and transforming the raw data into cleaned data
  
  •	Saving the cleaned data into MySQL table
  
  •	Generating location wise and Store wise profit and saving the results as csv 
  
  •	Scheduling SMTP enabling to send reports as a mail when the DAG is run (either manually or scheduled)

🔹 Features:

•	Daily schedules DAG for store sales data processing
  
•	Built with BashOperators, PythonOperators for flexibilty
 
•	Ensures dependency management and retries on failure
 
•	Designed for scalability and production-ready orchestration
 
🔹 Use Case:

Generates a daily store sales report pipeline, enabling data teams to monitor sales trends, ensure data quality and prepare datasets for BI dashboards.
