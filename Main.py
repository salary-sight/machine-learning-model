from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
api = Api(app)

# # create new model object
model = pickle.load(open("linear_model.sav", "rb"))

parser = reqparse.RequestParser()
parser.add_argument('YearsCode', required=True, type=int)
parser.add_argument('Country', required=True)
parser.add_argument('EdLevel', required=True)

skills = ['Assembly', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'Go', 'HTML/CSS',
          'Java', 'JavaScript', 'Kotlin', 'Objective-C', 'Other(s):', 'PHP',
          'Python', 'R', 'Ruby', 'Rust', 'SQL', 'Scala', 'Swift', 'TypeScript',
          'VBA', 'Cassandra', 'DynamoDB', 'Elasticsearch', 'Firebase', 'MariaDB',
          'Microsoft SQL Server', 'MongoDB', 'MySQL', 'Oracle', 'PostgreSQL',
          'Redis', 'SQLite', 'Linux', 'Windows', 'Android',
          'Google Cloud Platform', 'AWS', 'Docker', 'Heroku', 'MacOS', 'Slack',
          'iOS', 'Microsoft Azure', 'WordPress', 'Arduino', 'Raspberry Pi',
          'Kubernetes', 'Express', 'Ruby on Rails', 'Angular/Angular.js',
          'ASP.NET', 'Django', 'Flask', 'jQuery', 'Vue.js', 'Spring', 'React.js',
          'Laravel']
for s in skills:
    parser.add_argument(s, required=True)

jobs = ['Academic researcher', 'Data or business analyst',
        'Data scientist or machine learning specialist',
        'Database administrator', 'Designer', 'DevOps specialist',
        'Developer, QA or test', 'Developer, back-end',
        'Developer, desktop or enterprise applications',
        'Developer, embedded applications or devices', 'Developer, front-end',
        'Developer, full-stack', 'Developer, game or graphics',
        'Developer, mobile', 'Educator', 'Engineer, data',
        'Engineer, site reliability', 'Engineering manager', 'Product manager',
        'Scientist', 'Senior executive/VP', 'Student', 'System administrator']
for s in jobs:
    parser.add_argument(s, required=True)

class PredictSalary(Resource):
    def post(self):
        args = parser.parse_args()

        query = {}
        for i in args:
            query[i] = args[i]

        return predict(pd.DataFrame(query))


def predict(df):
    return {}

if __name__ == '__main__':
    app.run(debug=True)

api.add_resource(PredictSalary, '/')

