# def main():
#     print("Hello from heyworld!")

# print("__name__>>>>",__name__)

# if __name__ == "__main__": #name guard
#    main()

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

gemini_api_key = "AIzaSyClKLOVc-o6awnksGP3S_f3VF1iu08oxtw"

#Reference: https://ai.google.dev/gemini-api/docs/openai
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True 
)

agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant")

result = Runner.run_sync(starting_agent=agent, input="Asalm o alikum myself AISHA", run_config=config)

print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.
# if __name__ == "__main__": #name guard
#   main()



# #golobal

# import asyncio
# from openai import AsyncOpenAI
# from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# gemini_api_key = "AIzaSyDhD_WyAAS7eXi44gz1dvaWmqYlL9U_ah0"

# #Reference: https://ai.google.dev/gemini-api/docs/openai
# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# set_tracing_disabled(disabled=True)

# async def main():
#     # This agent will use the custom LLM provider
#     agent = Agent(
#         name="Assistant",
#         instructions="You only respond in haikus.",
#         model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
#     )

#     result = await Runner.run_sync(
#         agent,
#         "Tell me about recursion in programming.")
#     print(result.final_output)


# if __name__ == "__main__":
#     asyncio.run(main())



