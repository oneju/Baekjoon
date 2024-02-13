/** 플로이드
 * https://www.acmicpc.net/problem/11404 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = +input[0];
const INF = 1e9;
let cost = Array.from({ length: n }, () => Array(n).fill(INF));
input.slice(2).map(path => {
    const [a, b, c] = path.split(' ').map(v => +v);
    if (cost[a - 1][b - 1] > c) {
        cost[a - 1][b - 1] = c;
    }
})
for (let k = 0; k < n; k++){
    for (let i = 0; i < n; i++){
        for (let j = 0; j < n; j++){
            if (i !== j && cost[i][k] + cost[k][j] < cost[i][j]) {
                cost[i][j] = cost[i][k] + cost[k][j];
            }
        }
    }
}
cost.forEach((city,i) => {
    console.log(city.map((v,j) => { if (v === INF) return 0; return v; }).join(' '))
})