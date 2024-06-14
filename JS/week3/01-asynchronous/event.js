
//Producing code
function step1(init, callback){
    const result = init + 1;
    callback(result);
}

//Producing code
function step2(init){
    return init + 2;
}

//Producing code
function step3(init){
    return init + 3;
}

//consuming code
function doOperation(){
    let result = 0;
    result = step1(result);
    result = step2(result);
    result = step3(result);

    console.log(`result: ${result}`)
}

doOperation();