# The project is built using docker-compose, with the following commands:

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