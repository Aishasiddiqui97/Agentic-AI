from agents import Agent, Runner, function_tool
from main import config

@ function_tool
def weather_update(query:str) -> str:
  return  'Today weather in Karachi is sunny '

agent=Agent( 
    name='gabbar',
    instructions="you are a helpful assistant, Your task is to help the user with their queries. use tool if needed to answer weather questions.",
    tools=[weather_update],

)
result = Runner.run_sync(agent,       
  'what is weather in karachi?',
   run_config=config)
print(result.final_output)

#############################################################################################################

from agents import Agent, Runner, function_tool
from main import config

@function_tool
def weather_update (city:str):
    return f"the weather in {city} is sunny"




agent=Agent( 
    name='General Agent',
    instructions="you are a helpful assistant,use tool if needed to answer weather questions.",
    tools=[weather_update],

)
result = Runner.run_sync(agent,       
 'what is weather in Naran Kagan?',
  run_config=config)
print(result.final_output)

#############################################################################################################

