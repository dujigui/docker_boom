import subprocess
import sys

n = int(sys.argv[1])
image = sys.argv[2]
cmd = ["docker", "run", "-itd", "-P", image]

def start():
    subprocess.call(cmd)


for i in range(n):
    start()
