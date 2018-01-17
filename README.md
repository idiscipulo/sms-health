# sms-health
An SMS-based web app, seeking to provide medical advice to areas with poor data network infrastructure and delayed medical services. This projected was written in Python using the Twilio API and is deployed through Heroku. It was created as our entry for HackAZ 2018.

### Requirements
* Python 3.6
* Twilio
* Heroku

### To Run
1) Create a Heroku app on their website.
2) Login to Heroku on the console using `heroku login`
3) Enter `heroku git:clone -a YOUR_APP_NAME`
4) Download the sms-health files into your new, local repository
5) Get your Twilio account information (SID, auth, and number) and enter into the fields in run.py and clean.py
6) Enter `make` to run the make.bat file

### To Use
Your new app should now process any SMS messages that you send to your Twilio number. Note that with a trial account you must register your number for Twilio to recieve messages.
