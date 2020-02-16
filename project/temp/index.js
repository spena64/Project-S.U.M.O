  
  function createAccount()
  { 
    var email = document.getElementById("email_field");
    var pass = document.getElementById("password_field");
    var firebaseRef = firebase.database().ref("Users");
    
    const promise = auth.createUserWithEmailAndPassword(email.value, pass.value);
    promise.catch(e => alert(e.message));

    firebaseRef.push(
    {
      email: document.getElementById("email_field").value,
      password: document.getElementById("password_field").value,
      nickname: document.getElementById("nickname_field").value
    });

    alert("Welcome, " + nickname_field.value + "!");
    window.location.href = 'login.html';
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