let num = parseInt(prompt("Enter a number to print its multiplication table:"));

console.log("Multiplication Table of", num);
for (let i = 1; i <= 10; i++) {
    console.log(`${num} x ${i} = ${num * i}`);
}