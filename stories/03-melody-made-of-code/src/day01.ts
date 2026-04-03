import Day from './day';

export default class Day01 extends Day {
	constructor(inputPath: string) {
		super(inputPath);
	}

	isUpper(c: string): boolean {
		return c === c.toUpperCase();
	}

	private mapColor(color: string) {
		return parseInt(
			color
				.split('')
				.map((e) => (this.isUpper(e) ? '1' : '0'))
				.join(''),
			2,
		);
	}

	part1() {
		this.parse()
			.map(this.parseColors.bind(this))
			.filter((c) => c.g > c.r && c.g > c.b)
			.reduce((a, b) => a + b.id, 0);
	}

	part2() {
		const shines = this.parse()
			.map(this.parseColors.bind(this))
			.sort((a, b) => b.s - a.s);
		const max = this.max(shines, (a, b) => a.s > b.s).s;
		return shines
			.filter(({ s }) => s === max)
			.map(({ id, r, g, b }) => ({ id, c: r + g + b }))
			.sort((a, b) => a.c - b.c)
			.at(0)!.id;
	}

	part3() {
		const scales = this.parse().map(this.parseColors.bind(this));
		const shiny = scales.filter(({ s }) => s >= 33);
		const matte = scales.filter(({ s }) => s <= 30);

		const shinyRed = shiny.filter(
			({ r, g, b }) => Math.max(r, g, b) === r && r !== g && r !== b,
		);
		const shinyGreen = shiny.filter(
			({ r, g, b }) => Math.max(r, g, b) === g && g !== r && g !== b,
		);
		const shinyBlue = shiny.filter(
			({ r, g, b }) => Math.max(r, g, b) === b && b !== r && b !== g,
		);

		const matteRed = matte.filter(
			({ r, g, b }) => Math.max(r, g, b) === r && r !== g && r !== b,
		);
		const matteGreen = matte.filter(
			({ r, g, b }) => Math.max(r, g, b) === g && g !== r && g !== b,
		);
		const matteBlue = matte.filter(
			({ r, g, b }) => Math.max(r, g, b) === b && b !== r && b !== g,
		);

		const all = [
			shinyRed,
			shinyGreen,
			shinyBlue,
			matteRed,
			matteGreen,
			matteBlue,
		];

		const maxLen = Math.max(...all.map((l) => l.length));

		return all
			.filter((l) => l.length === maxLen)
			.at(0)!
			.reduce((a, b) => a + b.id, 0);
	}

	parse() {
		return this.file
			.toString()
			.trimEnd()
			.split('\n')
			.filter((line) => line);
	}

	parseColors(line: string) {
		const [id, colorLine] = line.split(':');
		const [r, g, b, s] = colorLine?.split(' ');
		return {
			id: parseInt(id),
			r: this.mapColor(r),
			g: this.mapColor(g),
			b: this.mapColor(b),
			s: s ? this.mapColor(s) : 0,
		};
	}

	max<T>(lst: T[], cmp: (a: T, b: T) => boolean) {
		return lst.reduce((a, b) => (cmp(a, b) ? a : b));
	}
}
