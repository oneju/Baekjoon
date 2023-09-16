/**동전 1
 * https://www.acmicpc.net/problem/2293 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n);
const [n, k] = input[0].split(" ").map((a) => +a);
const dp = Array.from(Array(n + 1), () => Array(k + 1).fill(0));
dp.map((coin) => (coin[0] = 1));
for (let i = 1; i <= n; i++) {
  for (let price = 1; price <= k; price++) {
    if (price < input[i]) dp[i][price] = dp[i - 1][price];
    else dp[i][price] = dp[i - 1][price] + dp[i][price - input[i]];
  }
}
console.log(dp[n][k]);
