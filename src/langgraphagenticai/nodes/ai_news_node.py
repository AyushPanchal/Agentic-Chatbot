from tavily import TavilyClient

from langchain_core.prompts import ChatPromptTemplate


class AINewsNode:
    def __init__(self, llm):
        self.tavily = TavilyClient()
        self.llm = llm

        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        frequency = state["message"][0].content_lower()
        self.state["frequency"] = frequency
        time_range_map = {
            "daily": "d",
            "weekly": "w",
            "monthly": "m",
            "year": "y"
        }

        days_map = {
            "daily": 1,
            "weekly": 7,
            "monthly": 30,
            "year": 366
        }

        response = self.tavily.search(query="Top Artificial Intelligence (AI) technology news india and globally",
                                      topic="news",
                                      time_range=time_range_map[frequency],
                                      include_answer="advanced",
                                      max_results=20,
                                      days=days_map[frequency],
                                      )
        state["news_data"] = response.get("results", [])
        self.state["news_data"] = state["news_data"]

        return state
