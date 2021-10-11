import anvil.server

def connect():
	anvil.server.connect("AUUM3BBUZ2X663XS3YVCXBOR-A3PANHICIGTZ7P35")

	@anvil.server.callable
	def say_hello(name):
		print("Hello from the uplink, %s!" % name)
		return "Hello from the uplink, %s!"+str(name)

	anvil.server.wait_forever()

connect()
