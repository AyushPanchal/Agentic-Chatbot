
from src.langgraphagenticai.state.state import State


class BasicChatbotNode:

    """
    This is basic chatbot node class.
    """

    def __init__(self, model):
        self.llm = model
    
    def process(self, state:State)->dict:
        """
        Process the state and return the response from the LLM.
        
        Args:
            state (State): The current state of the chatbot.
        
        Returns:
            dict: A dictionary containing the response from the LLM.
        """
        return {"messages": self.llm.invoke(state["messages"])}
        
