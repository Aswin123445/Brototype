let principal = parseFloat(prompt("Enter principal amount:"));
let rate = parseFloat(prompt("Enter rate of interest (%):"));
let time = parseFloat(prompt("Enter time in years:"));
let simpleInterest = (principal * rate * time) / 100;
console.log("Simple Interest is:", simpleInterest);
