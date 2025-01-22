from langchain.chains import RetrievalQA
from langchain.llms import Ollama

class QAChain:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = Ollama(base_url="http://localhost:11434", model="llama2")

    def get_answer(self, question):
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever()
        )
        return qa_chain.run(question)