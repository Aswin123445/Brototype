class Matrix {
    constructor(rows, cols) {
        this.rows = rows;
        this.cols = cols;
        this.data = Array.from({ length: rows }, () => Array(cols).fill(0));
    }

    setValues(values) {
        this.data = values;
    }

    display() {
        console.log("Matrix values:");
        for (let i = 0; i < this.rows; i++) {
            console.log(this.data[i].join(' '));
        }
    }
}

// Example usage:
let matrix = new Matrix(2, 2);
matrix.setValues([[1, 2], [3, 4]]);
matrix.display();
