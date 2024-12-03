from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
role = Blueprint('role', __name__)

#------------------------------------------------------------
# ROUTE DESCRIPTION
@role.route('//<company_id>/<role_id>', methods=['GET'])
def get_role(company_id, role_id):
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
@role.route('/<company_id>/<role_id>', methods=['POST'])
def add_role(company_id, role_id):
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
@role.route('/favorites', methods=['GET'])
def get_favorites():
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
@role.route('/favorites', methods=['POST'])
def add_favorite():
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
@role.route('/favorites', methods=['DELETE'])
def delete_favorite():
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