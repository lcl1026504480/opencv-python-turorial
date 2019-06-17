import subprocess
import os
main = "testmain.exe"
if os.path.exists(main):
    rc, out = subprocess.getstatusoutput(main)
    print('rc = %d, \nout = %s' % (rc, out))

print('*' * 10)
f = os.popen(main)
data = f.readlines()
f.close()
print(data)

print('*' * 10)
a = os.system(main)
print(a)
print('*' * 10 + "run")
subprocess.run(main)
print('*' * 10 + "call")
subprocess.call(main)
print('*' * 10 + "stdout")
res = subprocess.Popen(main, shell=True, stdout=subprocess.PIPE)
res.stdout.read()
res.stdout.close()
print(res.pid)
# print('*' * 10 + "stderr")
# res = subprocess.Popen(main, shell=True, stdout=subprocess.PIPE)
# res.stderr.read()
