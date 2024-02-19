/** 웜홀
 * https://www.acmicpc.net/problem/1865 */
let input = require("fs").readFileSync("example.txt").toString().trim().split("\n").map(a=>a.split(' ').map(Number));
// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(a=>a.split(' ').map(Number));
let idx = 1;
const bellman = (graph,n) => {
    const time = Array.from({ length: n+1 },()=>1000000000);
    time[1] = 0;
    for (let j = 1; j <= n; j++){
        for (let i = 1; i < n+1; i++){
            for (const [to,cost] of graph[i]){
                if (time[to] > time[i] + cost) {
                    time[to] = time[i] + cost;
                    if (j === n) return 'YES';
                }
            }
        }
    }
    return 'NO';
}
for (let i = 0; i < +input[0]; i++){
    const [n, m, w] = input[idx++];
    const distance = Array.from({length:n+1},()=>[]);
    input.slice(idx, idx += m).map(([s, e, t] )=> {
        distance[s].push([e, t]);
        if (s!==e) distance[e].push([s, t]);
    });
    input.slice(idx, idx += w).map(([s, e, t]) => {
        distance[s].push([e, -t]);
    });
    const tc = bellman(distance,n);
    console.log(tc);
}