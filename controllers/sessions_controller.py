from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_Class
from models.session import Session
from models.member import Member


import repositories.session_repository as session_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository


sessions_blueprint = Blueprint("sessions/add", __name__)

@sessions_blueprint.route("/gym_classes/add", methods=['GET'])
def sessions():
   
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/add.html", members=members, gym_classes=gym_classes)

@sessions_blueprint.route("/gym_classes/add", methods=['POST'])
def new_session():
   member_id = request.form['member_id']
   gym_class_id = request.form['gym_class_id']
   member = member_repository.select(member_id)
   gym_class = gym_class_repository.select(gym_class_id)
   session = Session(member, gym_class)
   current_capacity = gym_class_repository.check_class_capacity(gym_class.id)
   duplicate = session_repository.check_member_in_class(member.id, gym_class.id)
   
   if member.membership_type == 7 and gym_class.class_type == "Premier":
        return render_template("gym_classes/membership.html")
   if  duplicate > 0:
       return render_template("gym_classes/duplicate.html")
   if current_capacity == gym_class.capacity:
        return render_template("gym_classes/full.html")
   else:
        session_repository.save(session)
        return redirect('/gym_classes')
        
@sessions_blueprint.route("/gym_classes/remove")
def remove():
    gym_classes = gym_class_repository.select_all()
    members = member_repository.select_all()
    return render_template("gym_classes/remove.html", members=members, gym_classes=gym_classes)

@sessions_blueprint.route("/gym_classes/remove", methods=['POST'])
def remove_member_from_class():
   member_id = request.form['member_id']
   gym_class_id = request.form['gym_class_id']
   member = member_repository.select(member_id)
   gym_class = gym_class_repository.select(gym_class_id)
   session_repository.delete_by_member(member.id, gym_class.id)
   return redirect ('/gym_classes')

   



