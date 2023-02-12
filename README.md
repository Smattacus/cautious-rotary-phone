Hello world!

This repository is for simple testing of containerizing a CICD flow of a MVC application with a client view into the code.

Client <---RESTful (ideally) http calls ----> Application <---- Primarily ORM based interactions with ----> Database/Datastore (Redis in this particular case)

I want to have all of these start up in a container so I can run a battery of tests on the client and use the app and db as services for that client.

UPDATE: The way to do this I have found, currently, is this:

1. Create a docker compose file. Get this working on your local docker.
2. In the github action, use the docker container and build the docker compose with `docker compose build`
3. The subsequent github action step should then be `docker compose up --abort-on-container-exit --exit-code-from client`. This will bring up your docker container and run your tests.
4. A nonzero exit code from any container in the compose will cause your action to fail.

This has the following advantages:

1. I don't have to spend a lot of time messing around with github action's piecemeal interface/integration to containers; instead, I just call the Docker commands locally.
2. I can develop the bulk of the action locally (via Docker compose) and then creating the action itself is trivial. A big concern with developing github actions is that the dev TAT is slow from waiting for a runner, letting the runner run, wrap up, charging, poor local linting support, etc.

Discussion where I asked about making a service based on a Dockerfile: https://github.com/community/community/discussions/47105