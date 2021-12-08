use std::fs::File;
use std::io::{BufRead, BufReader};
use std::env;
use std::collections::HashMap;


fn read_input(args: &Vec<String>) -> HashMap<i32, i32> {
    let mut crabs = HashMap::new();
    let filename = &args[1];
    println!("filename {}", filename);
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    for line in reader.lines() {
        let line_content = line.unwrap();
        let crab_nums = line_content.split(",");
        for crab in crab_nums {
            let crab_str = crab.to_string();
            let entry = crabs.entry(crab_str.parse::<i32>().unwrap()).or_insert(1);
            *entry += 1;
        }
    }

    for (crab, &count) in crabs.iter() {
        println!("{}:{}", crab, count);
    }

    return crabs;
}

fn minimize() {

}

fn main() {
    let args: Vec<String> = env::args().collect();
    read_input(&args);
}
