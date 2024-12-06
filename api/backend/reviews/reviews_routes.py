from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
review = Blueprint('review', __name__)

# ------------------------------------------------------------
# Return all reviews written based on desired filters
@review.route('/reviews', methods = ['GET'])
def get_reviews():
    query = '''
        SELECT r.reviewId, r.createdAt, r.role, r.salary, r.rating, 
               r.summary, r.bestPart, r.worstPart, r.wouldRecommend, 
               s.major, s.coopLevel, s.year
        FROM Review r 
        JOIN Student s on r.createdBy = s.userId 
    '''
 
    filters = []
    if request.args.get('createdBy'):
        filters.append(f"r.createdBy = {request.args.get('createdBy')}")
    if request.args.get('role'):
        filters.append(f"r.role = {request.args.get('role')}")
    if request.args.get('rating'):
        filters.append(f"r.rating >= {request.args.get('rating')}")
    if request.args.get('wouldRecommend'):
        filters.append(f"r.wouldRecommend = {request.args.get('wouldRecommend').lower() == 'true'}")
    if request.args.get('salary'):
        filters.append(f"r.salary >= {request.args.get('salary')}")
    if request.args.get('coopLevel'):
        filters.append(f"s.coopLevel = {request.args.get('coopLevel')}")
    if request.args.get('major'):
        filters.append(f"s.major = '{request.args.get('major')}'")
    if request.args.get('year'):
        filters.append(f"s.year = {request.args.get('year')}")  


    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY createdAt DESC"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response  

# ------------------------------------------------------------
# Return all reviews submitted and the student information
@review.route('/reviews/<user_id>', methods = ['GET'])
def get_user_reviews(user_id):
    query = f'''
        SELECT r.reviewId, r.role,r.salary, r.rating, 
               r.summary, s.firstName, s.lastName, 
               s.major, s.coopLevel, s.year
        FROM Review r
        JOIN Student s ON r.createdBy = s.userId
        WHERE r.createdBy = {user_id}
    '''     

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response
 
# ------------------------------------------------------------
# Add an anonymous review
@review.route('/reviews/<user_id>', methods = ['POST'])
def add_user_reviews(user_id):
    the_data = request.json
    query = f'''
        INSERT INTO Review (createdAt, createdBy, role, salary, rating, 
                            summary, bestPart, worstPart)
        VALUES (now(), {user_id}, '{the_data["role"]}', {the_data["salary"]}, {the_data["rating"]}, 
                '{the_data["summary"]}', '{the_data["bestPart"]}', '{the_data["worstPart"]}')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review added successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Update a review
@review.route('/reviews/<user_id>/<review_id>', methods = ['PUT'])
def update_user_reviews(user_id, review_id):
    the_data = request.json
    query = f'''
        UPDATE Review
        SET summary = '{the_data["summary"]}', bestPart = '{the_data["bestPart"]}', 
            worstPart = '{the_data["worstPart"]}', rating = {the_data["rating"]}
        WHERE reviewId = {review_id} AND createdBy = {user_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review updated successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Delete a specific review previously written by a student
@review.route('/reviews/<user_id>/<review_id>', methods=['DELETE'])
def delete_user_reviews(user_id, review_id):
    query = f'''
        DELETE FROM Review
        WHERE reviewId = {review_id} AND createdBy = {user_id}
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Review deleted successfully")
    response.status_code = 200
    return response

# ------------------------------------------------------------
# Return reviews for a specific company
@review.route('/reviews/<companyName>/<company_id>', methods = ['GET'])
def get_company_reviews(companyName, company_id):
    query = f'''
        SELECT r.reviewId, r.createdAt, cp.companyName, r.rating, 
               r.summary, r.bestPart, r.worstPart
        FROM Review r
        JOIN Coop c ON r.role = c.coopId
        JOIN Company cp ON c.company = cp.companyId
        WHERE cp.companyId = {company_id} AND cp.companyName = '{companyName}'
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
@review.route('/reviews/coops/<company_id>/<coop_id>', methods = ['GET'])
def get_role_reviews(company_id, coop_id):
    query = f'''
        SELECT r.reviewId, c.title, r.createdAt, r.salary, r.rating, r.summary, 
               r.bestPart, r.worstPart
        FROM Review r
        JOIN Coop c ON r.role = c.coopId
        WHERE r.role = {coop_id} AND c.company = {company_id}
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
@review.route('/reviews/compare/<company_id>', methods = ['GET'])
def get_company_comparisons(company_id):
    role = request.args.get('role', None)
    query = f'''
       SELECT c.company, r.reviewId, r.createdAt, r.role, r.salary, r.rating, 
               r.summary, r.bestPart, r.worstPart
        FROM Review r
        JOIN Coop c ON r.role = c.coopId
        WHERE c.company != {company_id}
    '''
    if role:
        query += f" AND r.role = {role}"

    query += " ORDER BY r.createdAt DESC"

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



# ------------------------------------------------------------
# Returns summary report of a specific company and total number of good/bad reviews
@review.route('/analysis/summary_report/<company_id>', methods = ['GET'])

def get_analysis_report_and_reviews(company_id):
    query = f'''
    SELECT  
        SUM(r.rating < 3) AS bad_reviews_count,
        SUM(r.rating >= 3) AS good_reviews_count,
        sr.company, 
        sr.generatedSummary
    FROM Review r
    JOIN Coop c ON r.role = c.coopId
    JOIN Company co ON c.company = co.companyId
    JOIN SummaryReport sr ON co.companyId = sr.company
    WHERE co.companyId = {company_id}
    GROUP BY sr.company, sr.generatedSummary
    '''  

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# ------------------------------------------------------------
#  Add a summary report for a specific company
@review.route('/analysis/summary_report/<company_id>', methods = ['POST'])

def make_summary_report(company_id):

    the_data = request.json
    query = f'''  
        INSERT INTO SummaryReport (averageRating, generatedSummary, company, generatedBy) 
        VALUES ({the_data["averageRating"]}, '{the_data["generatedSummary"]}', {company_id}, {the_data["generatedBy"]})
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Summary Report Created")
    response.status_code = 200
    return response
 

# ------------------------------------------------------------
#  Add a visualization report for a specific company
@review.route('analysis/visualization/<company_id>', methods = ['POST'])

def add_visualization(company_id):

    the_data = request.json
    query = f'''  
        INSERT INTO Visualization(vizType, filters, company, createdBy) 
        VALUES ('{the_data["vizType"]}', '{the_data["filters"]}', {company_id}, {the_data["createdBy"]})
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Visualization Created")
    response.status_code = 200
    return response

