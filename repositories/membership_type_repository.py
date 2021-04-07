from db.run_sql import  run_sql

from models.membership_type import Membership_type

def save(membership_type):
    sql = "INSERT INTO membership_types (name) VALUES (%s) RETURNING id"
    values = [membership_type.name]
    results = run_sql(sql, values)
    membership_type.id = results[0]['id']
    return membership_type

def select_all():
    membership_types = []

    sql = "SELECT * FROM membership_types"
    results = run_sql(sql)
    for row in results:
        membership_type = Membership_type(row["name"], row["id"])  
        membership_types.append(membership_type)
    return membership_types

def select(id):
    membership_type = None
    sql = "SELECT * FROM membership_types WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    
    if result is not None:
        membership_type = Membership_type(result["name"], result["id"])
    return membership_type


def delete_all():
    sql = "DELETE FROM membership_types"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM membership_types WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(membership_type):
    sql = "UPDATE membership_types SET (name) = (%s) WHERE id = %s"
    values = [membership_type.name, membership_type.id]
    run_sql(sql, values)
