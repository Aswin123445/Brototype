let array1 = [1, 2, 3];
let array2 = [4, 5, 6];

console.log("Before swapping:");
console.log("Array 1:", array1);
console.log("Array 2:", array2);

// Swapping elements one by one
for (let i = 0; i < array1.length && i < array2.length; i++) {
    let temp = array1[i];
    array1[i] = array2[i];
    array2[i] = temp;
}

console.log("After swapping:");
console.log("Array 1:", array1);
console.log("Array 2:", array2);
