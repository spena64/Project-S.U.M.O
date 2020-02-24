// Your web app's Firebase configuration
var firebaseConfig = {
    apiKey: "AIzaSyAOk918OH35Ie5dx62O6HX4KmaSLn58cHQ",
    authDomain: "project-sumo-e6f87.firebaseapp.com",
    databaseURL: "https://project-sumo-e6f87.firebaseio.com",
    projectId: "project-sumo-e6f87",
    storageBucket: "project-sumo-e6f87.appspot.com",
    messagingSenderId: "548557512640",
    appId: "1:548557512640:web:2913ecd0b8c1ba3a24b225",
    measurementId: "G-W9VE8EX4DC"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  const database = firebase.database();
  const auth = firebase.auth();