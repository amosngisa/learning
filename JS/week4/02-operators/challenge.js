
const getMinMaxSum = (numbers) => {
    //destructuring
    const [first, ...rest] = [numbers];
   
    const {min,max,sum} = rest.reduce((acc,num) =>{
        return{
            min: Math.min(acc.min, num),
            max: Math.max(acc.max, num),
            sum: acc.sum + num
        };

    }, {min: first, max: first, sum: first});

    return{min, max, sum};


};

const numbers = [1,2,3,4,5];

let result = getMinMaxSum(numbers)

console.log(result);//{min: 1, max: 5, sum: 15}

