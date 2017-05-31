# TO DO:
- [ ] Environment variables for all the things.

## Developing locally with postgresql
Insecure local setup. Wooo.
Check if you need postgresql service running locally, or change the port in django settings.
```
docker run --rm --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=postgres postgres:alpine
python manage.py migrate
```