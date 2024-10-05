import os
import subprocess

def start_http_server(port=8000):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_directory)
    subprocess.run(['python', '-m', 'http.server', str(port)])

if __name__ == "__main__":
    start_http_server()
