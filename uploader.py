
import os
import subprocess

from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
   
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_the_page():
   if request.method == 'POST':
      f = request.files['file']
      print (f.filename)
      f.save(secure_filename(f.filename))
   subprocess.call(['chmod','755','walk.cc'])
   subprocess.call("rm -f ./a.out", shell=True)
   print (subprocess.call("ls -l", shell=True))
      
   retcode = subprocess.call("/usr/bin/g++ "+f.filename, shell=True)
   if retcode:
      print("failed to compile walk.cc")
      exit

   subprocess.call("rm -f ./output", shell=True)
   retcode = subprocess.call("./test.sh", shell=True)
   print ("Score: " + str(retcode) + " out of 2 correct.")
   print("*************Original submission*************")
   with open(f.filename,'r') as fs:
      print(fs.read()) 
   return "Score: " + str(retcode) + " out of 2 correct."
  # return 'file uploaded successfully'
    
if __name__ == '__main__':
   app.run(host="0.0.0.0")
