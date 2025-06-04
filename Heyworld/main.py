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

result = Runner.run_sync(starting_agent=agent, input="Har k jeetna wala ko bazigar khta h", run_config=config)

print(result.final_output)

# # Code within the code,
# # Functions calling themselves,
# # Infinite loop's dance.
# if __name__ == "__main__":  # name guard
#    main()
