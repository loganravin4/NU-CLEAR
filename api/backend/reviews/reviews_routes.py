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
@reviews.route('/', methods = ['GET'])
def get_reviews():
    query = '''
        SELECT reviewId, createdAt, createdBy, role, salary, rating, 
               summary, bestPart, worstPart, isAnonymous, wouldRecommend
        FROM Review
    '''

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
# Add an anonymous review
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
# Update a review
@reviews.route('/reviews/<user_id>/,<review_id>', methods = ['PUT'])
def update_user_reviews(user_id):
    the_data = request.json
    query = f'''
        UPDATE Review
        SET summary = '{the_data["summary"]}', bestPart = '{the_data["bestPart"]}', 
            worstPart = '{the_data["worstPart"]}', rating = {the_data["rating"]}
        WHERE reviewId = {the_data["reviewId"]} AND createdBy = '{user_id}'
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
@reviews.route('/reviews/<company_id>/<job_id>', methods = ['GET'])
def get_role_reviews(company_id, job_id):
    query = f'''
        SELECT reviewId, createdAt, salary, rating, summary, 
               bestPart, worstPart, isAnonymous
        FROM Review
        WHERE role = '{job_id}' AND companyId = '{company_id}'
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



# ------------------------------------------------------------
# Returns summary report of a specific company and total number of good/bad reviews
@reviews.route('/analysis/summary_report/{company_id}', methods = ['GET'])

def get_analysis_report_and_reviews(company_id):
    query = '''
    SELECT  
        SUM(r.rating < 3) AS bad_reviews_count,
        SUM(r.rating >= 3) AS good_reviews_count,
        sr.company, 
        sr.generatedSummary
    FROM Review r
    JOIN Coop c ON r.role = c.jobId
    JOIN Company co ON c.company = co.companyId
    JOIN SummaryReport sr ON co.companyId = sr.company
    WHERE co.companyId = {company_id}
    GROUP BY sr.company, sr.generatedSummary;

    '''  

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#  Add a summary report for a specific company
@reviews.route('/analysis/summary_report/{company_id}', methods = ['POST'])

def make_summary_report(company_id):

    the_data = request.json
    query = f'''  
        INSERT INTO SummaryReport (averageRating, generatedSummary, company, generatedBy, updatedBy, summaryReportId) 
        VALUES ('{the_data["averageRating"]}', '{the_data["generatedSummary"]}', '{company_id}' , '{the_data["generatedBy"]}',
                '{the_data["updatedBy"]}', '{the_data["summaryReportId"]}')
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Job added to favorites")
    response.status_code = 200
    return response
