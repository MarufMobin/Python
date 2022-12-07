# Flask CRUD Operation using JSON file

from flask import Flask, jsonify, request 
# Set Flask Name
app = Flask( __name__ )

# Database Create 
students = [{"id" : 1, "name" : "maruf"},{"id" : 2, "name" : "mobin"}]

# Read 
@app.route('/', methods=['GET'])
def home():
    return jsonify( students )

# add new student 
@app.route('/add', methods=['POST'])
def add():
    students.append( request.get_json() )
    print( request.get_json())
    return "Student Aded successfully." , 200

# Update Student are here
@app.route('/update', methods=['PUT'])
def update():
    for student in students:
        if student.get('id') == request.get_json().get('id') :
            student.update( request.get_json() )
    print('Student Updated successfully', request.get_json())
    return "Student Updated Successfully."

@app.route('/delete', methods=['DELETE'])
def delete():
    for i in range( len(students) ):
        if  students[i].get('id') == request.get_json().get('id'):
            del students[i]
    print('Student Deleted Successfully', request.get_json())
    return "Student Delete Successfully"

app.run( debug=True )