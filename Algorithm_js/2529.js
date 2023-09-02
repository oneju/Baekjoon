/**부등호
 * https://www.acmicpc.net/problem/2529 */
let [n, A] = require("fs").readFileSync("example.txt").toString().split("\n");
// let [n,A] = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const visited = Array(10).fill(0);
A = A.split(" ");
let max = "",
  min = "";
const check = (i, j, c) => {
  if (c === "<") return i < j;
  else return i > j;
};
const greedy = (d, num) => {
  if (d === +n + 1) {
    if (String(min).length === 0) min = num;
    else max = num;
    return;
  }
  for (let i = 0; i < 10; i++) {
    if (!visited[i]) {
      if (d === 0 || check(num[num.length - 1], i, A[d - 1])) {
        visited[i] = 1;
        greedy(d + 1, num + String(i));
        visited[i] = 0;
      }
    }
  }
};
greedy(0, "");
console.log(max);
console.log(min);
