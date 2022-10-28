const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().trim();
let ind = input*1;

function findQueens(n) {
	// 이곳에 작성합니다.
	function nQueen(row, size) {
		if (row === size) {
			answer += 1
		}
		else {
			for (let col = 0; col < size; col++) {
				if (visited[col] === 1) {
					continue
				}
				let a = row + col
				let b = row - col + (size - 1)
				if (accross1[a] === 1 || accross2[b] === 1){
					continue
				}
	
				visited[col] = accross1[a] = accross2[b] = 1
				nQueen(row + 1, size)
				visited[col] = accross1[a] = accross2[b] = 0
			}
		}
	}
	let answer = 0
	let visited = []
	for (let i = 0; i < n; i++){
		visited.push(0)
	}
	let accross1 = []
	let accross2 = []
	for (let i = 0; i < 2 * n; i++){
		accross1.push(0)
		accross2.push(0)
	}
	nQueen(0, n)

	return answer
}

console.log(findQueens(ind))
