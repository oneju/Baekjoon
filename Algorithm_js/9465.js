/** 스티커
 * https://www.acmicpc.net/problem/9465 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const getScore = (arr) => {
    const N = +arr[0];
    const dp = arr.slice(1).map(a => a.split(' ').map(v => +v));
    for (let j = 0; j < N; j++){
        for (let i = 0; i < 2; i++) {
            if (j > 1) {
                dp[i][j] += Math.max(dp[i ? 0 : 1][j - 1], dp[i][j - 2], dp[i ? 0 : 1][j - 2]);
            }
            else if (j===1) {
                dp[i][j] += dp[i ? 0 : 1][j - 1];
            }
        }
    }
    return Math.max(dp[0][N-1],dp[1][N-1]);
}

for (let T = 0; T < +input[0]; T++){
    const answer = getScore(input.slice((T * 3) + 1, (T * 3) + 4));
    console.log(answer);
}