window.addEventListener('load', function () {
    // FirebaseUI config.
    var uiConfig = {
      signInSuccessUrl: '/SignedIn',
      signInOptions: [
       
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
        firebase.auth.EmailAuthProvider.PROVIDER_ID,
      ],
      
    };
  
    firebase.auth().onAuthStateChanged(function (user) {
      if (!user) {
        // User is signed out.
        // Initialize the FirebaseUI Widget using Firebase.
        var ui = new firebaseui.auth.AuthUI(firebase.auth());
        // Show the Firebase login button.
        ui.start('#firebaseui-auth-container', uiConfig);
      }
    }, function (error) {
      console.log(error);
      alert('Unable to log in: ' + error)
    });
  });
