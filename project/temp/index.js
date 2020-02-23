const email = document.getElementById("email_field");
const pass = document.getElementById("password_field");
const cpass = document.getElementById("cpassword");
const nickname = document.getElementById("nickname_field");

async function createAccount()
{ 
  var firebaseRef = firebase.database().ref("Users");
  
  if (email.value != "" && nickname.value != "" && pass.value != "" && cpass.value != "")
  {
    if (isAlphanumeric(nickname)) 
    {
      if (pass.value == cpass.value)
      {
        await auth.createUserWithEmailAndPassword(email.value, pass.value).catch(function(error) {
          window.alert(error.message); 
          var flag = false; 
        });
        
        if(flag == false)
        {
          firebaseRef.push(
          {
            email: email.value,
            password: pass.value,
            nickname: nickname.value
          });

          alert("Welcome, " + nickname.value + "!");

          window.location.href = 'login.html'; 
        }
      }
      else  
        window.alert("Passwords do not match!");
    }
    else 
      window.alert("Nickname must be alphanumeric!");
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

  async function continueGuest()
  {
    if (nickname.value != "") 
    {
      if (isAlphanumeric(nickname)) 
      {
        await auth.signInAnonymously();
        firebase.auth().onAuthStateChanged(firebaseUser => {
        console.log(firebaseUser);
        });
      
        alert("Welcome, " + nickname.value + "!"); 
        window.location.href = 'home-page.html';
      }
      else 
        window.alert("Nickname must be alphanumeric!");
    }
    else
      window.alert("Please enter a nickname!"); 
  }

  function isAlphanumeric(str) 
  {
    var acceptableChars = /^[0-9a-zA-Z]+$/; 
    if(str.value.match(acceptableChars))
    {
      return true;
    }
    return false; 
  }