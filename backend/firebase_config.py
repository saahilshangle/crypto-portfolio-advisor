import pyrebase

config = {
  "apiKey": "AIzaSyBjFIYioSoHUkWplkE9BeNZe7qIrPnpeNs",
  "authDomain": "crypto-robo-advisor-8315f.firebaseapp.com",
  "databaseURL": "https://crypto-robo-advisor-8315f-default-rtdb.firebaseio.com",
  "storageBucket": "crypto-robo-advisor-8315f.appspot.com"
}

firebase = pyrebase.initialize_app(config)

#initialize Firebase Database
db = firebase.database()

#example of pushing data to database
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)