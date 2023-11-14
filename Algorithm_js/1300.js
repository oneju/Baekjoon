/**K번째 수
 * https://www.acmicpc.net/problem/1300 */
let [N, K] = require("fs")
  .readFileSync("example.txt")
  .toString()
  .split("\n")
  .map(Number);
// let [N,K] = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(Number);
let left = 1;
let right = K;
while (left < right) {
  const mid = ~~((left + right) / 2);
  let cnt = 0;
  for (let i = 1; i <= N; i++) cnt += mid / i > N ? N : ~~(mid / i);
  if (cnt < K) left = mid + 1;
  else right = mid;
}
console.log(right);
