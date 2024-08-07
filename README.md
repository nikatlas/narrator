Narrator brings AI characters and RPG campaings to life. 

- Create NPC and Player characters with custom background and knowledge.
- Discuss between one NPC and one Player character

- Custom RAG system with Qdrant Vector Database and PostgreSQL
- Abstract LLM interface with Langchain
- Custom Pipeline library for running complex tasks

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
