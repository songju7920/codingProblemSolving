function solution(dots) {
    dots.sort((a, b) => a[0] - b[0])
    let size = [Math.abs(dots[0][0] - dots[2][0]), Math.abs(dots[0][1] - dots[1][1])]
    return size[0] * size[1];
}