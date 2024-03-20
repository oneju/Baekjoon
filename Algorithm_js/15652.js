/** N과 M (4)
 * https://www.acmicpc.net/problem/15652 */
let [N, M] = require("fs").readFileSync("example.txt").toString().trim().split(' ').map(a=>+a);
// let [N, M] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const arr = Array.from({ length: M }, () => 0);
const bfs = (num, d) => {
    if (d === M) {
        const str = arr.join(' ');
        console.log(str);
        return;
    }
    for (let i = num; i < N; i++){
        arr[d] = i + 1;
        bfs(i, d + 1);
    }
}
bfs(0, 0);