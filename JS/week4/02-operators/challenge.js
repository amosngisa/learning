const numbers = [1,2,3,4,5];

const getMinMaxSum = (numbers) => {
    //destructuring
    //The numbers array is destructured. "first" is assigned the first element of the array, and rest is assigned the rest of the array elements.
    // If numbers = [1, 2, 3, 4, 5], then first = 1 and rest = [2, 3, 4, 5]
    const [first, ...rest] = numbers;
   

    const {min,max,sum} = rest.reduce((acc,num) =>{
        return{
            min: Math.min(acc.min, num),
            max: Math.max(acc.max, num),
            sum: acc.sum + num
        };

    }, {min: first, max: first, sum: first});

    //The reduce function is used to iterate over the rest array, updating the acc (accumulator) object 
    //which keeps track of the current minimum (min), maximum (max), and sum (sum) of the array elements.
    //For each num in rest, Math.min and Math.max functions update the min and max values respectively, and the sum is incremented by num.
    
    return{min, max, sum};

    //The function returns an object with the computed min, max, and sum values

};

//let result = getMinMaxSum(numbers)

console.log(getMinMaxSum(numbers));//{min: 1, max: 5, sum: 15}

