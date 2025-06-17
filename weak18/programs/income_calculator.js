let income = parseFloat(prompt("Enter your annual income:"));
let tax = 0;

if (income <= 250000) {
    tax = 0;
} else if (income <= 500000) {
    tax = (income - 250000) * 0.05;
} else if (income <= 1000000) {
    tax = (250000 * 0.05) + (income - 500000) * 0.2;
} else {
    tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3;
}

console.log("Calculated Tax:", tax);
