let my_string = "JavaScript";

try {
    let reversed = my_string.split("").reverse().join("");
    console.log("Reversed String:", reversed);
} catch (error) {
    console.log("Error:", error.message);
} finally {
    console.log("Type of my_string:", typeof my_string);
}
