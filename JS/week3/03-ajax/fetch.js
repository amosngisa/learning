async function myFunction(){

let user = {
    firstName: "Tedy",
    lastName: "Oloo",
    age: 20
};

// let response = await fetch('http://dummyjson.com/users/add', {
//     method: 'POST',
//     headers: {
//         'Content-Type': 'application/json'
//     },
//     body: JSON.stringify(user)
// });
let response = await fetch('https://jsonplaceholder.typicode.com/todos/1')

let result = await response.json();

console.log(result.message)

};

myFunction();

























//getText("ajax.txt");

// // fetch (file)
// // .then(x => x.text())
// // .then(y => document.getElementById("demo").innerHTML = y);

// async function getText(file){
//     let myObject = await fetch(file);
//     let mytext = await myObject.text();
//     document.getElementById("demo").innerHTML = mytext;
// }


//Async - makes a function return a Promise
//Await - makes a function wait for a Promise

// async function myyFunction(){
//     return "Heloo Class";
// }

// function myyFunction(){
//     return Promise.resolve("Hello")
// }


//Promise.resolve = async

//How to use a promise

// function myDisplayer(some) {
//     document.getElementById("demo").innerHTML = some;
//   }

// async function myyFunction(){
//     return "Hello";
// }

// myyFunction().then(
// function(value){
//     myDisplayer(value)
// }
// )

// async function myDisplayer(){

//     //promise
//     let myPromise = new Promise(function(resolve, reject){
//         resolve("Hi class 24");
//     });

//     //used await
//     document.getElementById("demo").innerHTML = await myPromise;
// }

// myDisplayer();