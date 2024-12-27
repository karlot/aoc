const fs = require('node:fs');
fs.readFile('input.txt', 'utf8', (err, data) => {
    let floors = 0;
    let bii = 0;
    for (let i = 0; i < data.length; i++) {
        if (data[i] === "(" ) floors++;
        if (data[i] === ")" ) floors--;
        if (floors < 0) { if (!bii) bii = i + 1 }
    }
    console.log(`Part1: ${floors}`);
    console.log(`Part2: ${bii}`);
});