function Car(name, mileage, max_speed) {
    this.name = name;
    this.mileage = mileage;
    this.max_speed = max_speed;
}

// Example usage:
let car1 = new Car("Toyota Fortuner", 12, 180);
let car2 = new Car("Honda City", 17, 160);

console.log(car1); // Output: Car { name: 'Toyota Fortuner', mileage: 12, max_speed: 180 }
console.log(car2); // Output: Car { name: 'Honda City', mileage: 17, max_speed: 160 }
