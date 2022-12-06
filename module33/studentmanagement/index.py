# Flask CRUD Operations using Query 
from flask import Flask, jsonify, request

app = Flask( __name__ )

# Database are here
students = [{"id" : 1, "name": "rahim"}, {"id" : 2, "name": "korim"}]

# All data are showing this route 
@app.route('/')
def home():
    return jsonify( students )

# A data are added in our database 
@app.route('/add', methods=['GET', 'POST'])
def add():
    students.append( request.args )
    return "Student added Successfully"

# A User information are update here
@app.route('/update', methods=['GET', 'PUT'] )
def update():
    for student in students:
        if str(student.get('id')) == request.args.get('id'):
            student.update(request.args)
    return "Student update successfully"

# A User Delete related work are here
@app.route('/delete', methods=["GET", "DELETE"])
def delete():
    for i in range( len(students) ):
        if str(students[i].get('id')) == request.args.get('id'):
            del students[i]
            break
    return "Student deleted successfully"
    
app.run( debug=True )