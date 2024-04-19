from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/execute-python-script', methods=['POST'])
def execute_python_script():
    # Receive data from the request
    data = request.json
    
    # Execute the Python script and capture its output
    result = subprocess.run(['python', 'degrees.py', data['directory']], capture_output=True, text=True)
    
    # Prepare the response
    response = {
        'stdout': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
