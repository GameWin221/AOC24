const FILE_DATA: &str = include_str!("./input.txt");

struct FileRange {
    start: u32,
    size: u32,
    id: u32
}
struct FreeRange {
    start: u32,
    size: u32
}

fn find_free_range(free_ranges: &Vec<FreeRange>, free_ranges_acc: &Vec<Vec<u32>>, size: u32, end: u32) -> Option<usize> {
    for index in &free_ranges_acc[size as usize] {
        let range = &free_ranges[*index as usize];
        if range.start >= end {
            break;
        }

        if range.size >= size {
            return Some(*index as usize);
        }
    }

    None
}

fn main() {
    let start = std::time::Instant::now();

    let mut file_ranges: Vec<FileRange> = Vec::new();
    let mut free_ranges: Vec<FreeRange> = Vec::new();
    let mut free_ranges_acc: Vec<Vec<u32>> = vec![Vec::new(); 10];

    let mut file_id = 0;
    let mut block_index = 0;
    for (i, c) in FILE_DATA.chars().enumerate() {
        let region_is_file = i % 2 == 0;
        let region_size = c as u32 - '0' as u32;
        
        if region_size == 0 {
            continue;
        }

        if region_is_file {
            file_ranges.push(FileRange { start: block_index, size: region_size, id: file_id });
            file_id += 1;
        } else {
            let siz_idx = free_ranges.len() as u32;
            for siz in 1..=region_size as usize {
                free_ranges_acc[siz].push(siz_idx);
            }

            free_ranges.push(FreeRange { start: block_index, size: region_size });
        }

        block_index += region_size;
    }

    let mut checksum: i64 = 0;
    for id in (0..file_ranges.len()).rev() {
        let file_range = &file_ranges[id];

        if let Some(index) = find_free_range(&free_ranges, &free_ranges_acc, file_range.size, file_range.start) {
            let free_range = &free_ranges[index];

            checksum += (2 * free_range.start + file_range.size - 1) as i64 * file_range.size as i64 * id as i64 / 2;

            free_ranges[index] = FreeRange { start: free_range.start + file_range.size, size: free_range.size - file_range.size };
        } else {
            checksum += (2 * file_range.start + file_range.size - 1) as i64 * file_range.size as i64 * file_range.id as i64 / 2;
        }
    }
    let elapsed = start.elapsed();

    println!("{}, took {}ms", checksum, elapsed.as_secs_f64() * 1000.0);
}
