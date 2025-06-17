let written = parseFloat(prompt("Enter Written Test Marks:"));     // 70%
let lab = parseFloat(prompt("Enter Lab Exam Marks:"));             // 20%
let assignment = parseFloat(prompt("Enter Assignment Marks:"));    // 10%

let weightedAverage = (written * 0.7) + (lab * 0.2) + (assignment * 0.1);
console.log("Weighted Average:", weightedAverage.toFixed(2));
