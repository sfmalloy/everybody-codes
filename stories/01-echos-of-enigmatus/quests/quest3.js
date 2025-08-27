import { readFileSync } from 'node:fs';

class Snail {
	constructor(x, y) {
		this.startX = x;
		this.startY = y;
		this.x = x;
		this.y = y;
		this.max = x + y - 1;
		this.offset = y;
	}

	// Keeping here for reference even though I don't use it in any solutions.
	// I used this to learn how the snails cycle.
	step() {
		this.x += 1;
		this.y -= 1;
		if (this.y < 1) {
			this.y = this.max;
			this.x = 1;
		}
	}
}

export function part1() {
	// All the snails happen to end up in the exact same spot
	// they started after 100 days...
	return readFileSync('inputs/quest3/part1.in')
		.toString()
		.trim()
		.split('\n')
		.map((line) => [
			parseInt(line.match(/x=(\d+)/)[1]),
			parseInt(line.match(/y=(\d+)/)[1]),
		])
		.reduce((a, [x, y]) => a + (x + 100 * y), 0);
}

export function part2() {
	return findAligned('inputs/quest3/part2.in');
}

export function part3() {
	return findAligned('inputs/quest3/part3.in');
}

function findAligned(filename) {
	let snails = readFileSync(filename)
		.toString()
		.trim()
		.split('\n')
		.map(
			(line) =>
				new Snail(
					parseInt(line.match(/x=(\d+)/)[1]),
					parseInt(line.match(/y=(\d+)/)[1])
				)
		);

	snails.sort((a, b) => b.max - a.max);
	const M = snails.reduce((a, b) => a * b.max, 1);
	let ans = 0;
	for (let i = 0; i < snails.length; ++i) {
		let m = snails[i].max;
		let n = Math.floor(M / m);
		let c = snails[i].offset;
		let inv = getModularInverses(n, m)[0];
		ans += (n * c * inv) % M;
	}

	return (ans % M) - 1;
}

function getModularInverses(a, b) {
	function coef(r, [x, y]) {
		return [y, x - r * y];
	}

	let s = [1, 0];
	let t = [0, 1];
	while (b) {
		const tmp = b;
		const div = Math.floor(a / b);
		b = a % b;
		a = tmp;

		s = coef(div, s);
		t = coef(div, t);
	}
	return [s[0], t[0]];
}
