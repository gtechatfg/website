from invoke import task
import requests
import json
import subprocess

@task
def build(c):
  #fetch student and college data from api
  colleges = requests.get("https://api.atfg.gtechindia.org/college").json()
  students = requests.get("https://api.atfg.gtechindia.org/students").json()

  #write to json files in data directory
  with open('data/colleges.json', 'w') as outfile:
    json.dump(colleges, outfile)
  with open('data/students.json', 'w') as outfile:
    json.dump(students, outfile)

  #invoke render-hugo buildcommand
  subprocess.run("hugo --gc --minify", shell=True)
