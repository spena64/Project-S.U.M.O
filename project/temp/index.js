  
  // Your web app's Firebase configuration
  var firebaseConfig = 
  {
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
  firebase.analytics();

  const auth = firebase.auth();

  function createAccount()
  {
      var email = document.getElementById("email_field");
      var pass = document.getElementById("password_field");
      
      const promise = auth.createUserWithEmailAndPassword(email_field.value, password_field.value);
      promise.catch(e => alert(e.message));

      alert("Sign up complete!");

      // yeet user to home page 
  }
      
    function login()
    {
        var email = document.getElementById("email_field");
        var pass = document.getElementById("password_field");
        
        const promise = auth.signInWithEmailAndPassword(email_field.value, password_field.value);
        promise.catch(e => alert(e.message));
  

        //take user to a different or home page 
        alert("Successfully logged in"); 
    }

    function signOut()
    {
        auth.signOut();
        alert("Signed Out");
    }


    auth.onAuthStateChanged(function(user)
    {
        if(user)
        {
            var email = user.email;
            alert("Active User " + email);
            //is signed in
        }
        else
        {
            alert("No Active User");
            //no user is signed in
        }
    });
