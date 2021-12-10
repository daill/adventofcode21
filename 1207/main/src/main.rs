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
            crabs.entry(crab_str.parse::<i32>().unwrap()).and_modify(|e| { *e += 1 }).or_insert(1);
        }
    }

    return crabs;
}

fn minimize(crabs: HashMap<i32, i32>) {
    let mut biggest = *crabs.keys().into_iter().max().unwrap();
    let mut smallest = *crabs.keys().into_iter().min().unwrap();
    let mut sum = -1;
    let mut new_sum;
    while biggest >= smallest {
        let mut temp_sum1 : i64 = 0;
        let mut temp_sum2 : i64 = 0;
        for crab in crabs.keys() {
            let n = crabs[crab];
            let t1 = (smallest-crab).abs();
            temp_sum1 += (((t1 * (t1 + 1)) / 2) * n) as i64;

            let t2 = (biggest-crab).abs();
            temp_sum2 += (((t2 * (t2 + 1)) / 2) * n) as i64;
        }
        if temp_sum2 < temp_sum1 {
            new_sum = temp_sum2;
        } else {
            new_sum = temp_sum1;
        }
        smallest += 1;
        biggest -= 1;

        if sum == -1 || (sum > new_sum) {
            sum = new_sum;
        }
    }
    println!("sum {}",sum);
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let crabs = read_input(&args);
    minimize(crabs)
}
