""" 
    My flask Application 
"""

from flask import Flask, request

database = { 'maruf': '1000'}

app = Flask(__name__)

""" 
    Routes are define here 
 """
#  Home Route 
@app.route('/', methods=['GET'])
def home():
    return "Welcome to my Home Page"

# About Route
@app.route('/about', methods=['GET'])
def about():
    return "my name is maruf"

# Read all data from Database 
@app.route('/getdata/', methods=['GET'])
def get_data():
    return database

# Create a data and set from database 
# api/adddata?name=id
@app.route('/adddata', methods=['GET', 'PUT'])
def add_data( ):
    key, value = list(request.args.items())[0]
    database[key] = value
    return f"{key} added Successfully"

# Delete Data 
# api/deletedata?user=name
@app.route('/deletedata/', methods=['GET','DELETE'])
def delete_data():
    _,value = list(request.args.items())[0]
    database.pop(value)

    return f"{value} Deleted Successfullys"

""" 
    Main Function all Called here
"""
if __name__ == '__main__':
    app.run()
