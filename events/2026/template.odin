package ec2026

import "core:path/filepath"
import "core:math"
import "core:strconv"
import "core:time"
import "core:strings"
import "core:fmt"
import "core:os"

import "base:runtime"

main :: proc() {
    solve(1)
    solve(2)
    solve(3)
}

solve :: proc(part: int) {
    options := setup_solver(part)
    part := time.benchmark(&options)
    if (part == time.Benchmark_Error.Okay) {
        fmt.print(options.duration, "\n\n")
    }
}

setup_solver :: proc(part: int) -> time.Benchmark_Options {
    p := new(int)
    p^ = part

    options := time.Benchmark_Options{}
    options.user_data = p
    options.bench = proc(options: ^time.Benchmark_Options, allocator: runtime.Allocator) -> (err: time.Benchmark_Error) {
        sb, e := strings.builder_make()
        part := (cast(^int)options.user_data)^

        if e != nil {
            fmt.eprintln("Bad", e)
            return nil
        }

        filepath := fmt.sbprintf(&sb, "inputs/day01_part%d.txt", part)
        data, e2 := os.read_entire_file(filepath, context.allocator)
        if e2 != nil {
            fmt.eprintln("Unable to read file", e)
            return nil
        }
        defer delete(data, context.allocator)

        if part == 1 {
            fmt.println(solve1(data))
        } else if part == 2 {
            fmt.println(solve2(data))
        } else {
            fmt.println(solve3(data))
        }

        return nil
    }

    return options
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
