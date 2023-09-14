// 가르침
// https://www.acmicpc.net/problem/1062
const input = require("fs").readFileSync("example.txt").toString().split("\n");
// const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, K] = input[0].split(" ").map((x) => Number(x));
const lst = input
  .slice(1)
  .map((str) => (str.length >= 8 ? str.slice(4, str.length - 4) : "--"));

const visited = Array(26).fill(0);
let max = 0;

for (let alph of "antic") {
  visited[alph.charCodeAt(0) - 97] = 1;
}

const combi = (index, depth) => {
  if (depth === K) {
    let count = 0;
    for (let word of lst) {
      if (word === "--") continue;
      let read = true;
      for (let a of word) {
        if (visited[a.charCodeAt(0) - 97] === 0) {
          read = false;
          break;
        }
      }
      if (read) count += 1;
    }
    max = count > max ? count : max;
    return;
  }
  for (let i = index; i < 26; i++) {
    if (visited[i] === 0) {
      visited[i] = 1;
      combi(i + 1, depth + 1);
      visited[i] = 0;
    }
  }
};

if (K < 5) max = 0;
else if (K >= 26) max = N;
else combi(0, 5);

console.log(max);
