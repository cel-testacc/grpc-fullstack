# grpc-fullstack
This is fullstack app that contains a grpc server, a grpc client, and a separate frontend to display API data. The goal of the app is to show how a simple grpc setup works.

### Dependencies
1. The client and server files run on Python and require installment of the following modules. You can use pip to install them.
- grpcio
- grpcio-tools=1.44.0 (*Note: The grpcio-tools version is fixed to 1.44.0 so as not to break compatibility with mysql-connector-python.*)
- mysql-connector-python
- flask
- flask-cors
2. The database folder contains a prepopulated MySQL file that contains the data used in this project. You can set it up within your own machine/virtual environment.
3. The database connections need to be set up in the server/bookdetails_server.py file. These need to be filled out with your own relevant environment variables.
```sh
config = {
    'user': os.getenv('DBUSER'),
    'password': os.getenv('DBPASS'),
    'host': os.getenv('DBHOST'),
    'database': os.getenv('DBSQLENDPOINTS'),
    'raise_on_warnings': True
}
```

### How to run the project

1. Navigate to the server directory and launch `python bookdetails_server.py` in one terminal. This opens the grpc server that holds the data and prepares it for transfer. It is written in Python.
2. In a second terminal window, navigate to the client directory and launch `FLASK_APP=bookdetails_client.py flask run`. This opens the receiving grpc client that sets up the API. The backend framework used for this is Flask.
3. In a third terminal window, navigate to the frontend directory and run `npm run dev`. This opens a simple frontend page where you can select an author's name from a drop-down list and it displays the corresponding top quotes from that author's books. The frontend framework used is Vue.js.

### Tests
There are unit tests for the grpc client and server files. To run them, make sure the files are launched and open another terminal window and run `python test_bookdetails_server.py` and `python test_bookdetails_client.py`.

### TODO
Currently, I haven't set up any component tests yet for the frontend framework to test the methods getData() and onChange() in App.vue. 
