DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS gym_classes;


CREATE TABLE membership_types (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    membership_id int REFERENCES membership_types(id)
    
    
);

CREATE TABLE gym_classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    date VARCHAR(255),
    time VARCHAR(255),
    capacity INT,
    class_type VARCHAR(255)
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    gym_class_id INT REFERENCES gym_classes(id)
);