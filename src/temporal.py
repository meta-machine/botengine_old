from datetime import datetime
import time

(dt, micro) = datetime.utcnow().strftime('%Y%m%d%H%M%S.%f').split('.')
#dt = "%s%03d" % (dt, int(micro) / 1000)
print(dt+'.'+micro)

#print ("%.5f" % time.time())
print (datetime.utcnow().time())