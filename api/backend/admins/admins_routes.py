from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of routes.
admin = Blueprint('admin', __name__)

#------------------------------------------------------------
# Return a lost of all modules and statuses 
@admin.route('/modules', methods=['GET'])
def get_modules():
    query = f'''
        SELECT moduleName, moduleStatus
        FROM Module
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Allow the Admin add a new module 
@admin.route('/modules', methods=['POST'])
def post_modules():
    the_data = request.json

    query = f'''
        INSERT INTO Module (moduleName, moduleStatus, createdBy)
        VALUES ('{the_data['moduleName']}', '{the_data['moduleStatus']}', {the_data['createdBy']}),
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Module created successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Get/see a list of all users and their permissions 
@admin.route('/user_permissions', methods=['GET'])
def get_user_perms():

    query = f'''SELECT *
                FROM Permission 
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#------------------------------------------------------------
# Add a new user and permissions 
@admin.route('/user_permissions', methods=['POST'])
def add_user_perms (userId):
    the_data = request.json
    query = f'''INSERT INTO Permission (createdBy, userType, canEditPerms, canEditModule, canEditAccSettings, 
                    canCreateReview, canCreateCoopListing, canCreateModule, canViewReview, canViewCoopListing, 
                    canViewModule, canDeleteReview, canDeleteCoopListing, canDeleteModule)
                VALUES ({userId},'{the_data['userType']}',{the_data['canEditPerms']}, {the_data['canEditModule']}, 
                {the_data['canEditAccSettings']}, {the_data['canCreateReview']}, {the_data['canCreateCoopListing']}, 
                {the_data['canCreateModule']}, {the_data['canViewReview']}, {the_data['canViewCoopListing']}, 
                {the_data['canViewModule']}, {the_data['canDeleteReview']}, {the_data['canDeleteCoopListing']}, 
                {the_data['canDeleteModule']}) 

    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Permission created successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Update existing user permissions 
@admin.route('/user_permissions', methods=['PUT'])
def update_user_perms ():
    the_data = request.json
    query = f'''UPDATE Permission
                SET canEditPerms = {the_data['canEditPerms']}, canEditModule = {the_data['canEditModule']}, 
                canEditAccSettings = {the_data['canEditAccSettings']}, canCreateReview = {the_data['canCreateReview']}, canCreateCoopListing = {the_data['canCreateCoopListing']}, canCreateModule = {the_data['canCreateModule']}, canViewReview = {the_data['canViewReview']}, canViewCoopListing = {the_data['canViewCoopListing']}, 
                canViewModule = {the_data['canViewModule']}, canDeleteReview = {the_data['canDeleteReview']}, 
                canDeleteCoopListing = {the_data['canDeleteCoopListing']}, canDeleteModule = {the_data['canDeleteModule']})
                {the_data['canEditModule']}
                WHERE userType = {the_data['userType']}
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    response = make_response("Permission updated successfully")
    response.status_code = 200
    return response

#------------------------------------------------------------
# Delete a user or permissions 
@admin.route('/user_permissions', methods=['DELETE'])
def delete_user_perms(user_id):
    the_data = request.json
    query = f'''DELETE FROM User
                WHERE userId = {the_data['userId']}; 

    '''
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response