import { readFileSync } from 'node:fs';

abstract class Day {
	file: Buffer<ArrayBuffer>;

	constructor(inputPath: string) {
		this.file = readFileSync(inputPath);
	}

	abstract part1(): any;
	abstract part2(): any;
	abstract part3(): any;
}

export default Day;
