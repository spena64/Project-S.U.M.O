const email = document.getElementById("email_field");
const pass = document.getElementById("password_field");
const cpass = document.getElementById("cpassword");
const nickname = document.getElementById("nickname_field");

async function createAccount()
{ 
  var firebaseRef = firebase.database().ref("Users");
  
  if (email.value != "" && pass.value != "" && cpass.value != "")
  {
    if (pass.value == cpass.value)
    {
      await auth.createUserWithEmailAndPassword(email.value, pass.value).catch(e => alert(e.message));

      firebaseRef.push(
      {
        email: email.value,
        password: pass.value,
        nickname: nickname.value
      });

      alert("Welcome, " + nickname.value + "!");

      window.location.href = 'login.html'; 
    }
      else  
        window.alert("Passwords do not match!");
    }
    else
      window.alert("Signup is incomplete!");
  }

  async function login()
  {   
    if (email.value != "" && pass.value != "")
    {
      await auth.signInWithEmailAndPassword(email.value, pass.value).catch(e => alert(e.message));

      firebase.auth().onAuthStateChanged(function(currentUser) 
      {
        if (currentUser && !currentUser.isAnonymous)
        {
          console.log(currentUser); 
          // TODO: figure out why nickname shows up as undefined 
          alert("Successfully logged in " + currentUser.email + "!"); 
          window.location.href = 'home-page.html';
        }
      }); 
    }  
    else 
      window.alert("Email and password required!");
  }

  function signOut()
  {
    auth.signOut();
    alert("Signed out!");
  }

  function continueGuest()
  {
    if (nickname.value != "") {
      alert("Welcome, " + nickname.value + "!"); 
      window.location.href = 'home-page.html';
    }
    else
      window.alert("Please enter a nickname!"); 
  }

  // firebase.auth().onAuthStateChanged(firebaseUser => {
  //   if(firebaseUser)
  //     console.log(firebaseUser);
  //   else
  //     console.log("not logged in");
  // });