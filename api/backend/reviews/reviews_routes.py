from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
reviews = Blueprint('reviews', __name__)

# ------------------------------------------------------------
# Return all reviews written based on desired filters
@reviews.route('/reviews', methods = ['GET'])
def get_reviews():
    query = '''
        SELECT reviewId, createdAt, createdBy, role, salary, rating, 
               summary, bestPart, worstPart, isAnonymous, wouldRecommend
        FROM Review
    '''

    # Dynamically build WHERE conditions
    filters = []
    if request.args.get('createdBy'):
        filters.append(f"createdBy = {request.args.get('createdBy')}")
    if request.args.get('role'):
        filters.append(f"role = {request.args.get('role')}")
    if request.args.get('rating'):
        filters.append(f"rating >= {request.args.get('rating')}")
    if request.args.get('isAnonymous'):
        filters.append(f"isAnonymous = {request.args.get('isAnonymous').lower() == 'true'}")
    if request.args.get('wouldRecommend'):
        filters.append(f"wouldRecommend = {request.args.get('wouldRecommend').lower() == 'true'}")
    if request.args.get('salary'):
        filters.append(f"salary >= {request.args.get('salary')}")
    if request.args.get('dateFrom') and request.args.get('dateTo'):
        filters.append(f"createdAt BETWEEN '{request.args.get('dateFrom')}' AND '{request.args.get('dateTo')}'")
    elif request.args.get('dateFrom'):
        filters.append(f"createdAt >= '{request.args.get('dateFrom')}'")
    elif request.args.get('dateTo'):
        filters.append(f"createdAt <= '{request.args.get('dateTo')}'")

    # Add filters to the query
    if filters:
        query += " WHERE " + " AND ".join(filters)

    # Add sorting
    query += " ORDER BY createdAt DESC"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Return all reviews submitted by a specific user
@reviews.route('/reviews/<user_id>', methods = ['GET'])
def get_user_reviews(user_id):
    query = f'''
        SELECT reviewId, createdAt, role, salary, rating, 
               summary, bestPart, worstPart, isAnonymous
        FROM Review
        WHERE createdBy = '{user_id}'
        ORDER BY createdAt DESC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Add an anonymous review to the database
@reviews.route('/reviews/<user_id>', methods = ['POST'])
def add_user_reviews(user_id):
    the_data = request.json
    query = f'''
        INSERT INTO Review (createdAt, createdBy, role, salary, rating, 
                            summary, bestPart, worstPart, isAnonymous)
        VALUES (now(), '{user_id}', '{the_data["role"]}', {the_data["salary"]}, {the_data["rating"]}, 
                '{the_data["summary"]}', '{the_data["bestPart"]}', '{the_data["worstPart"]}', TRUE)
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
 
    response = make_response("Review added successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Update a review previously written by a student
@reviews.route('/reviews/<user_id>/<review_id>', methods = ['PUT'])
def update_user_reviews(user_id, review_id):
    the_data = request.json
    query = f'''
        UPDATE Review
        SET summary = '{the_data["summary"]}', bestPart = '{the_data["bestPart"]}', 
            worstPart = '{the_data["worstPart"]}', rating = {the_data["rating"]}
        WHERE reviewId = '{review_id}' AND createdBy = '{user_id}'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review updated successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Delete a specific review previously written by a student
@reviews.route('/reviews/<user_id>/<review_id>', methods=['DELETE'])
def delete_user_reviews(user_id, review_id):
    query = f'''
        DELETE FROM Review
        WHERE reviewId = {review_id} AND createdBy = '{user_id}'
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review deleted successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Return reviews for a specific company
@reviews.route('/reviews/<company_id>', methods = ['GET'])
def get_company_reviews(company_id):
    query = f'''
        SELECT r.reviewId, r.createdAt, r.role, r.salary, r.rating, 
               r.summary, r.bestPart, r.worstPart, r.isAnonymous
        FROM Review r
        JOIN Coop c ON r.role = c.jobId
        WHERE c.companyId = '{company_id}'
        ORDER BY r.createdAt DESC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Return reviews for a specific role
@reviews.route('/reviews/<company_id>/<role_id>', methods = ['GET'])
def get_role_reviews(company_id, role_id):
    query = f'''
        SELECT reviewId, createdAt, salary, rating, summary, 
               bestPart, worstPart, isAnonymous
        FROM Review
        WHERE role = '{role_id}' AND companyId = '{company_id}'
        ORDER BY createdAt DESC
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

 
# ------------------------------------------------------------
# Returns reviews for other companies to compare it to my company
@reviews.route('/reviews/compare/<company_id>', methods = ['GET'])
def get_company_comparisons(company_id):
    query = '''
        
    ''' 

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response