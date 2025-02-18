from flask import Flask
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    ist_time = datetime.datetime.now(ist)
    
    # Get top command output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    
    # Get username
    username = subprocess.check_output(['whoami']).decode('utf-8').strip()
    
    # Format the response
    response = f"""Name: sample_name
user: {username}
Server Time (IST): {ist_time.strftime('%Y-%m-%d %H:%M:%S.%f')}
TOP output:
{top_output}"""
    
    return f"<pre>{response}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
