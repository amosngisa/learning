// //Callback
// setTimeout(function() { myFunction("I love You !!!"); }, 3000);

// function myFunction(value) {
//   document.getElementById("demo").innerHTML = value;
// }


//Promise
// let myPromise = new Promise(function(resolve, reject){

//    setTimeout(function() { resolve("I love You !!!"); }, 3000);

// });

// myPromise.then(function(value){
//    document.getElementById("demo").innerHTML = value;

// });

//Callback
// function myDisplayer(some) {
//   document.getElementById("demo").innerHTML = some;
// }

// function getFile(myCallback) {
//    let req = new XMLHttpRequest();
//    req.open('GET', "../../week2/04-Todo/index.html");
//    req.onload = function() {
//      if (req.status == 200) {
//        myCallback(req.responseText);
//      } else {
//        myCallback("Error: " + req.status);
//      }
//    }
//    req.send();
//  }
 
//  getFile(myDisplayer);

 //promise

 function myDisplayer(some) {
  document.getElementById("demo").innerHTML = some;
}

 let myPromise = new Promise(function(resolve, reject) {
  let req = new XMLHttpRequest();
  req.open('GET', "../../week2/04-Todo/index.html");
  req.onload = function() {
    if (req.status == 200) {
      resolve(req.response);
    } else {
      reject("File not Found");
    }
  };
  req.send();
});

myPromise.then(
  function(value) {myDisplayer(value);},
  function(error) {myDisplayer(error);}
);