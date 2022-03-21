from flask import Response, render_template
from flask_restful import Resource

class HomePage(Resource):
    def get(self):
        return Response(render_template('index.html', mimetype='text/html'))