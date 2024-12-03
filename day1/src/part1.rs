use std::io::BufRead;

const INPUT: &[u8] = include_bytes!("input.txt");

/* 
fn bisect(v: &Vec<u32>, x: u32) -> u32 {
    let mut hi = v.len() as u32;
    let mut lo = 0;

    while lo < hi {
        let mid = (lo + hi) / 2;

        if x < v[mid as usize] {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }

    return lo;
}
*/

pub fn answer() -> u32 {
    let mut buf0: Vec<u32> = Vec::with_capacity(1024);
    let mut buf1: Vec<u32> = Vec::with_capacity(1024);

    INPUT.lines().for_each(|line| {
        let line = line.unwrap();
        let mid = line.len() / 2;

        let d0 = line[0..mid-1].parse().unwrap();
        let d1 = line[mid+2..line.len()].parse().unwrap();

        buf0.push(d0);
        buf1.push(d1);
        
        //buf0.insert(bisect(&buf0, d0) as usize, d0);
        //buf1.insert(bisect(&buf1, d1) as usize, d1);
    });

    buf0.sort();
    buf1.sort();

    let result: u32 = buf0.iter().zip(buf1.iter()).map(|(&a, &b)| {
        a.abs_diff(b)
    }).sum();

    result
}
