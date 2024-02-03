/** N과 M (2)
 * https://www.acmicpc.net/problem/15650 */
let [N, M] = require("fs").readFileSync("example.txt").toString().split(' ').map(a=>+a);
// let [N, M] = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
const arr = Array.from({ length: M }, () => 0);
const visited = Array.from({ length: N+1 }, () => 0);
const findArr = (num, idx) => {
    if (idx === M) {
        console.log(arr.join(' '));
        return
    }
    for (let i = num; i <= N; i++){
        if (visited[i]) continue;
        arr[idx] = i;
        visited[i] = 1;
        findArr(i, idx + 1);
        visited[i] = 0;
    }
}
findArr(1, 0);