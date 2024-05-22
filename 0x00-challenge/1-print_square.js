#!/usr/bin/env node
/*
    Print a square with the character #
    
    The size of the square must be the first argument 
    of the program.
*/

const size = parseInt(process.argv[2]);

if (isNaN(size) || size <= 0) {
    console.error("Invalid size. Please provide a positive integer as size.");
    console.error("Usage: ./1-print_square.js <size>");
    console.error("Example: ./1-print_square.js 8");
    process.exit(1);
}

for (let i = 0; i < size; i++) {
    console.log('#'.repeat(size));
}
