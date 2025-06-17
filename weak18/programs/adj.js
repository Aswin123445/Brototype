let arr = [2, 3, 4, 5];
let result = [];

for (let i = 0; i < arr.length - 1; i++) {
    result.push(arr[i] * arr[i + 1]);
}

console.log("Original Array:", arr);
console.log("Multiplied Adjacent Array:", result);
