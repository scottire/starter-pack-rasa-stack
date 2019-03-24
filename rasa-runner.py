from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

core_endpoint_config = EndpointConfig(url='http://localhost:5055/webhook')

interpreter = RasaNLUInterpreter('models/current/nlu')
agent = Agent.load('models/current/dialogue', interpreter=interpreter,
                                    action_endpoint = core_endpoint_config)

messages = []
while True:
    a = input("Eu: ")
    messages.append(a)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for r in responses:
        answer = r.get("text")
        messages.append(answer)
        print("Bot: " + answer)