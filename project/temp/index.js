  

  function createAccount()
  {
      //var nickname = document.getElementById("nickname_field"); 
      var email = document.getElementById("email_field");
      var pass = document.getElementById("password_field");
      
      const promise = auth.createUserWithEmailAndPassword(email.value, pass.value);
      promise.catch(e => alert(e.message));
      
      firebase.database().ref("Users").child("User").set(
        {
          email: document.getElementById("email_field").value,
          password: document.getElementById("password_field").value
        });

      alert("Signed Up");

        // yeet user to home page
        window.location.href = 'login.html';
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
        // TODO: steven - figure out what to do with the guests in the database 

        // yeet user to home page 
        alert("Welcome, " + nickname_field.value + "!!"); 
        window.location.href = 'home-page.html';
    }

    // auth.onAuthStateChanged(function(user)
    // {
    //     if(user)
    //     {
    //         var email = user.email;
    //         alert("Active User " + email);
    //         // is signed in
    //     }
    //     else
    //     {
    //         alert("No Active User");
    //         // no user is signed in
    //     }
    // });
