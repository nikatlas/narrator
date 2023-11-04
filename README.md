![Test coverage](./assets/images/coverage.svg)

## Run Django server

Apply migrations:
```
make migrate
```

Run server:
```
make collectstatic
make runserver
```

Create test superuser for local development:
```
make createtestsuperuser
```
You will be prompted to give a password for the superuser.

After that you can log in to the admin panel with the superuser credentials.

Admin is located in `/admin` path.
