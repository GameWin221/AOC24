use std::time::Instant;

mod part1;
mod part2;

fn main() {
    let start = Instant::now();
    let result = part2::answer();
    let dur = start.elapsed();

    println!("{result}, took: {:.2}ms", dur.as_secs_f64() * 1000.0);
}