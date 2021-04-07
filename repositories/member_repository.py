from db.run_sql import run_sql

from models.member import Member
from models.gym_class import Gym_Class


def save(member):
    sql = "INSERT INTO members (name, age, membership_id) VALUES (%s, %s, %s) RETURNING id"
    values = [member.name, member.age, member.membership_type.id]
    results = run_sql(sql, values)
    member.id = results[0]['id']
    return member


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)
    for row in results:
        member = Member(row["name"], row["age"],
                        row["membership_id"], row["id"])
        members.append(member)
    return members


def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['name'], result['age'], result["membership_id"], result['id'])
    return member


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def get_by_class(gym_class):
    sql = "SELECT members.* FROM members INNER JOIN sessions ON members.id = sessions.member_id WHERE sessions.gym_class_id = %s"
    values = [gym_class.id]
    results = run_sql(sql, values)

    members = []

    for row in results:
        member = Member(row['name'], row['age'], row['membership_id'], row['id'])
        members.append(member)

    return members


def update(member):
    sql = "UPDATE members SET (name, age, membership_id) = (%s, %s, %s) WHERE id = %s"
    values = [member.name, member.age, member.membership_type.id, member.id]
    results = run_sql(sql, values)

    

    # for row in results:
    #     member = Member(row["name"], row["age"], row["id"])
    #     members.append(member)
    # return members
