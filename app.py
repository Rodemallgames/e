from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():'
    return 'Hello and this is the official Rodemallgames Development website. We are a small Roblox development group that made a game with over 500k visits. We will continue development on the website but, for now, it will look like this. Thanks for visiting!'


if __name__ == "__main__":
    app.run()
