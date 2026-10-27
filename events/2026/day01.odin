package ec2026

import "core:math"
import "core:strings"
import "core:strconv"

solve1_1 :: proc(input: []byte) -> ReturnValue {
    it := string(input)
    ans := 0
    for line in strings.split_iterator(&it, ",") {
        num, ok := strconv.parse_int(line)
        root := int(math.ceil(math.sqrt(f32(num))))
        ans += (root * root) - num
    }

    return ans
}

solve1_2 :: proc(input: []byte) -> ReturnValue {
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

solve1_3 :: proc(input: []byte) -> ReturnValue {
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
