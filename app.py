from flask import Flask, render_template, request
from src.helper import load_pdf, split_text
from store_index import create_vector_db
from retrieval_chain import form_retrieval_chain
from config import GeneralParams

app = Flask(__name__)

docs = load_pdf(path=GeneralParams.DATA_PATH)
chunks = split_text(documents=docs)

retriever = create_vector_db(documents=chunks)

retrieval_chain = form_retrieval_chain(retriever=retriever)


@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("Query: ", msg)
    result=retrieval_chain.invoke({"input": msg})
    print("Response : ", result["answer"])
    return str(result["answer"])

if __name__ == '__main__':
    app.run(debug=True)
