const fs = require('node:fs');
fs.readFile('input.txt', 'utf8', (err, data) => {
    const lines = data.split("\n");

    let total_paper_area = 0;
    let total_ribbon_len = 0;

    for (const line of lines) {
        const [l,w,h] = line.split("x");
        total_paper_area += 2*l*w + 2*w*h + 2*h*l + Math.min(l*w, w*h, h*l);
        
        const lwh = [l,w,h].toSorted((a,b) => a-b);
        total_ribbon_len += 2*lwh[0] + 2*lwh[1] + l*w*h;
    }

    console.log(`Part1: ${total_paper_area}`);
    console.log(`Part2: ${total_ribbon_len}`);
});