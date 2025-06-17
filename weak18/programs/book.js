let library = [
    { bookName: "Atomic Habits", author: "James Clear", readingStatus: true },
    { bookName: "1984", author: "George Orwell", readingStatus: false },
    { bookName: "The Alchemist", author: "Paulo Coelho", readingStatus: true }
];

for (let book of library) {
    console.log(`Book: "${book.bookName}", Author: ${book.author}, Reading Status: ${book.readingStatus ? "Completed" : "Not read yet"}`);
}
