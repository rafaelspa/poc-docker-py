import docker

client = docker.from_env()

# examples from https://github.com/sidpalas/devops-directive-docker-course/blob/main/03-installation-and-set-up/README.md

client.containers.run(
    "docker/whalesay", "cowsay Hello There")

client.containers.run(
    "postgres:15.1-alpine",
    environment=["POSTGRES_PASSWORD=foobarbaz"],
    ports={"5432/tcp": 5432},
    detach=True
)

for container in client.containers.list():
    container.stop()

client.containers.prune()