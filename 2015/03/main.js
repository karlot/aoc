const fs = require('node:fs');
fs.readFile('input.txt', 'utf8', (err, data) => {
    const lines = data.split("\n");

    let [x, y]   = [0, 0];  // Part 1
    let [sx, sy] = [0, 0];  // Part 2
    let [rx, ry] = [0, 0];  // Part 2

    const visited_p1 = new Set(["0,0"]);  // Part 1, SET Include starting position
    const visited_p2 = new Set(["0,0"]);  // Part 2, SET Include starting position

    for (const line of lines) {
        for (let i = 0; i < line.length; i++) {
            // Part 1
            if (line[i] === ">" ) x++;
            if (line[i] === "<" ) x--;
            if (line[i] === "^" ) y++;
            if (line[i] === "v" ) y--;
            if (! visited_p1.has(`${x},${y}`)) visited_p1.add(`${x},${y}`);
            
            // Part 2
            if (i % 2 == 0) {
                if (line[i] === ">" ) sx++;
                if (line[i] === "<" ) sx--;
                if (line[i] === "^" ) sy++;
                if (line[i] === "v" ) sy--;
                if (! visited_p2.has(`${sx},${sy}`)) visited_p2.add(`${sx},${sy}`);
            }
            else {
                if (line[i] === ">" ) rx++;
                if (line[i] === "<" ) rx--;
                if (line[i] === "^" ) ry++;
                if (line[i] === "v" ) ry--;
                if (! visited_p2.has(`${rx},${ry}`)) visited_p2.add(`${rx},${ry}`);
            }
        }
    }

    console.log(`Part1: ${visited_p1.size}`);
    console.log(`Part2: ${visited_p2.size}`);
});