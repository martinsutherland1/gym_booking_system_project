from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_Class
from models.session import Session
from models.member import Member


import repositories.session_repository as session_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository


sessions_blueprint = Blueprint("sessions/add", __name__)

@sessions_blueprint.route("/sessions", methods=['GET'])
def sessions():
   
    members = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    return render_template("sessions/add.html", members=members, gym_classes=gym_classes)

@sessions_blueprint.route("/sessions", methods=['POST'])
def new_session():
   member_id = request.form['member_id']
   gym_class_id = request.form['gym_class_id']
   member = member_repository.select(member_id)
   gym_class = gym_class_repository.select(gym_class_id)
   session = Session(member, gym_class)
   session_repository.save(session)
   return redirect('/sessions')






