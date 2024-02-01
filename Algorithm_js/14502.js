/** 연구소
 * https://acmicpc.net/problem/14502 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(Number);
// 0은 빈 칸, 1은 벽, 2는 바이러스, 새로 새울 수 있는 벽 3
const board = input.slice(1).map(a => a.split(' ').map(Number));
// virus 위치 저장
const virus = [];
board.map((a, idx) => {
    for (let i = 0; i < M;i++) {
        if (a[i] === 2)
            virus.push([idx, +i]);
    }
});

// safety zone
const cntSafety = (arr) => {
    const dir = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    const q = [...virus];
    let idx = 0;

    // spread virus
    while (q.length > idx) {
        const [y, x] = q[idx++];
        for (let i = 0; i < 4; i++){
            const dy = y + dir[i][0];
            const dx = x + dir[i][1];
            if (dy >= 0 && dx >= 0 && dy < N && dx < M) {
                if (arr[dy][dx] === 0) {
                    arr[dy][dx] = 2;
                    q.push([dy, dx]);
                }
            }
        }
    }
    let cnt = 0;

    // 빈 칸 탐색
    for (let i = 0; i < N;i++) {
        for (let j = 0; j < M; j++){
            if (arr[i][j] === 0) cnt++;
        }
    }
    return cnt;
}

let max_cnt = 0;
// 벽 설치
const search = (depth) => {
    if (depth === 3) {
        const arr = board.map(v => [...v]);
        const cnt = cntSafety(arr);
        max_cnt = Math.max(cnt, max_cnt);
        return;
    }
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (board[i][j] === 0) {
                board[i][j] = 1;
                search(depth + 1);
                board[i][j] = 0;
            }
        }
    }
}

search(0);
console.log(max_cnt);