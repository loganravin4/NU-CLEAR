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
# ROUTE DESCRIPTION
@admin.route('/modules', methods=['POST'])
def post_modules():
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
# ROUTE DESCRIPTION
@admin.route('/user_permissions', methods=['GET'])
def get_user_perms ():

    query = f'''SELECT id, 
                       product_name, 
                       description, 
                       list_price, 
                       category 
                FROM products 
                WHERE id = {str(id)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# ROUTE DESCRIPTION
@admin.route('/user_permissions', methods=['POST'])
def add_user_perms ():

    query = f'''SELECT id, 
                       product_name, 
                       description, 
                       list_price, 
                       category 
                FROM products 
                WHERE id = {str(id)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# ROUTE DESCRIPTION
@admin.route('/user_permissions', methods=['PUT'])
def update_user_perms ():

    query = f'''SELECT id, 
                       product_name, 
                       description, 
                       list_price, 
                       category 
                FROM products 
                WHERE id = {str(id)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# ROUTE DESCRIPTION
@admin.route('/user_permissions', methods=['DELETE'])
def delete_user_perms ():

    query = f'''SELECT id, 
                       product_name, 
                       description, 
                       list_price, 
                       category 
                FROM products 
                WHERE id = {str(id)}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response