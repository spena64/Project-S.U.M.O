import pyrebase

config = {
  'apiKey': "AIzaSyAOk918OH35Ie5dx62O6HX4KmaSLn58cHQ",
  'authDomain': "project-sumo-e6f87.firebaseapp.com",
  'databaseURL': "https://project-sumo-e6f87.firebaseio.com",
  'projectId': "project-sumo-e6f87",
  'storageBucket': "project-sumo-e6f87.appspot.com",
  'messagingSenderId': "548557512640",
  'appId': "1:548557512640:web:2913ecd0b8c1ba3a24b225",
  'measurementId': "G-W9VE8EX4DC",
  "serviceAccount": './ServiceAccountKey.json'
};


firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# userId = auth.sign_in_with_custom_token(email, password)

db = firebase.database()

# Pass the user's id to update their data
# TODO get the current userID using the uid instead of hardcoding the changes

results = db.child("Users").child('EpZIBBHlPYXi4J9pd7dpDYOyNtU2').update({'wins': '0','losses':'11'})

