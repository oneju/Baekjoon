/* 센서
https://www.acmicpc.net/problem/2212 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const sensor = input[2].split(" ").map((num) => +num);
sensor.sort((a, b) => a - b);
const dist = [];
for (let i = 1; i < +input[0]; i++) {
  dist.push(sensor[i] - sensor[i - 1]);
}
dist.sort((a, b) => a - b);
for (let i = 1; i < +input[1]; i++) {
  dist.pop();
}
const ans = dist.reduce((sum, num) => sum + num, 0);
console.log(ans);
