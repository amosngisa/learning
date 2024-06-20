//example creates an object person

//Naming convention
//1. Should start with a capital letter
//2. should be called with "new" operator
function Person(firstName, lastName) {
   this.firstName = firstName;
   this.lastName = lastName;

//created a method "getFullName()"
   this.getFullName = () =>{
    return "Hi " +this.firstName + " "+ this.lastName;//string literal
    //"This movie avengers was released on 2017"
   }
};

let person = new Person('John', 'Doe');



console.log(person.getFullName());
