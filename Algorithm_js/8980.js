/**택배
 * https://www.acmicpc.net/problem/8980 */
let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [towns, limit] = input[0].split(" ").map((num) => +num);
const boxes = input
  .slice(2)
  .map((a) => a.split(" ").map((a) => +a))
  .sort((a, b) => (a[1] === b[1] ? a[0] - b[0] : a[1] - b[1]));
let answer = 0;
const truck = Array(towns + 1).fill(0);

for (const [s, e, w] of boxes) {
  const temp = truck.slice(s, e);
  const max = Math.max(...temp);
  const min = limit - max > w ? w : limit - max;
  if (min > 0) {
    for (let i = s; i < e; i++) truck[i] += min;
    answer += min;
  }
}
console.log(answer);
