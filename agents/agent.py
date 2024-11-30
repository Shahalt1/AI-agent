from termcolor import colored
from prompts.prompt import agent_system_prompt_template
from models.ollama_models import OllamaModel
from toolbox.toolbox import ToolBox

class Agent:
    def __init__(self, tools, model_service, model_name, stop=None):
        self.tools = tools
        self.model_service = model_service
        self.model_name = model_name
        self.stop = stop

    def prepare_tools(self):
        toolbox = ToolBox()
        toolbox.store(self.tools)
        tool_description = toolbox.tools()

    def think(self, user_input):
        tool_description = self.prepare_tools()
        agent_system_prompt = agent_system_prompt_template.format(tool_descriptions=tool_description)

        if self.model_service == "OllamaModel":
            model_instance = self.model_service(
                model = self.model_name,
                system_prompt = agent_system_prompt,
                stop = self.stop, 
                temperature = 0
            )
        else:
            model_instance = self.model_service(
                model = self.model_name,
                system_prompt = agent_system_prompt,
                stop = self.stop, 
                temperature = 0
            )

        response = model_instance.generate_response(user_input)
        return response

    def work(self, user_input):
        agent_response = self.think(user_input)
        tool_choice = agent_response.get("tool_choice")
        tool_input = agent_response.get("tool_input")

        for tool in self.tools:
            if tool.__name__ == tool_choice:
                response = tool(tool_input)
                print(colored(response, 'cyan'))
                return
        print(colored(tool_input, 'cyan'))
        return
        
        
