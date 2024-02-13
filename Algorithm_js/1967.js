/** 트리의 지름
 * https://www.acmicpc.net/problem/1967 */
let input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = +input[0];
const visited = Array(n).fill(0);
const tree = Array.from({ length: n },()=>[]);
input.slice(1).forEach(e => {
    const [p, c, w] = e.split(' ').map(Number);
    tree[c - 1].push([p - 1,w]);
    tree[p - 1].push([c - 1,w]);
});
let max = {leaf:0, weight: 0};

const dfs = (c, w) => {
    visited[c] = 1;
    if (max.weight < w) max = { leaf: c, weight: w };
    for (let [n,q] of tree[c]){
        if (!visited[n]) {
            dfs(n,w+q);
        }
    }
}

// 루트에서 가장 max weight를 갖는 노드 찾기
dfs(0, 0);
visited.fill(0);
// 가장 멀리있는 노드에서 가장 멀리있는 노드를 탐색
dfs(max.leaf, 0);

console.log(max.weight);