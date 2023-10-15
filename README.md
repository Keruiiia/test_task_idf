## Introduction
In this project, I have executed several sql queries against the database. The results of the queries are saved as .csv files for future convenient use. 

Then I created a report that shows the monthly sales trend for each product in 2020. To do this, I created a table with 4 columns: month, products, sales (quantity * amount), and growth rate (percentage change from the previous 
months). After that I built graphs for each group of products grouped by sales. 
Since there were 197 unique products in the table, it was decided to make a graph for every 10 products for clarity.

<img src="https://github.com/Keruiiia/test_task_idf/blob/dca9a1c34eab747ee1ee43a94a760a47885c2aa8/img.png" width=20% height=20%>

For convenience, the project was built using docker compose.

***
### Project structure


| Name                                                                                                                                          | Description                                                                             |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [data/](https://github.com/Keruiiia/test_task_idf/blob/b8f0c76f2b3dfa6b74f42c3c604293d67795a730/data)                                         | Folder with dump of database                                                            |                                              |
| [queries/](https://github.com/Keruiiia/test_task_idf/blob/221bc3c238d939eb5e483be8a9d5adb91d880d8a/queries)                                   | Foler with queries to database                                                          |
| [results/](https://github.com/Keruiiia/test_task_idf/blob/221bc3c238d939eb5e483be8a9d5adb91d880d8a/results)                                   | Folder with results of queries in .csv files                                            |
| [results/charts/](https://github.com/Keruiiia/test_task_idf/blob/221bc3c238d939eb5e483be8a9d5adb91d880d8a/results/charts)                     | Folder with charts of report sales                                                      |
| [.env](https://github.com/Keruiiia/test_task_idf/blob/b8f0c76f2b3dfa6b74f42c3c604293d67795a730/.env)                                          | It usually added to .gitignore but in this case it is visible for verification purposes |                                              |
| [requirements.txt](https://github.com/Keruiiia/test_task_idf/blob/b8f0c76f2b3dfa6b74f42c3c604293d67795a730/requirements.txt)                  | File with the list of required libraries for project operation                          |
| [script_to_work_with_db.py](https://github.com/Keruiiia/test_task_idf/blob/681d192f7a69096226f0e4274ff94a5ea71d9e47/script_to_work_with_db.py) | A Python script to execute SQL queries and generate a sales report.                                                                                        |
***
### The project is built using docker-compose, with the following commands:
Create and start containers:
```
docker compose up -d --build
```
Import database dump:
```
docker compose exec -T db mysql -uroot -prootpassword sales < data/db_dump_version_2.sql
```
Run main python script:
```
docker compose run --rm app python script_to_work_with_db.py
```

While writing queries, I noticed a possible typo in the custmer_name field of the customers table.

<img src="https://github.com/Keruiiia/test_task_idf/blob/eb884a6ceefd2df8a8e7e48b71da2657f489510c/img_1.png" width=20% height=20%>
