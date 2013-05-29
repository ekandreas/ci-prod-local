__author__ = 'Andreas Ek, Flowcom AB'

# import the fabric lib into this script
from fabric.api import *
import os

# connect to sql, make a dump and get it
def printall():
	print os.environ["ANOTHERPARAMETER"]