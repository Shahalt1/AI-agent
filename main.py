from agents.agent import Agent
from models.gemini_models import GeminiModel
from models.ollama_models import OllamaModel
from tools.basic_calculator import calculator
from tools.reverser import reverse_string

if __name__ == "__main__":

    tools = [calculator, reverse_string]


    # Uncoment below to run with OpenAI
    # model_service = OpenAIModel
    # model_name = 'gpt-3.5-turbo'
    # stop = None

    # Uncomment below to run with Ollama
    model_service = OllamaModel
    model_name = 'llama3.2-vision'
    stop = "<|eot_id|>"

    agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

    while True:
        prompt = input("Ask me anything: ")
        if prompt.lower() == "exit":
            break
    
        agent.work(prompt)