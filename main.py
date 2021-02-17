import threading
import time
import flask
from engine import Engine
import os
from flask import request


class Observer (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.waterLevel = 0
        self.inflow = 0
        self.currentRegulator = 'fuzzy'

    def run(self):
        while True:
            time.sleep(1)
            print(app.engineThread.waterLevel)


class MyFlaskApp(flask.Flask):
    def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
        if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
            with self.app_context():
                self.engineThread = Engine(1, "Engine", 1)
                self.engineThread.start()
                self.observer = Observer(1, "Observer", 1)
                self.observer.start()
        super(MyFlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)



app = MyFlaskApp(__name__)
app.config["DEBUG"] = True


@app.route('/modelState', methods=['GET', 'POST'])
def modelState():
    if request.method == 'POST':
        if 'waterLevel' in flask.request.json:
            app.engineThread.waterLevel = flask.request.json['waterLevel']
        if 'inflow' in flask.request.json:
            app.engineThread.inflow = flask.request.json['inflow'] / 1000
        if 'currentRegulator' in flask.request.json:
            app.engineThread.currentRegulator = flask.request.json['currentRegulator']
        return 'OK'
    elif request.method == 'GET':
        return {
            'waterLevel': app.engineThread.waterLevel,
            'inflow': app.engineThread.inflow * 1000,
            'currentRegulator': app.engineThread.currentRegulator
        }

@app.route('/modelParameters', methods=['GET', 'POST'])
def modelParameters():
    if request.method == 'POST':
        if 'baseField' in flask.request.json:
            app.engineThread.model.base_field = flask.request.json['baseField']
        if 'setLevel' in flask.request.json:
            app.engineThread.aim = flask.request.json['setLevel']
        return 'OK'
    elif request.method == 'GET':
        return {
            'baseField': app.engineThread.model.base_field,
            'setLevel': app.engineThread.aim
        }


@app.route('/pidParameters', methods=['GET', 'POST'])
def pidParameters():
    if request.method == 'POST':
        if 'kp' in flask.request.json:
            app.engineThread.pid.Kp = flask.request.json['kp']
        if 'ti' in flask.request.json:
            app.engineThread.pid.Ti = flask.request.json['ti']
        if 'td' in flask.request.json:
            app.engineThread.pid.Td = flask.request.json['td']
        return 'OK'
    elif request.method == 'GET':
        return {
            'kp': app.engineThread.pid.Kp,
            'ti': app.engineThread.pid.Ti,
            'td': app.engineThread.pid.Td
        }

@app.route('/fuzzyParameters', methods=['GET', 'POST'])
def fuzzyParameters():
    if request.method == 'POST':
        if 'kp' in flask.request.json:
            app.engineThread.fuzzy.base_of_regules.data = flask.request.json['baseOfRules']
        return 'OK'
    elif request.method == 'GET':
        return {
            "baseOfRules": app.engineThread.fuzzy.base_of_regules.data
        }

app.run(host= '0.0.0.0')



