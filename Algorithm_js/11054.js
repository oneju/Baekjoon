/** 가장 긴 바이토닉 부분 수열
 * https://www.acmicpc.net/problem/11054 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

const arr = input[1].split(' ').map(Number)
const N = +input[0];
// [inc, dec]
const dp = Array.from({ length: N }, () => Array(2).fill(0));
// 기준 인덱스를 순차적으로 넣어가면서 최장 수열을 잡아야한다? 
// ex) i=1 -> 앞에 나보다 큰 수 얼마나 , 뒤에 나보다 작은 수 얼마나
// 1. i-1 이 i 보다 작은 경우 i-1 inc +1 , 같은경우엔 미동없음 , 큰 경우엔 ? 뒤에 배열만 탐색 ?
// 2. 반대로 i+1 i를 비교해서 ? 

for (let i = 1; i < N; i++){
    // inc
    if (arr[i] === arr[i - 1]) dp[i][0] = dp[i - 1][0];
    else {
        for (let j = i-1; j >=0; j--){
            if (arr[i] > arr[j]) {
                dp[i][0] = Math.max(dp[j][0]+1, dp[i][0]);
            } 
        }
    }

    // dec
    if (arr[N - i - 1] === arr[N - i]) dp[N - i - 1][1] = dp[N - i][1];
    else {
        for (let j = N - i; j < N; j++){
            if (arr[N - i - 1] > arr[j]) {
                dp[N - i - 1][1] = Math.max(dp[j][1] + 1,dp[N-i-1][1]);
            } 
        }
    }
}
let max = 0;
dp.map((a) => {
    if (a[0] + a[1] > max) max = a[0] + a[1];
}, 0);
console.log(max+1);