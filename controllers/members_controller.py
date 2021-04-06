from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.gym_class import Gym_Class
from models.session import Session
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.session_repository as session_repository

members_blueprint = Blueprint("members", __name__)

@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members=members)

@members_blueprint.route("/members/<id>")
def show(id):
    member = member_repository.select(id)
    gym_classes = gym_class_repository.get_by_member(member)

    return render_template("members/show.html", gym_classes=gym_classes, member=member)

@members_blueprint.route("/members/new_member", methods=['GET'])
def new():
    members = member_repository.select_all()
    return render_template("members/new.html", members=members)

@members_blueprint.route("/members", methods=['POST'])
def create():
    name = request.form["name"]
    age = request.form["age"]
    member = Member(name, age)
    member_repository.save(member)
    return redirect("/members")

@members_blueprint.route("/members/<id>/delete", methods=["post"])
def delete(id):
    member = member_repository.delete(id)
    return redirect("/members")

@members_blueprint.route("/members/<id>/edit")
def edit(id):
    member = member_repository.select(id)
    return render_template("members/edit.html", member=member)

@members_blueprint.route("/members/<id>", methods=['POST'])
def update(id):
    name = request.form["name"]
    age = request.form["age"]
    member = Member(name, age, id)
    member_repository.update(member)
    return redirect(f"/members")

   







