from objc_util import *

APP = UIApplication.sharedApplication()

def set(text):
	APP.setApplicationBadgeString_(text)
