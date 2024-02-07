/** 숨바꼭질 3
 * https://www.acmicpc.net/problem/13549 */
let [N,K] = require("fs").readFileSync("example.txt").toString().trim().split(' ').map(Number);
// let [N,K] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const visit = Array.from({ length: Math.max(N,K) * 2 }, () => 0);

const search = () => {
    let idx = 0;
    const queue = [];
    queue.push([N, 0]);
    visit[N] = 1;
    while (queue.length>idx) {
        const [cur, time] = queue[idx++];
        
        if (cur === K) return time;
        
        if (cur*2<=100000 && !visit[cur * 2] ) {
            visit[cur * 2] = 1;
            queue.push([cur * 2, time]);
        }
        if (cur>0 && !visit[cur - 1]) {
            visit[cur - 1] =1;
            queue.push([cur -1, time+1]);
        } 
        if (cur+1<=100000 && !visit[cur + 1]) {
            visit[cur + 1] = 1;
            queue.push([cur +1, time+1]);
        }
    }
}
console.log(search())