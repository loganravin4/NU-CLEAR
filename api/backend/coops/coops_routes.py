from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
coop = Blueprint('coop', __name__)

#------------------------------------------------------------
# See all roles
@coop.route('/coop', methods=['GET'])
def get_role():
    query = '''
        SELECT c.coopId, c.title, cp.companyName, c.description, c.locationState AS state, c.locationCity AS city, c.locationCountry AS country
        FROM Coop c JOIN Company cp ON c.company = cp.companyId
    ''' 

    filters = []

    if request.args.get('title'):
        filters.append(f"c.title = '{request.args.get('title')}'")
    if request.args.get('locationCity'):
        filters.append(f"c.locationCity = '{request.args.get('locationCity')}'")
    if request.args.get('locationState'):
        filters.append(f"c.locationState = '{request.args.get('locationState')}'")
    if request.args.get('locationCountry'):
        filters.append(f"c.locationCountry = '{request.args.get('locationCountry')}'")

    if filters:
        query += " WHERE " + " AND ".join(filters)

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
 

#------------------------------------------------------------
# Add a new co-op listing 
@coop.route('/coop', methods=['POST'])
def add_role():        
    
    the_data = request.json
    query = f'''
        INSERT INTO Coop (locationCity, locationState, locationCountry, title, description, company)
        VALUES ('{the_data["locationCity"]}', '{the_data["locationState"]}','{the_data["locationCountry"]}', '{the_data["title"]}',
                '{the_data["description"]}', {the_data["company"]}) 
    ''' 
                 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Coop listing created successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update a coop listing
@coop.route('/coop', methods=['PUT'])
def update_coop():        
    the_data = request.json
    query = f'''
    UPDATE Coop
    SET 
        title = '{the_data['title']}',
        description = '{the_data['description']}',
        locationCity = '{the_data['locationCity']}',
        locationState = '{the_data['locationState']}',
        locationCountry = '{the_data['locationCountry']}'
    WHERE 
        coopId = {the_data['coopId']}
    '''

    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Co-op updated successfully")
    response.status_code = 200
    return response


#------------------------------------------------------------
# Delete a coop listing
@coop.route('/coop', methods=['DELETE'])
def delete_coop():        
    the_data = request.json
    query = f'''
    DELETE FROM Coop
    WHERE coopId = {the_data['coopId']}
    '''

    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Co-op deleted successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Return a list of favorited/saved jobs
@coop.route('/favorites/<user_id>', methods=['GET'])
def get_favorites(user_id):
    query = f'''
        SELECT 
            c.coopId, 
            c.title, 
            cmp.companyName AS companyName, 
            c.locationCity, 
            c.locationState, 
            c.locationCountry, 
            c.description
        FROM Favorite f
        JOIN Coop c ON f.coopId = c.coopId
        JOIN Company cmp ON c.company = cmp.companyId
        WHERE f.userId = {user_id}
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
@coop.route('/favorites/<user_id>', methods=['POST'])
def add_favorite(user_id):
    the_data = request.json
    query = f'''
        INSERT INTO Favorite (userId, coopId)
        VALUES ({user_id}, {the_data["coopId"]})
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Coop added to favorites successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Remove a job from the favorites list
@coop.route('/favorites/<user_id>', methods=['DELETE'])
def delete_favorite(user_id):
    the_data = request.json
    query = f'''
        DELETE FROM Favorite
        WHERE userId = {user_id} AND coopId = {the_data["coopId"]}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Coop removed from favorites successfully")
    response.status_code = 200
    return response