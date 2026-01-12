#we must name the file conftest otherwise, if we name this file other than conftest where we add the dir to system path , we must import this file everywhere where we need the dir added to system path
import os
import sys
projectroot=os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(projectroot)
sys.path.insert(0,projectroot)   #here we are appending the current file dir into a PYTHONPATH