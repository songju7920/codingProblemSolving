const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    str = line;
}).on('close', function () {
    console.log(str.split(' ').reduce((a, b) => a + b));
});