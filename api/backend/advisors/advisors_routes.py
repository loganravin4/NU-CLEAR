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
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
advisor = Blueprint('advisor', __name__)


#------------------------------------------------------------
# View all announcements sent by advisors
@advisor.route('/announcements', methods=['GET'])
def get_messages(student_id):

    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT DISTINCT createdBy, announcementText
                        FROM Announcement
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Send out a new announcement
@advisor.route('/announcements', methods=['POST'])
def send_messages(student_id):

    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        INSERT INTO Announcement (announcementId, createdBy, announcementText)
        VALUES ('{the_data["announcementId"]}', '{the_data["createdBy"]}', '{the_data["announcementText"]}')
    ''')
    
    theData = cursor.fetchall()

    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Delete an announcement from board
@advisor.route('/announcements', methods=['DELETE'])
def delete_messages(student_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        DELETE FROM Announcement 
        WHERE Announcement.announcementId = {the_data['announcementId']})
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Get a list of favorited/recommended jobs  
@advisor.route('/recommendations/<student_id>', methods=['GET'])
def get_recommendations(student_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''SELECT {the_data['jobId']}
                        FROM Favorite 
                        WHERE Favorite.studentId = {the_data['studentId']}
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

#------------------------------------------------------------
# Inserts list of recomended jobs into the students favorite 
@advisor.route('/recommendations/<student_id>', methods=['POST'])
def create_recommendations(student_id):
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
# Delete recomendations for the student 
@advisor.route('/recommendations/<student_id>', methods=['DELETE'])
def delete_recommendations(student_id):
    the_data = request.json

    cursor = db.get_db().cursor()
    cursor.execute(f'''
        DELETE FROM  Favorite 
        WHERE Favorite.studentId = {the_data['studentId']} AND Favorite.jobId = '{the_data["jobId"]}')
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response