import os
from subprocess import PIPE, Popen, call
from sys import exit, platform

# subprocess.Popen is more general than subprocess.call.
# Popen doesn't block, allowing you to interact with the
# process while it's running, or continue with other things
# in your Python program; whereas call does block.

if platform in ["linux", "linux2", "darwin"]:
    os.system("ls -l /usr/bin/python")
    call("ls -l /usr/bin/python", shell=True)
    myprocess = Popen("ls -l /usr/bin/python", shell=True, stdin=PIPE, stdout=PIPE)
    output, err = myprocess.communicate()
    print("output==============\n", output)
    print("err=================\n", err)
elif platform == "win32":
    # print(os.system('dir /x C:\Python27'))
    # print(call('dir /x C:\Python27', shell=True))

    myprocess = Popen(r"diras /x C:\Python27", shell=True, stderr=PIPE, stdout=PIPE)
    output, err = myprocess.communicate()
    print("output==============\n", output.decode("utf-8"))
    print("err=================\n", err.decode("utf-8"))
else:
    print("unhandled platform :", platform)
    exit(1)
