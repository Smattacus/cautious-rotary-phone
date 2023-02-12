Hello world!

This repository is for simple testing of containerizing a CICD flow of a MVC application with a client view into the code.


Client <---RESTful (ideally) http calls ----> Application <---- Primarily ORM based interactions with ----> Database/Datastore (Redis in this particular case)

Note: Unfortunately, it looks like I'll have to go back to the drawing board. This is because the app container will just sit and wait in a workflow. Another idea is I can just run a docker compose that builds all three containers and runs the top level (client) "tests", and have that just be a simple step. Takes github step declarations mostly out of the equation anyways. Discussion where I asked about making a service based on a Dockerfile: https://github.com/community/community/discussions/47105