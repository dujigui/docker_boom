import subprocess


def stop(c):
    subprocess.call(["docker", "container", "stop", c])
    return


def rm(c):
    subprocess.call(["docker", "container", "rm", c])
    return

print("remove all running container?!!(yes|no)")
confirm = input()
if confirm != "yes":
    exit()

output = subprocess.check_output(["docker", "ps", "-q"]).decode("utf-8")
container_list = output.split("\n")
container_list.remove("")

for container in container_list:
    stop(container)
    rm(container)
