import os

exits = os.popen('docker ps -a --format "{{.Names}}" --filter "status=exited"')
# active = os.popen('docker ps -a --format "{{.Names}}" --filter "status=running"')

print(exits.read())
# print(active.read())