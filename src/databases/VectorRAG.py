from vector_db import VectorDB
from llm_api import LLM

class VectorRAG:
    def __init__(self):
        self.vector_db = VectorDB()
        self.llm = LLM()

    def query(self, question):
        context = self.vector_db.retrieve(question)
        answer = self.llm.generate(question, context)
        return answer, 0.0  # Placeholder for runtime