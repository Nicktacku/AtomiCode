from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
from lexer import Lexer
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

class HelloWorld(Resource):
    def get(self, content):
        lexer = Lexer(content)

        content_output = lexer.to_token()
        new_lexemes = [str(i) for i in content_output]

        lexeme = [i[i.find(" "): ].strip() for i in new_lexemes]
        token = [i[:i.find(" ") ].strip() for i in new_lexemes]

        return jsonify({"code" : str(content),
                        "lexeme" : list(lexeme),
                        "token" : list(token)})

api.add_resource(HelloWorld, "/helloworld/<string:content>")

if __name__ == "__main__":
    app.run(debug=True)