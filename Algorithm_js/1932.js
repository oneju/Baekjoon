/* 정수 삼각형
 * https://www.acmicpc.net/problem/1932 */
let [n, ...input] = require("fs")
  .readFileSync("example.txt")
  .toString()
  .split("\n");
// let [n,...input] = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const triangle = input.map((n) => n.split(" ").map((num) => +num));
for (let i = 1; i < n; i++) {
  for (let j = 0; j < triangle[i].length; j++) {
    if (j == 0) triangle[i][j] += triangle[i - 1][j];
    else if (j == triangle[i].length - 1)
      triangle[i][j] += triangle[i - 1][j - 1];
    else triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j]);
  }
}
console.log(Math.max(...triangle[n - 1]));
