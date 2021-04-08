from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
from models.gym_class import Gym_Class
from models.session import Session
from models.membership_type import Membership_type
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.session_repository as session_repository
import repositories.membership_type_repository as membership_type_repository

membership_type_blueprint = Blueprint("membership_types", __name__)

@membership_type_blueprint.route("/membership_types")
def membership_types():
    membership_types = membership_type_repository.select_all()
    return render_template("membership_types/index.html", membership_types=membership_types)

@membership_type_blueprint.route("/membership_types/<id>")
def show(id):
    membership_type = membership_type_repository.select(id)

    return render_template("/membership_types/show.html", membership_type=membership_type)

@membership_type_blueprint.route("/membership_types/new_membership", methods=['GET'])
def new():
    membership_types = membership_type_repository.select_all()
    return render_template("/membership_types/new_mem.html", membership_types=membership_types)

@membership_type_blueprint.route("/membership", methods=['POST'])
def create():
    name = request.form["name"]
    membership_type = Membership_type(name)
    membership_type_repository.save(membership_type)
    return redirect("/membership_types")

@membership_type_blueprint.route("/membership_types/<id>/delete", methods=['POST'])
def delete(id):
    membership_type = membership_type_repository.delete(id)
    return redirect("/membership_types")

@membership_type_blueprint.route("/membership_types/<id>/edit")
def edit(id):
    membership_type = membership_type_repository.select(id)
    return render_template("membership_types/edit.html", membership_type=membership_type)
   

@membership_type_blueprint.route("/membership_types/<id>", methods=['POST'])
def update(id):
    name = request.form["name"]

    membership_type = Membership_type(name, id)
    membership_type_repository.update(membership_type)
    return redirect(f"/membership_types")