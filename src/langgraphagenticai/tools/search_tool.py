from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns a list of tools for the agent.
    Currently, it includes a web search tool using Tavily.
    """
    tools = [TavilySearchResults(max_results=2)]

    return tools

def create_tool_node(tools):
    """
    Creates a ToolNode with the provided tools.
    
    Args:
        tools (list): A list of tools to be included in the ToolNode.
    
    Returns:
        ToolNode: An instance of ToolNode containing the specified tools.
    """
    return ToolNode(tools=tools)