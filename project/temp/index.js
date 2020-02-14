  
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
      var nickname = document.getElementID("nickname_field"); 

      // TODO: steven - set up database so it can create account/handle errors 
      if(document.getElementById("password_field") == document.getElementById("password_confirm_field")) 
      {
        const promise = auth.createUserWithEmailAndPassword(email_field.value, password_field.value);
        promise.catch(e => alert(e.message));

        alert("Sign up complete!");

        // yeet user to home page
        window.location.href = 'login.html';
      }
  }
      
    function login()
    {
        var email = document.getElementById("email_field");
        var pass = document.getElementById("password_field");
        
        const promise = auth.signInWithEmailAndPassword(email_field.value, password_field.value);
        promise.catch(e => alert(e.message));
   
        alert("Successfully logged in"); 

        // yeet user to home page
        window.location.href = 'home-page.html';
    }

    function signOut()
    {
        auth.signOut();
        alert("Signed Out");
    }

    function continueGuest()
    {
        window.location.href = 'home-page.html';
        // TODO: steven - figure out what to do with the guests in the database 
        alert("alert~");
        var nickname = document.getElementID("nickname_field"); 

        // yeet user to home page 
        alert("Welcome, " + nickname + "!!"); 
        window.location.href = 'home-page.html';
    }

    auth.onAuthStateChanged(function(user)
    {
        if(user)
        {
            var email = user.email;
            alert("Active User " + email);
            // is signed in
        }
        else
        {
            alert("No Active User");
            // no user is signed in
        }
    });
