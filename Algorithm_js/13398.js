/**연속합 2
 * https://www.acmicpc.net/problem/13398 */
let [n, arr] = require("fs").readFileSync("example.txt").toString().split("\n");
// let [n,arr] = require('fs').readFileSync('/dev/stdin').toString().split('\n');
arr = arr.split(" ").map((num) => +num);

const lst = Array.from(Array(+n), () => Array(2).fill(0));
lst[0][0] = lst[0][1] = arr[0];
for (let i = 1; i < n; i++) {
  lst[i][0] = Math.max(lst[i - 1][0] + arr[i], arr[i]);
  lst[i][1] = Math.max(lst[i - 1][0], lst[i - 1][1] + arr[i]);
}
const num = Math.max(...lst.flat());
console.log(num);
