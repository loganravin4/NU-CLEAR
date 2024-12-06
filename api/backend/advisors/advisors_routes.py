from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
advisor = Blueprint('advisor', __name__)

#------------------------------------------------------------
# View all students
@advisor.route('/student_dashboard/<user_id>', methods=['GET'])
def get_students(user_id):

    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT userId, firstName, lastName, major, coopLevel, year
                       FROM Student
                       WHERE advisor = {user_id}
    ''')
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get a list of favorited/recommended coops for a specific student
@advisor.route('/student_dashboard/<user_id>/favorites', methods=['GET'])
def get_favorites_for_student(studentId):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT s.firstName, s.lastName, f.coopId, c.title, cmp.companyName
                       FROM Favorite f
                       JOIN Coop c ON f.coopId = c.coopId
                       JOIN Company cp ON c.company = cp.companyId
                       JOIN Student s ON f.studentId = s.userId
                       WHERE Favorite.studentId = {the_data['studentId']}
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Insert a favorited/recommended coop for a specific student
@advisor.route('/student_dashboard/<user_id>/favorites', methods=['POST'])
def add_favorite_for_student(user_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''INSERT INTO Favorite (userId, coopId)
                        VALUES ({user_id}, {the_data["coopId"]})
    ''')
    
    db.get_db().commit()
    
    the_response = make_response("Advisor added co-op to favorites successfully")
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# View all announcements sent by advisors
@advisor.route('/announcements', methods=['GET'])
def get_announcements():

    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT an.announcementText, ad.firstName, ad.lastName
                        FROM Announcement an
                        JOIN Advisor ad ON ad.userId = an.createdBy
    ''')
    theData = cursor.fetchall()
    
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Send out a new announcement
@advisor.route('/announcements', methods=['POST'])
def post_announcement():
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        INSERT INTO Announcement (createdBy, announcementText)
        VALUES ({the_data["userId"]}, '{the_data["announcement"]}')
    ''')
    db.get_db().commit()

    response = make_response("Announcement posted successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update an announcement
@advisor.route('/announcements', methods=['PUT'])
def put_announcement():
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        UPDATE Announcement
        SET announcementText = '{the_data["announcementText"]}'
        WHERE announcementId = {the_data["announcementId"]}
    ''')
    db.get_db().commit()

    response = make_response("Announcement updated successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Delete an announcement from board
@advisor.route('/announcements', methods=['DELETE'])
def delete_announcement():
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        DELETE FROM Announcement 
        WHERE Announcement.announcementId = {the_data['announcementId']}
    ''')
    db.get_db().commit()
 
    response = make_response("Announcement deleted successfully")
    response.status_code = 200
    return response 