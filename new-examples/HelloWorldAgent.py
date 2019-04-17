# Needed imports
from pade.behaviours.types import OneShotBehaviour
from pade.core.agent import Agent
from pade.misc.utility import display_message, start_loop

# Defining the HelloWorldAgent class
class HelloWorldAgent(Agent):

	# This method will execute on agent initiation
	def setup(self):
		# It adds a behaviour in the agent
		self.add_behaviour(SayHello(self))


# Defining the SayHello behaviour
class SayHello(OneShotBehaviour):

	# This method executes the main action of this behaviour
	def action(self):
		# It shows a message, with date information, in console
		display_message(self.agent, 'Hello world!')


# It starts the agent HelloWorldAgent with PADE
if __name__ == '__main__':
	# Defining a HelloWorldAgent object
	helloagent = HelloWorldAgent('hello')
	# Create a list with agents that will be executed
	agents_list = [helloagent]
	# Passing the agent list to main loop of PADE
	start_loop(agents_list)