from db.run_sql import run_sql
from models.gym_class import Gym_Class
from models.member import Member

import repositories.member_repository as member_repository

def save(gym_class):
    sql = "INSERT INTO gym_classes (name, date, time, capacity, class_type) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.capacity, gym_class.class_type]
    results = run_sql(sql, values)
    gym_class.id = results[0]['id']
    return gym_class

def select_all():
    gym_classes = []

    sql = "SELECT * FROM gym_classes"
    results = run_sql(sql)

    for row in results:
        
        gym_class = Gym_Class(row['name'], row['date'], row['time'], row['capacity'], row['class_type'], row['id'])
        gym_classes.append(gym_class)
    return gym_classes


def select(id):
    gym_class = None
    sql = "SELECT * FROM gym_classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        gym_class = Gym_Class(result['name'], result['date'], result['time'], result['capacity'], result['class_type'], result['id'])
    return gym_class

def delete_all():
    sql = "DELETE FROM gym_classes"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM gym_classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(gym_class):
    sql = "UPDATE gym_classes SET (name, date, time, capacity, class_type) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [gym_class.name, gym_class.date, gym_class.time, gym_class.capacity, gym_class.class_type, gym_class.id]
    run_sql(sql, values)
    

def get_by_member(member):
    sql = "SELECT gym_classes.* FROM gym_classes INNER JOIN sessions ON gym_classes.id = sessions.gym_class_id WHERE sessions.member_id = %s"
    values = [member.id]
    results = run_sql(sql, values)

    gym_classes = []

    for row in results:
        gym_class = Gym_Class(row['name'], row['date'], row['time'], row['capacity'], row['class_type'])
        gym_classes.append(gym_class)

    return gym_classes
    
def check_class_capacity(id):
    sql = "SELECT count(*) FROM sessions WHERE gym_class_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        count = row['count']

    return count


