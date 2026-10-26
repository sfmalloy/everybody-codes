import Day from './day';

export default class Day02 extends Day {
	constructor(inputPath: string) {
		super(inputPath);
	}

	part1() {
		const lines = this.file.toString().split('\n');
		let pos: Vector = { r: 0, c: 0 };
		let bone: Vector = { r: 0, c: 0 };
		for (let r = 0; r < lines.length; ++r) {
			for (let c = 0; c < lines.length; ++c) {
				if (lines[r][c] === '@') {
					pos = { r, c };
				} else if (lines[r][c] === '#') {
					bone = { r, c };
				}
			}
		}

		const map = Array(lines.length).fill(Array(lines[0].length).fill(0));
		const dirs = [
			{ r: -1, c: 0 },
			{ r: 0, c: 1 },
			{ r: 1, c: 0 },
			{ r: 0, c: -1 },
		];
		let d = 0;
		let skipped = 0;
		while (pos.r !== bone.r || pos.c !== bone.c) {
			console.log(pos);
			const dir = dirs[d];
			d = (d + 1) % dirs.length;
			const next = this.step(pos, dir);
			if (map[next.r][next.c] === 1) {
				skipped += d;
			}
			pos = next;
			map[pos.r][pos.c] = 1;
		}

		return skipped;
	}

	part2() {}

	part3() {}

	step(pos: Vector, delta: Vector) {
		return { r: pos.r + delta.r, c: pos.c + delta.c };
	}
}

interface Vector {
	r: number;
	c: number;
}
