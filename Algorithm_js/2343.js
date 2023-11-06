/**기타 레슨
 * https://www.acmicpc.net/problem/2343 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(" ").map((a) => +a);
const lectures = input[1].split(" ").map((a) => +a);
let high = lectures.reduce((a, b) => a + b, 0);
let low = Math.max(...lectures);
let answer = high;
while (low <= high) {
  const mid = ~~((high + low) / 2);
  let temp = 0;
  let cnt = 1;

  for (const lec of lectures) {
    if (temp + lec > mid) {
      temp = 0;
      cnt++;
      if (cnt > M) break;
    }
    temp += lec;
  }

  if (cnt > M) low = mid + 1;
  else {
    answer = answer > mid ? mid : answer;
    high = mid - 1;
  }
}
console.log(answer);
