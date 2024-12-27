use md5::{Md5, Digest};
use std::str;
use std::fs::File;
use std::io::{BufReader, BufRead};

fn find_number(key: Vec<u8>, zeroes: usize) -> u32 {
    let key_str = str::from_utf8(&key).unwrap().to_owned();
    let search_target = "0".repeat(zeroes);
    let mut number = 0;

    loop {
        let combined_str = key_str.clone() + number.to_string().as_str();

        let mut hasher = Md5::new();
        hasher.update(combined_str.as_bytes());
        let result = hasher.finalize();

        if format!("{:x}", result).starts_with(&search_target) {
            break;
        }
        number += 1;
    }
    number
}

fn main() {
    // Still having issue of million ways to read something from file
    let file = File::open("input.txt").expect("no such file");
    let buf = BufReader::new(file);
    let lines: Vec<String> = buf.lines().map(|l| l.expect("Line parse failed")).collect();

    for line in lines {
        println!("Part1: {}", find_number(line.clone().into_bytes(), 5));
        println!("Part2: {}", find_number(line.clone().into_bytes(), 6));
    }
}