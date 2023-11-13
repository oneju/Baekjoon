/**로프
 * https://www.acmicpc.net/problem/2217 */
const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .split("\n")
  .map(Number);
// const input = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(Number);
const n = input[0];
const ropes = input.slice(1).sort((a, b) => b - a);

let maxi = 0;
for (let i = 0; i < n; i++) {
  maxi = Math.max(maxi, ropes[i] * (i + 1));
}
console.log(maxi);
