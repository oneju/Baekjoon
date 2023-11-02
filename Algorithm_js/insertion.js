/** 비트 연습 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
const [N, M, i, j] = input;
const allOnes = ~0;
const left = allOnes << (j + 1);
const right = ~(1 << (i + 1));
const mask = left | right;
const newN = N & mask;
const newM = M << i;
console.log((newN | newM).toString(2));
