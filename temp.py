# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np

edu_map = pd.read_csv('edu_map.csv')
country_map = pd.read_csv('country_map.csv')

def format_count_edu(df):
    df = df.merge(edu_map, on='EdLevel', how='left')
    df = df.merge(country_map, on='Country', how='left')
    df = df.drop(['EdLevel', 'Country', 'Unnamed: 0_x', 'Unnamed: 0_y'], axis=1)
    return df

test = {'YearsCode': [12],
'Country': ['United States'],
'EdLevel': ['Master’s degree (MA, MS, M.Eng., MBA, etc.)'],
'Academic researcher': [0],
'Data or business analyst': [0],
'Data scientist or machine learning specialist': [0],
'Database administrator': [0],
'Designer': [0],
'DevOps specialist': [0],
'Developer, QA or test': [0],
'Developer, back-end': [0],
'Developer, desktop or enterprise applications': [0],
'Developer, embedded applications or devices': [1],
'Developer, front-end': [0],
'Developer, full-stack': [0],
'Developer, game or graphics': [0],
'Developer, mobile': [0],
'Educator': [0],
'Engineer, data': [0],
'Engineer, site reliability': [0],
'Engineering manager': [0],
'Product manager': [0],
'Scientist': [0],
'Senior executive/VP': [0],
'Student': [0],
'System administrator': [0],
'Assembly': [1],
'Bash/Shell/PowerShell': [0],
'C': [1],
'C#': [0],
'C++': [1],
'Go': [1],
'HTML/CSS': [0],
'Java': [0],
'JavaScript': [0],
'Kotlin': [0],
'Objective-C': [0],
'Other(s):': [0],
'PHP': [0],
'Python': [0],
'R': [0],
'Ruby': [0],
'Rust': [0],
'SQL': [0],
'Scala': [0],
'Swift': [0],
'TypeScript': [0],
'VBA': [0],
'Cassandra': [0],
'DynamoDB': [0],
'Elasticsearch': [0],
'Firebase': [0],
'MariaDB': [0],
'Microsoft SQL Server': [0],
'MongoDB': [0],
'MySQL': [0],
'Oracle': [0],
'PostgreSQL': [0],
'Redis': [0],
'SQLite': [0],
'Linux': [1],
'Windows': [1],
'Android': [1],
'Google Cloud Platform': [0],
'AWS': [0],
'Docker': [0],
'Heroku': [0],
'MacOS': [0],
'Slack': [0],
'iOS': [0],
'Microsoft Azure': [0],
'WordPress': [0],
'Arduino': [1],
'Raspberry Pi': [1],
'Kubernetes': [0],
'Express': [0],
'Ruby on Rails': [0],
'Angular/Angular.js': [0],
'ASP.NET': [0],
'Django': [0],
'Flask': [0],
'jQuery': [0],
'Vue.js': [0],
'Spring': [0],
'React.js': [0],
'Laravel': [0]}

test_df = pd.DataFrame(test)

new_test = format_count_edu(test_df)

print(new_test.columns)