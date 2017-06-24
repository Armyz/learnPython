class Test(object):
    def __init__(self,switch):
    	self.switch = switch

    def Cal(self,a,b):
    	try:
    	    a/b
    	except Exception as result:
    		if(self.switch):
                    print("chu li yi chang")
                    print(result)
    		else:
    		    raise

a = Test(True)
a.Cal(11,0)
