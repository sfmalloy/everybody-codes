package ec2026

import "core:math"
import "core:strconv"
import "core:time"
import "core:strings"
import "core:fmt"
import "core:os"

import "base:runtime"

main :: proc() {
    solve(1, 1)
    solve(1, 2)
    solve(1, 3)
}

solve1 :: proc(input: []byte) -> int {
    it := string(input)
    ans := 0
    for line in strings.split_iterator(&it, ",") {
        num, ok := strconv.parse_int(line)
        root := int(math.ceil(math.sqrt(f32(num))))
        ans += (root * root) - num
    }

    return ans
}

solve2 :: proc(input: []byte) -> int {
    it := string(input)
    ans := 0

    frame_size :: proc(size: int) -> int {
        return 4 * size - 4
    }

    for line in strings.split_iterator(&it, ",") {
        num, ok := strconv.parse_int(line)
        i := 3
        for ; frame_size(i) < num; do i += 1
        local := frame_size(i) - num
        ans += local
    }

    return ans
}

solve3 :: proc(input: []byte) -> int {
    it := string(input)
    ans := 0

    frame_size :: proc(size: int) -> int {
        return size * size - 1
    }

    for line in strings.split_iterator(&it, ",") {
        num, ok := strconv.parse_int(line)
        i := 3
        for ; frame_size(i) < num; do i += 2
        local := frame_size(i) - num
        ans += local
    }

    return ans
}

// Template code

solve :: proc(day: int, part: int) {
    options := setup_solver(day, part)
    part := time.benchmark(&options)
    if (part == time.Benchmark_Error.Okay) {
        fmt.print(options.duration, "\n\n")
    }
}

SolverOptions :: struct {
    day: int,
    part: int,
}

setup_solver :: proc(day: int, part: int) -> time.Benchmark_Options {
    solver_options := new(SolverOptions)
    solver_options^ = SolverOptions{day, part}

    options := time.Benchmark_Options{}
    options.user_data = solver_options
    options.bench = proc(options: ^time.Benchmark_Options, allocator: runtime.Allocator) -> (err: time.Benchmark_Error) {
        sb, e := strings.builder_make()
        solver_options := (cast(^SolverOptions)options.user_data)^

        if e != nil {
            fmt.eprintln("Bad", e)
            return nil
        }

        filepath := fmt.sbprintf(&sb, "inputs/day%02d/part%d.txt", solver_options.day, solver_options.part)
        data, e2 := os.read_entire_file(filepath, context.allocator)
        if e2 != nil {
            fmt.eprintln("Unable to read file", e)
            return nil
        }
        defer delete(data, context.allocator)

        if solver_options.part == 1 {
            fmt.println(solve1(data))
        } else if solver_options.part == 2 {
            fmt.println(solve2(data))
        } else {
            fmt.println(solve3(data))
        }

        return nil
    }

    return options
}
