/** 흙길 보수하기
 * https://www.acmicpc.net/problem/1911 */
let input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .split("\n")
  .map((a) => a.split(" ").map((a) => +a));
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n').map((a) => a.split(" ").map((a) => +a));
const [N, L] = input[0];
const puddle = input.slice(1).sort((a, b) => a[0] - b[0]);
let cur = 0;
let cnt = 0;
for (const [start, end] of puddle) {
  if (end <= cur) continue;
  if (start > cur) cur = start;
  const temp =
    (end - cur) % L > 0 ? ~~((end - cur) / L) + 1 : ~~((end - cur) / L);
  cnt += temp;
  cur += temp * L;
}
console.log(cnt);
