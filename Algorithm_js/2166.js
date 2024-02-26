/** 다각형의 면적
 * https://www.acmicpc.net/problem/2166 */
let input = require("fs").readFileSync("example.txt").toString().trim().split("\n").map(a=>a.split(' ').map(a=>+a));
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(a=>a.split(' ').map(a=>+a));
/** 신발끈 공식 -> 다각형을 여러개의 삼각형으로 나누어 구하는 방식 */
let sum = 0;
for (let i = 0; i < input[0]; i++){
    sum += (input[i + 1][0] * input[i+1===+input[0]?1:i + 2][1]);
    sum -= (input[input[0] - i][0] * input[input[0] - i - 1 || input[0]][1]);
}
if (sum < 0) sum *= (-1);
console.log((sum / 2).toFixed(1));