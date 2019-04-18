import psutil
import subprocess

subprocess.call(["free", "-m"])
print("Cpu:" + str(psutil.cpu_percent(interval=1)))
subprocess.call(["df", "-h"])