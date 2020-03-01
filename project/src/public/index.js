const email = document.getElementById("email_field");
const pass = document.getElementById("password_field");
const cpass = document.getElementById("cpassword");
const nickname = document.getElementById("nickname_field");

async function createAccount()
{ 
  if (email.value != "" && nickname.value != "" && pass.value != "" && cpass.value != "")
  {
    if (isAlphanumeric(nickname)) 
    {
      if (pass.value == cpass.value)
      {
        if(await authenticate())
        {
          pushToDatabase(); 
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
        if(retrieve("nickname"))
          window.location.href = 'home-page.html';
        else 
          window.alert("Error connecting to databse. Please try again later."); 
      }
    }); 
  }  
  else 
    window.alert("Email and password required!");
}

async function retrieve(data)
{
  var userId = firebase.auth().currentUser.uid; 

  var firebaseRef = firebase.database().ref("/Users/" + userId + "/" + data);

  await firebaseRef.on('value', function(snapshot) {
    if (snapshot.val())
    {
      window.alert("Successfully logged in " + snapshot.val() + "!"); 
      return true; 
    }
    else
      return false;
  }); 
}

function signOut() 
{
  auth.signOut();
  alert("Signed out!");
  window.location.href = 'index.html';
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

async function authenticate()
{
  var flag; 
  await auth.createUserWithEmailAndPassword(email.value, pass.value).then(function(user) {
    flag = true; 
  })
  .catch(function(error) {
    window.alert(error.message); 
    flag = false; 
  });

  return flag; 
}

function pushToDatabase() 
{
  var userId = firebase.auth().currentUser.uid;
  var firebaseRef = firebase.database().ref("/Users/" + userId);

  firebaseRef.set(
    {
      email: email.value,
      password: pass.value,
      nickname: nickname.value
    });
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

// listen for auth status changes
firebase.auth().onAuthStateChanged(user => {
  if (user)
  {
    console.log('logged in as ' + user.email);
  }
    
  else
    console.log('no user logged in');
})