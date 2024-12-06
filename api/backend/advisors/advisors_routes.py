########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
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
@advisor.route('/student_dashboard', methods=['GET'])
def get_announcements(advisor_id):

    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT userId, firstName, lastName, major, coopLevel, year
                       FROM Student
                       WHERE advisor = {advisor_id}
    ''')
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Get a list of favorited/recommended jobs for a specific student
@advisor.route('/student_dashboard/<user_id>/favorites', methods=['GET'])
def get_students(studentId):
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
# Inserts list of recomended jobs into the students favorite 
@advisor.route('/recommendations/<student_id>', methods=['POST'])
def add_favorite(student_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        INSERT INTO Favorite (studentId, jobId)
        VALUES ('{the_data["studentId"]}', '{the_data["jobId"]}')
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response('Advisor recommended a job to a student' )
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# View all announcements sent by advisors
@advisor.route('/announcements', methods=['GET'])
def get_announcements():

    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT createdBy, announcementText
                        FROM Announcement
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


#------------------------------------------------------------
# Send out a new announcement
@advisor.route('/announcements', methods=['POST'])
def post_announcement(userId):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        INSERT INTO Announcement (createdBy, announcementText)
        VALUES ({userId}, '{the_data["announcementText"]}')
    ''')
    db.get_db().commit()

    response = make_response("Coop added to favorites successfully")
    response.status_code = 200
    return response


#------------------------------------------------------------
# Delete an announcement from board
@advisor.route('/announcements', methods=['DELETE'])
def delete_announcement(announcement_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        DELETE FROM Announcement 
        WHERE Announcement.announcementId = {the_data['announcementId']})
    ''')
    db.get_db().commit()

    response = make_response("Coop added to favorites successfully")
    response.status_code = 200
    return response
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response