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

    if (auth.currentUser)
    {
      let userNickname = await retrieve("nickname"); 
      if(userNickname) 
      {
        window.alert("Successfully logged in " + userNickname + "!");
        window.location.href = 'home-page.html';
      }
      else 
        window.alert("Error connecting to databse. Please try again later."); 
    }
  }  
  else 
    window.alert("Email and password required!");
}

async function retrieve(data)
{
  var userId = firebase.auth().currentUser.uid; 

  var firebaseRef = firebase.database().ref("/Users/" + userId + "/" + data);
   
  return new Promise(function(resolve, reject) {
    firebaseRef.once('value').then(function(snapshot) {
      if (snapshot.val())
      {
        resolve(snapshot.val());
      }
    }); 
  });
}

async function showStats()
{
  if (auth.currentUser)
    {
      let wins = await retrieve("wins");
      let losses = await retrieve("losses"); 
        window.alert("Total Wins: " + wins + "\n" + "Total Losses: " + losses);
    }
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
      nickname: nickname.value,
      wins: "0",
      losses: "0"
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
    if (window.location.href == 'https://project-sumo-e6f87.firebaseapp.com/')
    {
      console.log('logged in as ' + user.email);
      window.location.href = 'home-page.html';
    }
    else
    {
      console.log('logged in as ' + user.email);
      var userNav = document.getElementById("nav-bar-user"); 
      var guestNav = document.getElementById("nav-bar-guest"); 
      if (user.email != null) {
        userNav.style.display = 'block'; 
        guestNav.style.display = 'none'; 
      }
      else {
        userNav.style.display = 'none'; 
        guestNav.style.display = 'block';
      }
    }
  }
  else
  {
    console.log('no user logged in');
    var userNav = document.getElementById("nav-bar-user"); 
    var guestNav = document.getElementById("nav-bar-guest"); 
    userNav.style.display = 'none'; 
    guestNav.style.display = 'block';
  }
})