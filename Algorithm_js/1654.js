/**랜선 자르기
 * https://www.acmicpc.net/problem/1654 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [K, N] = input[0].split(" ");
const lines = input.slice(1).map(Number);
lines.sort((a, b) => b - a);
let [start, end] = [1, lines[0]];
while (start <= end) {
  const len = parseInt((start + end) / 2);
  let cnt = 0;
  for (const line of lines) cnt += ~~(line / len);
  if (cnt < N) end = len - 1;
  else start = len + 1;
}
console.log(end);
