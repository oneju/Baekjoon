/**숫자세는 양 (Large)
 * https://www.acmicpc.net/problem/14382 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let number = "0";
const sleep = (arr, num, n) => {
  number = String(Number(num) * n);
  const newarr = Array.from(new Set(number.split("")));
  arr = [...new Set([...arr, ...newarr])];
  if (arr.length === 10) return;
  else sleep(arr, num, n + 1);
};

for (let index = 1; index <= input[0]; index++) {
  if (input[index] === "0") number = "INSOMNIA";
  else {
    sleep([], input[index], 1);
  }
  console.log(`Case #${index}: ${number}`);
}
