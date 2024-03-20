/** 최단경로 
 * https://www.acmicpc.net/problem/1753 */
let input = require('fs').readFileSync('example.txt').toString().trim().split('\n').map(a => a.split(' ').map(v=>+v));
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(a => a.split(' ').map(v=>+v));
const [V, E] = input[0];
const K = input[1];
const graph = Array.from({ length: V }, () => []);
const weight = Array.from({ length: V }, () => Infinity);
const visit = Array.from({ length: V }, () => 0);
weight[K - 1] = 0;
for (let i = 0; i < E; i++){
    const [u, v, w] = input[i + 2];
    graph[u - 1].push([v - 1, w]);
}
const getIdx = () => {
    let min = Infinity;
    let idx = 0;
    for (let i = 0; i < V; i++){
        if (!visit[i] && min > weight[i]){
            idx = i;
            min = weight[i];
        }
    }
    return idx;
}
const dijk = (s) => {
    weight[s] = 0;
    for (let i = 0; i < V; i++){
        const cur = getIdx();
        visit[cur] = 1;
        for (const [nxt, w] of graph[cur]) {
            if (weight[cur] + w < weight[nxt]){
                weight[nxt] = weight[cur] + w;
            }
        }
    }
}
dijk(K - 1);
weight.map(v => {
    if (v === Infinity) console.log('INF');
    else console.log(v);
});