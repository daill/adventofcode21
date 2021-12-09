use std::fs::File;
use std::io::{BufRead, BufReader};
use std::env;
use std::collections::HashMap;
use std::num::abs;


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

    return crabs;
}

fn minimize(crabs: HashMap<i32, i32>) {
    let biggest = crabs.keys().into_iter().max();
    let smallest = crabs.keys().into_iter().min();
    let sum = -1;
    let new_sum = -1;
    while biggest >= smallest {
        let temp_sum1 = 0;
        let temp_sum2 = 0;
        for crab in crabs.keys() {
            let t = (biggest.unwrap()-crab).abs();
            temp_sum1 = (t*(t+1))/2;
        }
    }

}

fn main() {
    let args: Vec<String> = env::args().collect();
    let crabs = read_input(&args);
    minimize(crabs)
}
