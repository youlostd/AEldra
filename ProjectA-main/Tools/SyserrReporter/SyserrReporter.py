import requests
import hashlib
import sys

if len(sys.argv) < 2 or sys.argv[1] != 'game':
  print "4"
  sys.exit(1)

if not os.path.exists("packet_errors.log"):
  print "5"
  sys.exit(1)

with open('packet_errors.log', 'r') as r:
  lines = "".join(r.readlines())

# cut too long texts...
if len(lines) > 2048:
  lines = lines[2048:]

md5 = hashlib.md5()
md5.update(lines + lines + "5")
hash = md5.hexdigest()

url = 'http://syserrreporter.aeldra.net/report.php'

post_data = {
          'sec' : hash,
          'reporter' : os.getenv('COMPUTERNAME') + ' @ ' + os.environ.get('USERNAME'),
          'data' : lines,
        }

print requests.post(url, data = post_data)
print "done"

os.remove("packet_errors.log")