//syntax
// const {variable1, variable2} = object;

//Example
// const person = {name: 'Shawn Paul', age: 21}; //object

// const {name, age} = person; //variables

// console.log(name); //''Shawn Paul'

// console.log(age); // 21

//steps for object destructing

//1. assigning object value to exixt variable
// const superHero = {
//     name: 'Spiderman',
//     power: 'Spider sense',
//     color: 'red'
// };

// const {name, power} = superHero; //variable
// console.log("Name: ",name);
// console.log("Power: ",power);

//2. assigning new variable names
//destruct the object into variable

// const {name: n, power: p, color: c} = superHero; //variable

// console.log("Name: ", n); //spidername

//3. Nested object destructuring
const superHero = {
    "name": "Spiderman",
    "power": "Spider sense",
    "character":{
        "realName": "Tom Holland",
        "citizenship": "British",
        "apprearances":{
            "movie": "captain america civil war",
            "releaseDate": "6 May 2016"
        }
    }
};

const {character:{realName}} = superHero;//variable

//console.log("movie: ", movie );//movie
//console.log("citizenship: ", citizenship );//citizenship
//console.log("releaseDate: ", releaseDate );//releaseDate
console.log("realName: ", realName );//realName