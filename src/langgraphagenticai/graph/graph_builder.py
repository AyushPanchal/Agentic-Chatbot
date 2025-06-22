from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools, create_tool_node


class GraphBuilder:
    def __init__(self, model):
        self.basic_chatbot_node = None
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using langgraph.
        This method initializes a chatbot node using the "BasicChatBotNode" class
        and integrates it into the graph. The chatbot node is set as both the entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def chatbot_with_tools_build_graph(self):
        """
        Builds a chatbot graph with tools using langgraph.
        This method initializes a chatbot node with tools and integrates it into the graph.
        The chatbot node is set as both the entry and exit point of the graph.
        """
        # Tool definition
        tools = get_tools()
        tool_node = create_tool_node(tools)

        llm = self.llm

        obj_chatbot_with_node = ChatbotWithToolNode(llm)

        chatbot_node = obj_chatbot_with_node.create_chatbot(tools)

        # add the nodes
        self.graph_builder.add_node("chatbot", chatbot_node)
        self.graph_builder.add_node("tools", tool_node)

        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot", tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def ai_news_build_graph(self):
        # Added the nodes
        self.graph_builder.add_node("fetch_news","")
        self.graph_builder.add_node("summarize_news","")
        self.graph_builder.add_node("save_results","")

        # Added the edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news", "summarize_news")
        self.graph_builder.add_edge("summarize_news", "save_results")
        self.graph_builder.add_edge("save_results", END)






    def setup_graph(self, usecase: str):
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()

        if usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()

        return self.graph_builder.compile()
