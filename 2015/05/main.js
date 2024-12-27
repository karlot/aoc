const fs = require('node:fs');

// Part1 checkers
const r1 = /(?:[aeiou].*){3,}/; // Minimum 3 vowels (a, e, i, o, u)
const r2 = /(\w)\1+/;           // Contains pairs of characters like "aa" or "xx"
const r3 = /ab|cd|pq|xy/;       // Contains forbidden words (ab, cd, pq, or xy)

// Part2 checkers
const r4 = /(.{2}).*?\1/        // Pair of chars that appear again, like "abab" or "abcab"
const r5 = /(.)(.)\1/           // Matches repeating letter after once char, like "xyx" or "efe"


fs.readFile('input.txt', 'utf8', (err, data) => {
    const list = data.split("\n");

    let nice1 = 0;
    for (const l of list) { if (r1.test(l) && r2.test(l) && !r3.test(l)) nice1++; }
    console.log(`Part1: ${nice1}`);

    let nice2 = 0;
    for (const l of list) { if (r4.test(l) && r5.test(l)) nice2++; }
    console.log(`Part2: ${nice2}`);
});