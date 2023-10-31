/**https://www.acmicpc.net/problem/1303
 * 전쟁 - 전투 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(" ").map((a) => +a);
const bg = input.slice(1).map((a) => a.split(""));
const dir = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];
const visited = Array.from(Array(M), () => Array(N).fill(0));
const bfs = (a, b, t) => {
  let cnt = 1;
  const queue = [[a, b]];
  visited[a][b] = 1;
  while (queue.length > 0) {
    const [x, y] = queue.shift();
    for (let i = 0; i < 4; i++) {
      const ax = x + dir[i][0];
      const ay = y + dir[i][1];
      if (0 <= ax && ax < M && 0 <= ay && ay < N) {
        if (visited[ax][ay] === 0 && bg[ax][ay] === t) {
          queue.push([ax, ay]);
          visited[ax][ay] = 1;
          cnt += 1;
        }
      }
    }
  }
  return cnt ** 2;
};
const power = { W: 0, B: 0 };
for (let t of Object.keys(power)) {
  for (let i = 0; i < M; i++) {
    for (let j = 0; j < N; j++) {
      if (bg[i][j] === t && visited[i][j] === 0) {
        power[t] += bfs(i, j, t);
      }
    }
  }
}
console.log(Object.values(power).join(" "));
