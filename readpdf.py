import os
from langchain.document_loaders import PyPDFLoader 
from langchain.embeddings import OpenAIEmbeddings 
from langchain.vectorstores import Chroma 
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.memory import ConversationSummaryMemory

class joelchat:
    def on_chain():
        load_dotenv()
        api_key = os.environ.get('OPENAI_API_KEY')

        ordtih_file_path = os.getcwd()

        pdf_file_name = "constitucionparte1993-12-09-2017.pdf"
        pdf_path = f"{ordtih_file_path}\{pdf_file_name}"
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        embeddings = OpenAIEmbeddings(openai_api_key=api_key)

        pdfsearch = Chroma.from_documents(documents, embeddings)
        memory = ConversationSummaryMemory(
            llm = ChatOpenAI(model_name='gpt-3.5-turbo'),
            memory_key='chat_history',
            return_messages=True,
            output_key='answer')
        #memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

        global chain
        chain = ConversationalRetrievalChain.from_llm(
                    ChatOpenAI(temperature=0.3,model="gpt-3.5-turbo",
                            openai_api_key=api_key), 
                    retriever=pdfsearch.as_retriever(),
                    memory=memory
                )
        
        return chain
    
    def on_submit(query,chain):
        
        if query.lower() == 'exit':
            print("Thank you for using the State of the Union chatbot!")
            return

        result = chain({"question": query})
        return result
        


