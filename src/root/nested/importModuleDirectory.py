'''
Created on 13/04/2012

@author: jmrua
'''

import os, sys, inspect
from UserDict import UserDict



if __name__ == '__main__':
    cmd_folder = os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0])
    print str(inspect.currentframe())
    print str(inspect.getfile(inspect.currentframe()))
    print str(os.path.split(inspect.getfile(inspect.currentframe())))
    if cmd_folder not in sys.path:
        #sys.path.insert(0,   cmd_folder)
         print cmd_folder
         print "\n".split(sys.path)
         print 
         
    print cmd_folder
    #print "\n".split(sys.path)