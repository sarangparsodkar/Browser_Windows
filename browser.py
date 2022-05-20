#------------------------------------------------------------------ TO RUN -------------------------------------------------------#
## set FLASK_APP=browser.py
## $env:FLASK_APP = "browser.py"
## python -m flask run

from os import system
from this import s
from flask import Flask, render_template, request
from pywinauto import Application

app = Flask(__name__)
app.debug = True
@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")

#------------------------------------------------------------------ STARTS BROWSER -------------------------------------------------------#

@app.route('/start', methods=['GET'])
def start():				
				
    if 'browser' in request.args and 'url' in request.args:
    
        print ("Testing");
        browser_name = str(request.args['browser'])
        url = str(request.args['url'])
        print (browser_name);
        print (url);
        
        if browser_name == "chrome":
            import webbrowser, os
            os.system("start " + browser_name + " " + url)
            return "Chrome fired up with specified url"
            
        elif browser_name == "firefox":
            import webbrowser, os
            os.system("start " + browser_name + " " + url)
            return "Mozilla fired up with specified url"
            
        else:
            return "This browser isnt available"
            
            
    elif 'browser' in request.args:
        browser_name = str(request.args['browser'])
        
        if browser_name == "chrome":
            import os
            browserExe = "chrome"
            os.system("start " + browserExe)
            return "Chrome fired up"
            
        elif browser_name == "firefox":
            import os
            browserExe = "firefox"
            os.system("start " + browserExe)
            return "Mozilla fired up "
            
        else:
            return "This browser isnt available"
            
    elif 'url' in request.args:
        return "Error only url provided"

#------------------------------------------------------------- STOPS BROWESER ---------------------------------------------------------------#

@app.route('/stop', methods=['GET'])

def stop():				
			
    if 'browser' in request.args:
    
        browser_name = str(request.args['browser'])
        print (browser_name);
        
        if browser_name == "chrome":
            import os
            browserExe = "chrome"
            os.system("tskill " + browserExe)
            return "CHROME CLOSED"
            
        elif browser_name == "firefox":
            import os
            os.system("tskill " + "firefox")
            return "MOZILLA CLOSED"
            
        else:
            return "This browser isnt available"
            
    else:
        return "Browser name required"

##-------------------------------------------------------- DELETE ALL BROWSING SESSIONS ----------------------------------------------------##

@app.route('/cleanup', methods=['GET'])

def cleanup():

    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print (browser_name);
        
        if browser_name == "chrome":
            # Successfully DELETS chrome content
            import os,shutil
            ChromeDir="C:/Users/sarang.parsodkar/AppData/Local/Google/Chrome/User Data/"
            print (ChromeDir)
            for files in os.listdir(ChromeDir):
                path = os.path.join(ChromeDir, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                   os.remove(path)
            #os.rmdir(ChromeDir)
            #shutil.rmtree(ChromeDir)
            #os.system ("del /q /s /f " + ChromeDir )
            #os.system(" rd /s /q " + ChromeDir )
            return "Chrome Data IS CLEARED"
            
        elif browser_name == "firefox":
            # Successfully DELETS firefox content
            import os,shutil
            FirefoxDir = "C:/Users/sarang.parsodkar/AppData/Roaming/Mozilla/Firefox/Profiles/sunmigwj.Default User/"
            print (FirefoxDir)
            for files in os.listdir(FirefoxDir):
                path = os.path.join(FirefoxDir, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                   os.remove(path)
            #os.system ("del /q /s /f " + FirefoxDir )
            #os.system(" rd /s /q " + FirefoxDir )
            return "Firefox Data IS CLEARED"
            
    else:
        return "No query passed for filtration"

##-------------------------------------------------------- GET URL ----------------------------------------------------##

@app.route('/geturl', methods=['GET'])

def geturl():

    if 'browser' in request.args:
        browser_name = str(request.args['browser'])
        print (browser_name);
        
        if browser_name == "chrome":
            app = Application(backend='uia')
            app.connect(title_re=".*Chrome.*")
            dlg = app.top_window()
            url = dlg.child_window(title="Address and search bar", control_type="Edit").get_value()
            print(url)
            return url
            
        elif browser_name == "firefox":
            app = Application(backend='uia')
            app.connect(title_re=".*Mozilla Firefox.*")
            dlg = app.top_window()
            url = dlg.child_window(title="Search with Google or enter address", control_type="Edit").get_value()
            print(url)
            return url
    else:
        return "No query passed for filtration"

#-------------------------------------------------------------------------------------------------------------------------------------------##

if __name__ == '__main__':
    app.run(debug=True, port=8000)
    
