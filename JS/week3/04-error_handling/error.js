function myFunction() {
    const message = document.getElementById("p01");
    message.innerHTML = "";
    let x = document.getElementById("demo").value;
    try {
      if(x.trim() == "") throw "is empty";
      if(isNaN(x)) throw "is not a number";
      x = Number(x);
      if(x > 10) throw "is too high";
      if(x < 5) throw "is too low";
      if(x >= 5 && x <= 10 ) throw "it's between the range";
    }
    catch(err) {
      message.innerHTML = "Error: " + err + ".";
    }
    finally {
      document.getElementById("demo").value = "";
    }
  }
  le.log("Error: " + error)
// }