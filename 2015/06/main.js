const fs = require('node:fs');

function get_light_array(size, init_val=0) {
    const arr = new Array(size)
    for (var i = 0; i < size; i++) {
        const row = new Array(size);
        for (var j = 0; j < size; j++) {
            row[j] = init_val;
        }
        arr[i] = row;
    }
    return arr;
}

function calculate_lights(lights) {
    let count = 0;
    for (const row of lights) {
        for (const val of row) {
            count += val;
        }
    }
    return count;
}

function process_operations(ops, lights1, lights2) {
    for (const op of ops) {
        // Not checking any potential runtime issue :D
        const rd = op.match(/^([\w ]+) (\d+),(\d+) through (\d+),(\d+)$/);
        const [o, x1, y1, x2, y2] = [rd[1], Number(rd[2]), Number(rd[3]), Number(rd[4]), Number(rd[5])];

        for (let y = y1; y <= y2; y++) {
            // Interestingly this also add speed up in already very fast execution
            // from ~0.180s to ~0.130s ~~ +27% performance gain
            row1 = lights1[y]
            row2 = lights2[y]
            for (let x = x1; x <= x2; x++) {
                if (o === "turn on") {
                    // lights1[y][x] = 1;
                    // lights2[y][x]++;
                    row1[x] = 1;
                    row2[x]++;
                }
                else if (o === "turn off") {
                    // lights1[y][x] = 0;
                    // lights2[y][x] -= lights2[y][x] > 0 ? 1 : 0;
                    row1[x] = 0;
                    row2[x] -= row2[x] > 0 ? 1 : 0;
                }
                else {
                    // lights1[y][x] = lights1[y][x] ? 0 : 1;
                    // lights2[y][x] += 2;
                    row1[x] = row1[x] ? 0 : 1;
                    row2[x] += 2;
                }
            }
        }
    }
}

fs.readFile('input.txt', 'utf8', (err, data) => {
    const ops = data.split("\n");

    const lights1 = get_light_array(1000);
    const lights2 = get_light_array(1000);

    process_operations(ops, lights1, lights2);

    console.log(`Part1: ${calculate_lights(lights1)}`);
    console.log(`Part2: ${calculate_lights(lights2)}`);
});