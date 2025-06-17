let str = prompt("Enter a string:");

// Convert to lowercase and remove non-alphanumeric characters (optional cleanup)
let cleanStr = str.toLowerCase().replace(/[^a-z0-9]/g, '');
let reversedStr = cleanStr.split('').reverse().join('');

if (cleanStr === reversedStr) {
    console.log(`${str} is a Palindrome.`);
} else {
    console.log(`${str} is NOT a Palindrome.`);
}
