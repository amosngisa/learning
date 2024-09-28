function linearSearch(arr, target){
    for(let i = 0; i < arr.length; i++){
        if (arr[i] === target){
            return i;
        }
    }
    return -1;
}

let arr = [2, 11, 5, 8, 21];
let target = 2;

console.log(linearSearch(arr, target));


// Pseudocode
function linearSearch(arr, target):
    for each element in arr:
        if element == target:
            return index
    return -1
