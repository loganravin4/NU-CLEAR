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
@role.route('/<company_id>/<role_id>', methods=['GET'])
def get_role(company_id, role_id):
    query = '''
        SELECT * 
        FROM Review  
        
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
# Return a list of favorited/saved jobs
@role.route('/favorites/<user_id>', methods=['GET'])
def get_favorites(user_id):
    query = f'''
        SELECT 
            c.jobId, 
            c.title, 
            cmp.companyName AS companyName, 
            c.locationCity, 
            c.locationState, 
            c.locationCountry, 
            c.description
        FROM Favorite f
        JOIN Coop c ON f.jobId = c.jobId
        JOIN Company cmp ON c.company = cmp.companyId
        WHERE f.userId = '{user_id}'
        ORDER BY c.title ASC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Add a job to the favorites list
@role.route('/favorites/<user_id>', methods=['POST'])
def add_favorite(user_id):
    the_data = request.json
    query = f'''
        INSERT INTO Favorite (userId, jobId)
        VALUES ('{user_id}', '{the_data["jobId"]}')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Job added to favorites")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Remove a job from the favorites list
@role.route('/favorites/<user_id>', methods=['DELETE'])
def delete_favorite(user_id):
    the_data = request.json
    query = f'''
        DELETE FROM Favorite
        WHERE userId = '{user_id}' AND jobId = '{the_data["jobId"]}'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Job removed from favorites")
    response.status_code = 200
    return response