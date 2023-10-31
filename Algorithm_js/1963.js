/**소수 경로
 * https://www.acmicpc.net/problem/1963 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
/**1. 에라토스테네스의 체 -> 소수 판별
 * 2. bfs 탐색
 * 3. 탐색 도중 찾으면 탈출 못찾으면 impossible */
const eratos_lst = Array(10001).fill(true);
eratos_lst[0] = eratos_lst[1] = false;
for (let i = 2; i < 10001 / 2; i++) {
  if (eratos_lst[i]) {
    for (let a = 2 * i; a < 10001; a += i) eratos_lst[a] = false;
  }
}
let visited = [];
const bfs = (a, b) => {
  visited[a] = 0;
  const queue = [+a];

  while (queue.length) {
    const num = queue.shift();

    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 10; j++) {
        const arrnum = num.toString().split("");
        arrnum[i] = j;
        const newnum = +arrnum.join("");
        if ((i === 0 && j === 0) || visited[newnum] > -1 || !eratos_lst[newnum])
          continue;
        visited[newnum] = visited[num] + 1;

        queue.push(newnum);
        if (newnum === +b) return;
      }
    }
  }
};

for (let i = 0; i < input[0]; i++) {
  const [a, b] = input[i + 1].split(" ");

  visited = Array(10001).fill(-1);
  bfs(a, b);
  console.log(visited[b]);
}
