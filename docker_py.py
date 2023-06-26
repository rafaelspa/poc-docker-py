import docker

# from docs at https://github.com/docker/docker-py

def main():
    print("## Docker Py env")
    client = docker.from_env()
    print(client.api, "\n")

    print('## Container creation: client.containers.run("ubuntu:latest", "echo hello world")')
    print(client.containers.run("ubuntu:latest", "echo hello world"), "\n")

    print('## Run container in background:')
    client.containers.run("bfirsh/reticulate-splines", detach=True)
    print('"client.containers.run("bfirsh/reticulate-splines", detach=True)"', "\n")

    print("## Container list")
    containerList = client.containers.list()
    print(containerList, "\n")

    ## Manage containers
    container = client.containers.get(client.containers.list()[0].short_id)
    print('## Managing container "', container.short_id, '"')
    print('# config image\n',container.attrs['Config']['Image'])
    print('# logs\n',container.logs())
    print()

    print("## Stopping containers")
    for container in containerList:
        container.stop()
    print()

    # Removing all containers not used
    client.containers.prune()

    ## Stream logs
    # for line in container.logs(stream=True):
    # ...   print(line.strip())

    ## Manage images
    print("## Pulling nginx image")
    print(client.images.pull('nginx'), '\n')

    print("## Listing images")
    print(client.images.list(), "\n")

if __name__ == "__main__":
    main()