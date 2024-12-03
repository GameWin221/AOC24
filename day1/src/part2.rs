use std::io::BufRead;
use std::collections::HashMap;

const INPUT: &[u8] = include_bytes!("input.txt");

pub fn answer() -> u32 {
    let mut counts0: HashMap<u32, u32> = HashMap::with_capacity(1024);
    let mut counts1: HashMap<u32, u32> = HashMap::with_capacity(1024);

    INPUT.lines().for_each(|line| {
        let line = line.unwrap();
        let mid = line.len() / 2;

        let d0 = line[0..mid-1].parse().unwrap();
        let d1 = line[mid+2..line.len()].parse().unwrap();

        if let Some(v) = counts0.get_mut(&d0) {
            *v += 1;
        } else {
            counts0.insert(d0, 1);
        }

        if let Some(v) = counts1.get_mut(&d1) {
            *v += 1;
        } else {
            counts1.insert(d1, 1);
        }
    });

    let mut result = 0;
    for (k0, v0) in counts0 {
        if let Some(v1) = counts1.get(&k0) {
            result += k0 * v0 * v1;
        }
    }

    result
}
