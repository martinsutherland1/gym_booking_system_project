from flask import Flask, render_template

# from controllers.members_controller import members_blueprint
# from controllers.gym_classes_controller import gym_class_blueprint
# from controllers.sessions_controller import sessions_blueprint

app = Flask(__name__)

# app.register_blueprint(members_blueprint)
# app.register_blueprint(gym_class_blueprint)
# app.register_blueprint(sessions_blueprint)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ ==('__main__'):
    app.run(debug=True)
