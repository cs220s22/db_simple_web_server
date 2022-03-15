from flask import Flask
from redis import Redis


app = Flask(__name__)
r = Redis('redis')


def read_count():
    val = r.get('count')
    if val is None:
        return 0
    return int(val)


def save_count(count):
    r.set('count', count)


@app.route("/")
def hello():
    count = read_count()    
    count += 1
    save_count(count);
    return "<h1 style='color:red'>Hello World! {}</h1>".format(count)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
