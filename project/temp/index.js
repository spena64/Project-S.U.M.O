  
  function createAccount()
  { 
    var email = document.getElementById("email_field");
    var pass = document.getElementById("password_field");
    var cpass = document.getElementById("cpassword");
    var firebaseRef = firebase.database().ref("Users");
    
    if (email.value != "" && pass.value != "" && cpass.value != "")
    {
      if (pass.value == cpass.value)
      {
        firebaseRef.push(
        {
          email: document.getElementById("email_field").value,
          password: document.getElementById("password_field").value,
          nickname: document.getElementById("nickname_field").value
        });
      
        const promise = auth.createUserWithEmailAndPassword(email.value, pass.value);
        promise.catch(e => alert(e.message));

        alert("Welcome, " + nickname_field.value + "!");
        window.location.href = 'login.html';
      }

      else  
        window.alert("Passwords do not match!");
    }

    else
      window.alert("Signup is incomplete!");
  }

    function login()
    {
      var email = document.getElementById("email_field");
      var pass = document.getElementById("password_field");
      
      const promise = auth.signInWithEmailAndPassword(email_field.value, password_field.value);
      promise.catch(e => alert(e.message));
  
      alert("Successfully logged in"); 
      window.location.href = 'home-page.html';
    }

    function signOut()
    {
      auth.signOut();
      alert("Signed Out");
    }

    function continueGuest()
    {
      alert("Welcome, " + nickname_field.value + "!!"); 
      window.location.href = 'home-page.html';
    }