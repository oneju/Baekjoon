/* 숫자 카드 */
/* https://www.acmicpc.net/problem/10815 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const s_arr = {};
input[1].split(" ").map((a) => (s_arr[a] = 1));
const f_arr = input[3].split(" ").map((a) => +a);
const answer = [];

for (const num of f_arr) {
  if (s_arr[num]) answer.push(1);
  else answer.push(0);
}
console.log(answer.join(" "));
