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
@role.route('/<company_id>/<job_id>', methods=['GET'])
def get_role(company_id, role_id):
    query = '''
        SELECT co.* 
        FROM Coop co 
        JOIN Company c ON co.company = c.companyID
        WHERE c.companyId = {company_id} 
        AND co.job_id = {job_id}
    ''' 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response 

#------------------------------------------------------------
# ROUTE DESCRIPTION
@role.route('/<company_id>/<job_id>', methods=['POST'])
def add_role(company_id, job_id):
    
    the_data = request.json
    query = f'''
        INSERT INTO Coop (locationCity, locationState, locationCountry, title, description, company, jobId)
        VALUES ('{the_data["locationCity"]}', '{the_data["locationState"]}','{the_data["locationCountry"]}', '{the_data["title"]}',
                '{the_data["description"]}', '{company_id}, '{job_id}') 
    ''' 
          
       
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
  
    response = make_response("Job added to favorites")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Return a list of favorited/saved jobs
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
# Add a job to the favorites list
@role.route('/favorites', methods=['POST'])
def add_favorite():
    the_data = request.json
    query = f'''
        INSERT INTO Favorite (studentId, jobId)
        VALUES ('{the_data["studentId"]}', '{the_data["jobId"]}')
    '''

    the_data = request.json
    query = f'''  
        INSERT INTO Favorite (studentId, jobId)
        VALUES ('{the_data["studentId"]}', '{the_data["jobId"]}')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Job added to favorites")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Remove a job from the favorites list
@role.route('/favorites', methods=['DELETE'])
def delete_favorite():
    the_data = request.json
    query = f'''
        DELETE FROM Favorite
        WHERE studentId = '{the_data["studentId"]}' AND jobId = '{the_data["jobId"]}'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Job removed from favorites")
    response.status_code = 200
    return response