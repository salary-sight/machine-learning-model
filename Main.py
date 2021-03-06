from flask import Flask
from flask_cors import CORS
from flask_restful import reqparse, abort, Api, Resource
import pickle
import pandas as pd
import pycountry

app = Flask(__name__)
CORS(app)
api = Api(app)

edu_map = pd.read_csv(r'/Users/xiangqian.hongibm.com/Desktop/HTV/machine-learning-model/edu_map.csv')
country_map = pd.read_csv(r'/Users/xiangqian.hongibm.com/Desktop/HTV/machine-learning-model/country_map.csv')

# # create new model object
model = pickle.load(open(r"/Users/xiangqian.hongibm.com/Desktop/HTV/machine-learning-model/linear_model.sav", "rb"))

parser = reqparse.RequestParser()
parser.add_argument('YearsCode', required=True, type=int)
parser.add_argument('EdLevel', required=True)
parser.add_argument('Skills', required=True)
parser.add_argument('Experiences', required=True)


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
# for s in skills:
#     parser.add_argument(s, required=True)

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
# for s in jobs:
#     parser.add_argument(s, required=True)


def formatDf(df):
    df = df.merge(edu_map, on='EdLevel', how='left')
    df = df.merge(country_map, on='Country', how='left')
    df = df.drop(['EdLevel', 'Country', 'Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)
    return df[['YearsCode', 'CountryAvgComp', 'EducationAvgComp',
       'Academic researcher', 'Data or business analyst',
       'Data scientist or machine learning specialist',
       'Database administrator', 'Designer', 'DevOps specialist',
       'Developer, QA or test', 'Developer, back-end',
       'Developer, desktop or enterprise applications',
       'Developer, embedded applications or devices', 'Developer, front-end',
       'Developer, full-stack', 'Developer, game or graphics',
       'Developer, mobile', 'Educator', 'Engineer, data',
       'Engineer, site reliability', 'Engineering manager', 'Product manager',
       'Scientist', 'Senior executive/VP', 'Student', 'System administrator',
       'Assembly', 'Bash/Shell/PowerShell', 'C', 'C#', 'C++', 'Go', 'HTML/CSS',
       'Java', 'JavaScript', 'Kotlin', 'Objective-C', 'Other(s):', 'PHP',
       'Python', 'R', 'Ruby', 'Rust', 'SQL', 'Scala', 'Swift', 'TypeScript',
       'VBA', 'Cassandra', 'DynamoDB', 'Elasticsearch', 'Firebase', 'MariaDB',
       'Microsoft SQL Server', 'MongoDB', 'MySQL', 'Oracle', 'PostgreSQL',
       'Redis', 'SQLite', 'Linux', 'Windows', 'Android',
       'Google Cloud Platform', 'AWS', 'Docker', 'Heroku', 'MacOS', 'Slack',
       'iOS', 'Microsoft Azure', 'WordPress', 'Arduino', 'Raspberry Pi',
       'Kubernetes', 'Express', 'Ruby on Rails', 'Angular/Angular.js',
       'ASP.NET', 'Django', 'Flask', 'jQuery', 'Vue.js', 'Spring', 'React.js',
       'Laravel']]

class PredictSalary(Resource):
    def post(self):
        args = parser.parse_args()

        query = {}
        for i in args:
            if i == 'Skills':
                for j in skills:
                    if j in i:
                        query[j] = 1
                    else:
                        query[j] = 0
            elif i == 'Experiences':
                for j in jobs:
                    if j in i:
                        query[j] = 1
                    else:
                        query[j] = 0
            else:
                query[i] = args[i]


        ret = []

        for i in country_map.Country:
            query["Country"] = i
            formatted = formatDf(pd.DataFrame(query, index=[0]))
            # print(pycountry.countries.search_fuzzy(i))
            search = pycountry.countries.search_fuzzy(i)
            country = search[0]
            # if len(search) > 1:
            #     print(i, search)
            ret.append({
                "id": country.alpha_2,
                "name": country.name,
                "value": abs(model.predict(formatted)[0])
            })

        return {"data": ret}

if __name__ == '__main__':
    app.run(debug=True)

api.add_resource(PredictSalary, '/')



