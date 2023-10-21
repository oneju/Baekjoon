/* 바이러스
https://www.acmicpc.net/problem/2606 */
let input = require("fs")
  .readFileSync(__dirname + "/example.txt")
  .toString()
  .split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const networks = Array.from(Array(+input[0]), () => []);
for (let i = 0; i < input[1]; i++) {
  const [a, b] = input[i + 2].split(" ").map((a) => +a);
  networks[a - 1].push(b - 1);
  networks[b - 1].push(a - 1);
}
const visited = Array(+input[0]).fill(0);
let cnt = 0;
visited[0] = 1;
const dfs = (com) => {
  for (const next of networks[com]) {
    if (visited[next] === 0) {
      visited[next] = 1;
      cnt += 1;
      dfs(next);
    }
  }
};
dfs(0);
console.log(cnt);
