const fs = require('node:fs');
const { argv, exit } = require('node:process');

if (argv.length != 3) {
    console.log("Please define one input file!");
    exit();
}

// Permutation function Snatched from SO:
// https://stackoverflow.com/questions/9960908/permutations-in-javascript?page=1&tab=scoredesc#tab-top
function* permute(permutation) {
    var length = permutation.length,
        c = Array(length).fill(0),
        i = 1, k, p;

    yield permutation.slice();
    while (i < length) {
        if (c[i] < i) {
            k = i % 2 && c[i];
            p = permutation[i];
            permutation[i] = permutation[k];
            permutation[k] = p;
            ++c[i];
            i = 1;
            yield permutation.slice();
        } else {
            c[i] = 0;
            ++i;
        }
    }
}

const towns = new Set()
const distances = {};
fs.readFile(argv[2], 'utf8', (err, data) => {
    const lines = data.split("\n");
    for (const line of lines) {
        const match = /^(\w+) to (\w+) = (\d+)$/.exec(line)
        if (match) {
            const [_, src, dst, dist] = match;
            towns.add(src);
            towns.add(dst);
            distances[`${src},${dst}`] = Number(dist);
            distances[`${dst},${src}`] = Number(dist);
        }
    }

    let shortest = Infinity;
    let longest = 0;
    for (var perm of permute([...towns])){
        let path_len = 0;
        for (let i = 0; i < perm.length - 1; i++) {
            const src = perm[i];
            const dst = perm[i+1];
            path_len += distances[`${src},${dst}`];
        }
        shortest = Math.min(shortest, path_len);
        longest = Math.max(longest, path_len);
    };

    console.log(`Part1 (shortest): ${shortest}`);
    console.log(`Part2 (longest):  ${longest}`);
});