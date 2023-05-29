import os
import grpc
import json
from flask import Flask, request
from flask_cors import CORS
import bookdetails_pb2
import bookdetails_pb2_grpc

app = Flask(__name__)
CORS(app)

def setupGrpcStub():
    bookclient_host = os.getenv("CLIENT_PLACEHOLDER_HOST", "localhost")
    bookclient_channel = grpc.insecure_channel(f"{bookclient_host}:50051")
    bookclient_stub = bookdetails_pb2_grpc.BookDetailsStub(bookclient_channel)

    return bookclient_stub

@app.route("/topBookQuotes")
def renderJsonBookDetailsResponse():
    author_name = request.args.get('author')
    if not author_name:
        return json.dumps([])

    response = setupGrpcStub().GetBookDetails(bookdetails_pb2.BookDetailsRequest(author=author_name.strip()))
    pretty_booklist = []
    for rbd in response.bookDetails:
        pretty_booklist.append([rbd.author, rbd.title, rbd.quotes])

    return json.dumps(pretty_booklist)

@app.route("/authors")
def renderJsonAuthorsListResponse():
    response = setupGrpcStub().GetAuthorsList(bookdetails_pb2.AuthorsListRequest())
    pretty_authorlist = []
    for ral in response.authorsList:
        pretty_authorlist.append(ral.author)

    return json.dumps(pretty_authorlist)

@app.route("/")
def renderHomepage():
    return "<h2>Hello, there's nothing here; <br />if you're looking for the relevant URLs, they're located at <i><a/>http://127.0.0.1:5000/topBookQuotes/?author=author-name</a></i> or <i><a>http://127.0.0.1:5000/authors</a></i></h2>"
