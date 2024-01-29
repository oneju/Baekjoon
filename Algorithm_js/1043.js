/** 거짓말
 * https://www.acmicpc.net/problem/1043 */
let input = require("fs").readFileSync("example.txt").toString().split("\n");
// let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(a => +a);

// 진실을 알고있는 사람
const truth = Array.from({ length: N + 1 }, () => false);
const visited = Array.from({ length: N + 1 }, () => false);
// 2차원 배열에서 만난 사람들을 기록
const meeting = Array.from({ length: N + 1 }, () => Array(N + 1).fill(0));
const queue = [];
let answer = M;
input[1].split(' ').slice(1).map(a => {
    truth[+a] = true;
    queue.push(+a);
});

const party_list = input.slice(2).map(a => a.split(' ').map(v => +v));

for (let i = 0; i < M; i++){
    const party = party_list[i];
    for (let j of party.slice(1)){
        for (let p of party.slice(1)){
            if (j !== p) {
                meeting[j][p] = meeting[p][j] = 1;
            }
        }
    }
}

// 큐에서 꺼내서 만난 사람들 조사 <- 진실을 알고 있을 가능성 있는 사람들
let idx = 0;
while (idx < queue.length) {
    const know = queue[idx++];
    for (let i = 0; i < N; i++){
        if (meeting[know][i+1] === 1 && !visited[i+1]) {
            truth[i + 1] = true;
            visited[i + 1] = true;
            queue.push(i+1);
        }
    }
}

for (let i = 0; i < M; i++){
    const party = party_list[i].slice(1);
    if (party.some(a => truth[a])) {
        answer--;
    }
}
console.log(answer);