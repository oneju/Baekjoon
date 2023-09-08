/**퇴사
 * https://www.acmicpc.net/problem/14501 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const dday = +input[0];
const arr = input.slice(1, dday + 1);
const days = Array(dday + 1).fill(0);
for (let i = 0; i < dday; i++) {
  const [time, pay] = arr[i].split(" ").map((v) => +v);
  if (i + time > dday) continue;
  days[i] += pay;
  for (let j = i + time; j < dday; j++) {
    days[j] = Math.max(days[j], days[i]);
  }
}
console.log(Math.max(...days));
