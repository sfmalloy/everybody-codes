import { readFileSync } from 'node:fs';

export function part1() {
	function eni(n, exp, mod) {
		let score = 1;
		let rem = [];
		for (let i = 0; i < exp; ++i) {
			score = (score * n) % mod;
			rem.push(score);
		}
		return parseInt(rem.reduceRight((prev, curr) => `${prev}${curr}`));
	}

	return getMaxEni('inputs/quest1/part1.in', eni);
}

export function part2() {
	function eni(n, exp, mod) {
		let score = 1;
		let rem = [];
		let foundCycle = false;
		for (let i = 0; i < mod; ++i) {
			score = (score * n) % mod;
			if (score === rem[0]) {
				foundCycle = true;
				break;
			}
			rem.push(score);
		}
		let res = [];
		let index = (exp - 1) % rem.length;
		if (!foundCycle) {
			return 0;
		}
		while (res.length < Math.min(exp, 5)) {
			res.push(rem[index]);
			index = index - 1;
			if (index < 0) {
				index += rem.length;
			}
		}
		return parseInt(res.join(''));
	}
	return getMaxEni('inputs/quest1/part2.in', eni);
}

export function part3() {
	function eni(n, exp, mod) {
		let score = 1;
		let rem = [];
		let seen = new Set();
		let cycleStart = 0;
		while (true) {
			score = (score * n) % mod;
			if (seen.has(score)) {
				cycleStart = score;
				break;
			}
			rem.push(score);
			seen.add(score);
		}
		let start = rem.findIndex((val) => val === cycleStart);
		let end = rem.length;
		let numLeftover = ((exp - 1) % (end - start)) + 1;
		let numCycles = Math.floor((exp - start) / (end - start));

		let cycleSum = rem.slice(start, end).reduce(sum, 0);
		let leftoverSum = rem.slice(start, numLeftover).reduce(sum, 0);
		let startSum = rem.slice(0, start).reduce(sum, 0);

		return startSum + cycleSum * numCycles + leftoverSum;
	}

	return getMaxEni('inputs/quest1/part3.in', eni);
}

function sum(a, b) {
	return a + b;
}

function getMaxEni(filename, eni) {
	return Math.max(
		...readFileSync(filename)
			.toString()
			.trim()
			.split('\n')
			.map((line) => line.split(/[A-Z]=(\d+)/))
			.map((nums) =>
				nums.filter((elem) => elem.trim()).map((elem) => parseInt(elem))
			)
			.map(
				([a, b, c, x, y, z, m]) => eni(a, x, m) + eni(b, y, m) + eni(c, z, m)
			)
	);
}
