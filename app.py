from flask import Flask
application = Flask(__name__)

@application.route("/", methods=['POST','GET'])
def hello():
  return 'hello!'

if __name__ == "__main__":
  application.run(host='0.0.0.0')
