python clean.py
pip freeze > requirements.txt
git add .
git commit -am "commit changes"
git push heroku master
heroku ps:scale worker=1