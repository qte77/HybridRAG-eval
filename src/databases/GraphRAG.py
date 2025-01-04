from .KnowledgeGraph import KnowledgeGraph
from llm_api import LLM

class GraphRAG:
    def __init__(self):
        self.graph_db = KnowledgeGraph()
        self.llm = LLM()

    def query(self, question):
        context = self.graph_db.retrieve(question)
        answer = self.llm.generate(question, context)
        return answer, 0.0  # Placeholder for runtime
