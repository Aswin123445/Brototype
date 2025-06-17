function myFilter(myArray, callback) {
    let result = [];
    for (let num of myArray) {
        if (callback(num)) {
            result.push(num);
        }
    }
    return result;
}

// Callback: checks if sum of digits is even
function isSumEven(number) {
    let sum = 0;
    let n = Math.abs(number);
    while (n > 0) {
        sum += n % 10;
        n = Math.floor(n / 10);
    }
    return sum % 2 === 0;
}

// Example usage
let numbers = [12, 35, 44, 71, 28];
let filtered = myFilter(numbers, isSumEven);
console.log("Filtered array (sum of digits is even):", filtered);
