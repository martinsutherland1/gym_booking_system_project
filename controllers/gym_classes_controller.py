from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.gym_class import Gym_Class
from models.session import Session
from models.member import Member

import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository
import repositories.session_repository as session_repository


gym_classes_blueprint = Blueprint("gym_classes", __name__)

@gym_classes_blueprint.route("/gym_classes")
def gym_classes():
    gym_classes = gym_class_repository.select_all()
    
    
    
    return render_template("gym_classes/index.html", gym_classes=gym_classes)

@gym_classes_blueprint.route("/gym_classes/<id>")
def show(id):
    members_all = member_repository.select_all()
    gym_classes = gym_class_repository.select_all()
    gym_class = gym_class_repository.select(id)
    class_capacity = gym_class_repository.check_class_capacity(gym_class.id)
    members = member_repository.get_by_class(gym_class)
    return render_template("gym_classes/show.html", members_all=members_all, gym_class=gym_class, members=members, class_capacity=class_capacity, gym_classes=gym_classes)

@gym_classes_blueprint.route("/gym_classes/create_class", methods=["GET"])
def new():
    gym_classes = gym_class_repository.select_all()
    return render_template("gym_classes/new.html", gym_classes=gym_classes)

@gym_classes_blueprint.route("/gym_classes", methods=['POST'])
def create():
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    class_type = request.form["class_type"]
    
    gym_class = Gym_Class(name, date, time, capacity, class_type)
    gym_class_repository.save(gym_class)
    return redirect("/gym_classes")

@gym_classes_blueprint.route("/gym_classes/<id>/delete", methods=["post"])
def delete(id):
    gym_class = gym_class_repository.delete(id)
    return redirect("/gym_classes")

@gym_classes_blueprint.route("/gym_classes/<id>/edit")
def edit(id):
    gym_class = gym_class_repository.select(id)
    return render_template("gym_classes/edit.html", gym_class=gym_class)

@gym_classes_blueprint.route("/gym_classes/<id>", methods=['POST'])
def update(id):
    name = request.form["name"]
    date = request.form["date"]
    time = request.form["time"]
    capacity = request.form["capacity"]
    class_type = request.form["class_type"]
    gym_class = Gym_Class(name, date, time, capacity, class_type, id)
    gym_class_repository.update(gym_class)
    return redirect("/gym_classes")





    



   
