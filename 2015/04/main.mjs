import { readFile } from "node:fs";
import { createHash } from "node:crypto";

function find_number(key, zeroes) {
    const search_target = "0".repeat(zeroes);
    let number = 0;
    while (true) {
        let result = createHash("md5").update(`${key}${number}`).digest("hex")
        if (result.startsWith(search_target)) return number;
        number++;
    }
}

readFile('input.txt', 'utf8', (err, data) => {
    const key = data.trim()
    console.log(`Part1: ${find_number(key, 5)}`);
    console.log(`Part2: ${find_number(key, 6)}`);
});