/** N과 M (9)
 * https://www.acmicpc.net/problem/15663 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number).sort((a, b) => a - b);

const visited = new Array(n).fill(0);
const output = new Set();

const searchFn = (perm) => {
    if (perm.length === m) {
        output.add(perm.join(' '));
        return;
    }
    for (let i = 0; i < n;i++) {
        if (visited[i]) continue;
        visited[i] = 1;
        searchFn([...perm,arr[i]]);
        visited[i] = 0;
    }
}
searchFn([]);
console.log([...output].join('\n'));