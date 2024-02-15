/** 파티
 *  https://www.acmicpc.net/problem/1238 */
let input = require("fs").readFileSync("example.txt").toString().trim().split("\n").map(a=>a.split(' ').map(Number));
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(a=>a.split(' ').map(Number));
const [n, m, x] = input[0];
const goroute = Array.from({length:n},()=>[]);
const backroute = Array.from({length:n},()=>[]);
input.slice(1).map(v => {
    goroute[v[0]-1].push([v[1]-1,v[2]])
    backroute[v[1]-1].push([v[0]-1,v[2]])
});
const dijkstra = (g) => {
    const costs = Array(n).fill(Infinity);
    costs[x - 1] = 0;
    const queue = [];
    let idx = 0;
    queue.push([x-1, 0]);
    while (queue.length > idx) {
        const [curr, cost] = queue[idx++];
        for (const [v,c] of g[curr]){
            if ( costs[v] > c + cost ){
                costs[v] = c+cost;
                queue.push([v, costs[v]]);
            }
        }
    }
    return costs
}
const gocosts = dijkstra(goroute);
const backcosts = dijkstra(backroute);
let max_cost = 0;
for (let i = 0; i < n; i++){
    if (i !== x - 1)
        max_cost = Math.max(max_cost, gocosts[i] + backcosts[i]);
}

console.log(max_cost)
