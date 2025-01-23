from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

class QAChain:
    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.llm = Ollama(base_url="http://localhost:11434", model="llama2")

        # Enhanced prompt template for more precise answers
        self.prompt_template = PromptTemplate(
            template="""You are a precise and concise AI assistant. Answer the question based only on the provided context.
            If the information is not in the context, say "I don't have enough information to answer this question."
            
            Context: {context}
            Question: {question}
            
            Provide a clear and concise answer in 1-2 sentences:""",
            input_variables=["context", "question"]
        )

    def get_answer(self, question):
        try:
            # Create the QA chain
            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store.as_retriever(),
                return_source_documents=False,
                chain_type_kwargs={
                    "prompt": self.prompt_template,
                    "verbose": False
                }
            )
            
            # Get the answer
            answer = qa_chain.run(question)
            print(f"[QAChain] Generated answer: {answer}")
            
            
            return answer.strip() 
            
        except Exception as e:
            print(f"Error in getting answer: {str(e)}")
            return "Sorry, there was an error processing your question. Please try again."