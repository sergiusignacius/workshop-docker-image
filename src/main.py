from flask import Flask
import redis
import datetime

app = Flask(__name__)

r = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route("/")
def index():
    r.rpush('visits', datetime.datetime.utcnow())
    count = r.llen('visits')
    if count == 1:
        return "You have accessed this website 1 time"
    else:
        return "You have accessed this website {count} times".format(count=count)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
