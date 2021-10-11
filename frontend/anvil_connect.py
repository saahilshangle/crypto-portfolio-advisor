import anvil.server

def connect():
	anvil.server.connect("X3ZM4VT6464V5AMEBUOBR5ZV-A3PANHICIGTZ7P35")

	@anvil.server.callable
	def say_hello(name):
		print("Hello from the uplink, %s!" % name)
		return "Hello from the uplink"+str(name)

	anvil.server.wait_forever()

connect()
