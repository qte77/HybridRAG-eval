from .KnowledgeGraph import KnowledgeGraph
from vector_db import VectorDB
from llm_api import LLM

class HybridRAG:
    def __init__(self):
        self.vector_db = VectorDB()
        self.kg = KnowledgeGraph()
        self.llm = LLM()

    def query(self, question):
        vector_context = self.vector_db.retrieve(question)
        graph_context = self.kg.retrieve(question)
        combined_context = self.combine_contexts(vector_context, graph_context)
        answer = self.llm.generate(question, combined_context)
        return answer, 0.0  # Placeholder for runtime

    def combine_contexts(self, vector_context, graph_context):
        pass
