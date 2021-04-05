from db.run_sql import run_sql
from models.gym_class import Gym_Class
from models.member import Member

import repositories.member_repository as member_repository

def save(gym_class):
    sql = "INSERT INTO gym_classes (name, date, time, capacity) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.capacity]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        
        gym_class = Gym_Class(row['name'], row['date'], row['time'], row['capacity'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_Class(result['name'], result['date'], result['time'], result['capacity'], result['id'])
    return gym_class

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)



