from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of routes.
admin = Blueprint('admin', __name__)

#------------------------------------------------------------
# ROUTE DESCRIPTION
@admin.route('/modules', methods=['GET'])
def get_modules():
    query = '''
        SELECT  id, 
                product_code, 
                product_name, 
                list_price, 
                category 
        FROM products
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Allow the Admin add a new module 
@admin.route('/modules', methods=['POST'])
def post_modules():
    the_data = request.json

    query = f'''
        INSERT INTO Module (moduleName, moduleStatus, createdBy)
        VALUES ({the_data['moduleName']}, {the_data['moduleStatus']}, {the_data['createdBy']}),
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get/see a list of all users and their permissions 
@admin.route('/user_permissions', methods=['GET'])
def get_user_perms ():

    query = f'''SELECT *
                FROM UserPermission 
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Add a new user and permissions 
@admin.route('/user_permissions', methods=['POST'])
def add_user_perms ():
    the_data = request.json
    query = f'''INSERT INTO UserPermission (userType, permissionId)
                VALUES ({the_data['userType']},{the_data['permissionId']})

    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update existing user permissions 
@admin.route('/user_permissions', methods=['PUT'])
def update_user_perms ():
    the_data = request.json
    query = f'''UPDATE UserPermission
                SET permissionId = {the_data['permissionId']}
                WHERE userType = {the_data['userType']}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Delete a user or permissions 
@admin.route('/user_permissions', methods=['DELETE'])
def delete_user_perms ():
    the_data = request.json
    query = f'''DELETE FROM User
                WHERE userId = {the_data['userId']}; 

    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response