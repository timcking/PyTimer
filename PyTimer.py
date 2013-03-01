# Demo of a Python Timer class
import sys
import time
from random import randint

class Timer:    
    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start
        
def main(iRuns):
    iHeads = 0
    iTails = 0
    print "New Run"
    
    try:
        with Timer() as t:    
            for i in range(1, iRuns):
                randnum = randint(2, 999)
        
                if randnum%2 == 0:
                    iHeads += 1
                else:
                    iTails += 1        
            
            print("Heads: %s" % iHeads)
            print("Tails: %s" % iTails)
            print("Difference: %s" % str(iHeads - iTails))
            
    finally:
        print('Request took %.03f sec.' % t.interval)

if __name__ == '__main__':
    if len(sys.argv) <> 2:
        print 'Usage: ' + sys.argv[0] + ' runs'
        sys.exit(1)        
        
    iRuns = int(sys.argv[1])
        
    main(iRuns)    
    