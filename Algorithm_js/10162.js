/* 전자레인지
https://www.acmicpc.net/problem/10162 */
let input = require("fs").readFileSync("example.txt").toString();
// let input = require('fs').readFileSync('/dev/stdin').toString();
const A = parseInt(input / 300);
input %= 300;
const B = parseInt(input / 60);
input %= 60;
const C = parseInt(input / 10);
if (input % 10 > 0) console.log(-1);
else console.log(A, B, C);
