use std::fs::File;
use std::io::Read;

fn main() {
    let mut content = String::new();
    File::open("input.txt")
        .expect("Error opening file")
        .read_to_string(&mut content)
        .expect("Error reading file");

    let mut floors = 0;
    let mut bii = 0;
    for (i, c) in content.chars().enumerate() {
        match c {
            '(' => floors += 1,
            ')' => floors -= 1,
            _ => {}
        }
        if floors < 0 {
            if bii == 0 {
                bii = i + 1
            }
        }
    }
    println!("Part1: {}", floors);
    println!("Part2: {}", bii);
}