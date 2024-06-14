function check(n) {
    if (!(n >= -500 && n <= 500)) {
      throw new RangeError("The argument must be between -500 and 500.");
    }
  };
  
check(5000);