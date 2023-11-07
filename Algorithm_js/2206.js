/**벽부수고이동하기
 * https://www.acmicpc.net/problem/2206 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(" ").map((a) => +a);
const map = input.slice(1).map((a) => a.split("").map((a) => +a));
const visited = Array.from({ length: N }, () =>
  Array.from({ length: M }, () => Array.from({ length: 2 }, () => -1))
);
visited[0][0][0] = 1;
const queue = [[0, 0, 0]];
const dir = [
  [0, -1],
  [1, 0],
  [0, 1],
  [-1, 0],
];
const bfs = () => {
  let idx = 0; // shift(<- 시간 초과가 난다) 대신 idx 를 옮겨가며 탐색
  while (idx < queue.length) {
    const [x, y, b] = queue[idx];
    if (x === N - 1 && y === M - 1) return visited[x][y][b];
    for (let i = 0; i < 4; i++) {
      const ax = x + dir[i][0];
      const ay = y + dir[i][1];
      if (ax < N && ax >= 0 && ay < M && ay >= 0) {
        if (map[ax][ay] === 0 && visited[ax][ay][b] === -1) {
          queue.push([ax, ay, b]);
          visited[ax][ay][b] = visited[x][y][b] + 1;
        } else if (map[ax][ay] === 1 && b === 0 && visited[ax][ay][1] === -1) {
          queue.push([ax, ay, 1]);
          visited[ax][ay][1] = visited[x][y][b] + 1;
        }
      }
    }
    idx += 1;
  }
  return -1;
};
console.log(bfs());
