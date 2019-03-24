from flask import Flask
import sys
app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def handle_response():
      
      
      return 'Hello, World!'

      