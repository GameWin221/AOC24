use std::{collections::HashSet, time::Instant};

const INPUT_FILE: &str = include_str!("input.txt");

fn find_guard(lines: &Vec<Vec<char>>) -> (i32, i32) {
    for (y, line) in lines.iter().enumerate() {
        for (x, &c) in line.iter().enumerate() {
            if c == '^' {
                return (x as i32, y as i32);
            }
        }
    }

    return (-1, -1);
}

fn check(lines: &Vec<Vec<char>>, width: i32, height: i32, s_px: i32, s_py: i32, s_dx: i32, s_dy: i32) -> bool {
    let mut move_map = [0u8; 140*140];
    
    let mut px = s_px;
    let mut py = s_py;
    let mut dx = s_dx;
    let mut dy = s_dy;
    
    loop {
        let nx = px as i32 + dx;
        let ny = py as i32 + dy;

        if nx < 0 || nx >= width || ny < 0 || ny >= height {
            return false;
        }

        if lines[ny as usize][nx as usize] == '#' {
            let old_dy = dy;
            dy = dx;
            dx = -old_dy;
            continue
        }

        let d_id = if dx == 0 {
            if dy > 0 { 1u8 } else { 2u8 }
        } else {
            if dx > 0 { 4u8 } else { 8u8 }
        };
                
        let t_id = py * width + px;
        if move_map[t_id as usize] & d_id != 0 {
            return true;
        }
        
        move_map[t_id as usize] |= d_id;

        px = nx;
        py = ny;
    }
}

fn find_path(lines: &Vec<Vec<char>>, width: i32, height: i32, s_px: i32, s_py: i32, s_dx: i32, s_dy: i32) -> HashSet<(i32, i32)> {
    let mut move_set: HashSet<(i32, i32)> = HashSet::with_capacity(1024);

    let mut px = s_px;
    let mut py = s_py;
    let mut dx = s_dx;
    let mut dy = s_dy;
    
    loop {
        let nx = px as i32 + dx;
        let ny = py as i32 + dy;

        if nx < 0 || nx >= width || ny < 0 || ny >= height {
            move_set.insert((px, py));
            move_set.remove(&(s_px, s_py));
            return move_set;
        }

        if lines[ny as usize][nx as usize] == '#' {
            let old_dy = dy;
            dy = dx;
            dx = -old_dy;
            continue
        }

        move_set.insert((px, py));

        px = nx;
        py = ny;
    }
}

// Reimplemented part2.py in Rust

fn main() {
    let mut lines: Vec<Vec<char>> = INPUT_FILE.lines().map(|line| line.chars().collect()).collect();

    let start = Instant::now();

    let width = lines[0].len() as i32;
    let height = lines.len() as i32;

    let (s_dx, s_dy) = (0, -1);
    let (s_px, s_py) = find_guard(&lines);
    lines[s_py as usize][s_px as usize] = '.';

    let mut result = 0;
    for (x, y) in find_path(&lines, width, height, s_px, s_py, s_dx, s_dy) {
        lines[y as usize][x as usize] = '#';

        if check(&lines, width, height, s_px, s_py, s_dx, s_dy) {
            result += 1;
        }

        lines[y as usize][x as usize] = '.';
    }

    let elapsed = start.elapsed();

    println!("{result}, took: {}ms", elapsed.as_secs_f64() * 1000.0)
}
