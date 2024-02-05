/**N과 M (5)
 * https://www.acmicpc.net/problem/15654 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number).sort((a,b)=>a-b);
const visited = Array.from({ length: N }, () => false);
const res = Array.from({ length: M }, () => 0);
const searchFn = (idx, depth) => {
    if (depth === M) {
        console.log(res.join(' '));
        return
    }
    for (let i = 0; i < N; i++){
        if (visited[i]) continue;
        res[depth] = arr[i];
        visited[i] = true;
        searchFn(i, depth+1);
        visited[i] = false;
    }
}
searchFn(0,0);