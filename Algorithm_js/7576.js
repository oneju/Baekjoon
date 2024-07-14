/** 토마토
 * https://www.acmicpc.net/problem/7576 */
let input = require('fs').readFileSync('example.txt').toString().trim().split('\n').map(a => a.split(' ').map(a => +a));
// let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(a => a.split(' ').map(a => +a));
const [N, M] = input[0];
const storage = input.slice(1);
const rotten = [];
let nums = 0;
for (let i = 0; i <M; i++) {
  for (let j = 0; j <N; j++){
    if (storage[i][j] === 1) {
      rotten.push([i, j]);
    }
    if (storage[i][j] === 0) nums++;
  }
}
let days = 0;
const bfs = () => {
  const dir = [[0, 1], [1, 0], [0, -1], [-1, 0]];
  let lastlen = rotten.length;
  
  let idx = 0;
  while (idx < rotten.length) {
    const [x, y] = rotten[idx++];
    for (let i = 0; i < 4; i++){
      const [nx, ny] = [x + dir[i][0], y + dir[i][1]];
      if (nx >= M || ny >= N || nx < 0 || ny < 0) continue;
      if (storage[nx][ny] === 0) {
        nums--;
        storage[nx][ny] = 1;
        rotten.push([nx,ny])
      }
    }
    if (idx === lastlen) {
      days++;
      lastlen = rotten.length;
    }
  }
}

bfs();
console.log(nums>0?-1:days-1);