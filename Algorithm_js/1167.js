/** 트리의 지름
 * https://www.acmicpc.net/problem/1167 */
let input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let root = 0;
const tree = Array(+input[0]).fill([]);

input.slice(1).map((e, idx) => {
    const arr = e.split(' ').map(Number);
    tree[arr[0] - 1] = arr.slice(1, arr.length - 1);
    if (tree[root].length < tree[arr[0]-1].length) root = idx;
});

let max = { leaf: 0, weight: 0 };
const visited = Array(+input[0]).fill(0);

const dfs = (c, w) => {
    visited[c] = 1;
    if (max.weight < w) max = { leaf: c, weight: w };
    for (let i = 0; i < ~~(tree[c].length / 2); i++){
        const [n, q] = tree[c].slice(i * 2, i * 2 + 2);
        if (!visited[n-1]) {
            dfs(n-1,w+q);
        }
    }
}

dfs(root, 0);
visited.fill(0);
dfs(max.leaf, 0);
console.log(max.weight)