import subprocess

def handler(request):
    subprocess.run(["streamlit", "run", "dashboard/app.py"])