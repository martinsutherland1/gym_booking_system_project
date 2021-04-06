from db.run_sql import run_sql
from models.session import Session
import repositories.gym_class_repository as gym_class_repository
import repositories.member_repository as member_repository

def save(session):
    sql = "INSERT INTO sessions (member_id, gym_class_id) VALUES (%s, %s) RETURNING id"
    values = [session.member.id, session.gym_class.id]
    results = run_sql(sql, values)
    session.id = results[0]['id']
    return session

def select_all():
    sessions = []

    sql = "SELECT * FROM sessions"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        gym_class = gym_class_repository.select(row['gym_class_id'])
        session = Session(member, gym_class, row['id'])
        sessions.append(session)
    return sessions

def delete_all():
    sql = "DELETE FROM sessions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sessions where id = %s"
    values = [id]
    run_sql(sql, values)

def delete_by_member(member_id, gym_class_id):
    sql = "DELETE FROM sessions WHERE sessions.member_id = %s AND sessions.gym_class_id = %s"
    values = [member_id, gym_class_id]
    run_sql(sql, values)
    
