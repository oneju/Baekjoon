/** 체스판 다시 칠하기
 * https://www.acmicpc.net/problem/1018 */
const input = require("fs").readFileSync("example.txt").toString().trim().split("\n");
//const input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M] = input[0].split(' ').map(n => +n);
let min_diff = 64;
const check = (si, sj) => {
  const first = ['B','W'];
  const mod = (si + sj) % 2;
  let cnt = 0;
  for (let chess = 0; chess < 2; chess++){
    for (let i = si; i < si + 8; i++){
      if (min_diff <= cnt) break;
      for (let j = sj; j < sj + 8; j++){
        if ((i + j) % 2 === mod) {
          if (input[i][j] !== first[chess]) cnt++;
        }
        else {
        if (input[i][j] === first[chess]) cnt++;
        }
      }
    }
    min_diff = Math.min(min_diff, cnt);
    cnt = 0;
  }
}

for (let x = 0; x < N - 7; x++) {
  for (let y = 0; y < M - 7; y++) {
    check(x+1, y);
  }
}

console.log(min_diff);