
const email = document.getElementById("email_field");
const pass = document.getElementById("password_field");
const cpass = document.getElementById("cpassword");
const nickname = document.getElementById("nickname_field");

function createAccount()
{ 
  var firebaseRef = firebase.database().ref("Users");
  
  if (email.value != "" && pass.value != "" && cpass.value != "")
  {
    

    if (pass.value == cpass.value)
    {
      var promise = auth.createUserWithEmailAndPassword(email.value, pass.value);
      promise.catch(e => alert(e.message));

      firebaseRef.push(
      {
        email: email.value,
        password: pass.value,
        nickname: nickname.value
      });

      alert("Welcome, " + nickname.value + "!");
      // NEED TO MAKE IT SO THAT THE BUTTON WILL GO TO LOGIN PAGE AFTERWARDS WILE ALSO SAVING IN THE AUTHENTICATION TOKEN
      // set 3000 milliseconds before redirecting 
      setTimeout(redirect, 100);
    }
      else  
        window.alert("Passwords do not match!");
    }
    else
      window.alert("Signup is incomplete!");
  }

  function redirect() {
    window.location.href = 'login.html';
  }

  function login()
  {   
    const promise = auth.signInWithEmailAndPassword(email.value, pass.value);
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
    alert("Welcome, " + nickname.value + "!!"); 
    window.location.href = 'home-page.html';
  }

  // firebase.auth().onAuthStateChanged(firebaseUser => {
  //   if(firebaseUser)
  //     console.log(firebaseUser);
  //   else
  //     console.log("not logged in");
  // });