let percentage = parseFloat(prompt("Enter your total percentage:"));

if (percentage >= 90) {
    console.log("Grade: A+");
} else if (percentage >= 80) {
    console.log("Grade: A");
} else if (percentage >= 70) {
    console.log("Grade: B");
} else if (percentage >= 60) {
    console.log("Grade: C");
} else if (percentage >= 50) {
    console.log("Grade: D");
} else {
    console.log("Grade: F (Fail)");
}
