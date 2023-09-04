/**소수&팰린드롬
 * https://www.acmicpc.net/problem/1747 */
let n = +require("fs").readFileSync("example.txt").toString();
// let n = +require('fs').readFileSync('/dev/stdin').toString();
const eratos_lst = Array(1003002).fill(true);
eratos_lst[0] = eratos_lst[1] = false;
for (let i = 2; i <= 1001; i++) {
  if (eratos_lst[i]) {
    let a = 2;
    while (i * a < 1003002) {
      if (eratos_lst[i * a]) eratos_lst[i * a] = false;
      a++;
    }
  }
}
const palind = (num) => {
  const rev = num.split("").reverse().join("");
  if (rev === num) return true;
  else return false;
};
for (; n < 1003002; n++) {
  if (palind(String(n))) {
    if (eratos_lst[n]) break;
  }
}
console.log(n);
