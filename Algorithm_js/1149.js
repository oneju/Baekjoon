/** RGB 거리
 * https://www.acmicpc.net/problem/1149 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const N = +input[0];
const dp = input.slice(1).map(a=>a.split(' ').map(a=>+a));
for (let i = 1; i < N; i++){
    for (let j = 0; j < 3; j++){
        dp[i][j] += Math.min(...dp[i - 1].filter((v, idx) => idx !== j));
    }
}
const answer = Math.min(...dp[N - 1]);
console.log(answer)