from concurrent.futures import ThreadPoolExecutor
from datetime import *
import time
def pow(x):
    # time.sleep(1.0 / x )
    print (1.0 / x)
    return x+1

now = datetime.now()
with ThreadPoolExecutor(max_workers=5) as executor:

    for x in xrange(1,10):
        future = executor.submit(pow, x)
        pass

print datetime.now() - now
