/*
 * Copyright 2021 Christian Kramer
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
 * (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,
 * publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do
 * so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
 * LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO
 * EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */


use std::fs::File;
use std::io::{BufRead, BufReader};
use std::env;

static OPENINGS : [char; 4] = ['<', '(', '[', '{'];
static ENDINGS : [char; 4] = ['>', ')' ,']' ,'}'];

fn read_input(args: &Vec<String>) -> Vec<String> {
    let filename = &args[1];
    println!("filename {}", filename);
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    let mut lines = Vec::new();
    for line in reader.lines() {
        let line_content = line.unwrap();
        lines.push(line_content.trim_end().to_string());
    }

    return lines;
}

fn parse(lines: Vec<String>) -> (i32, i64) {
    let mut sum1 : i32 = 0;
    let mut sum2 : i64;
    let mut sums : Vec<i64> = Vec::new();
    for line in lines{
        sum1 += parse_line_one(&line);
        sum2 = parse_line_two(&line);
        if sum2 > 0 {
            sums.push(sum2);
        }
    }
    sums.sort();
    sum2 = sums[(sums.len()/2) as usize];

    return (sum1, sum2);
}

// part two
fn parse_line_two(line: &String) -> i64 {
    let mut opened : Vec<char> = Vec::new();
    let char_vec: Vec<char> = line.chars().collect();
    let mut sum : i64 = 0;
    for i in 0..=(char_vec.len()-1) {
        let c = char_vec[i];
        if OPENINGS.contains(&c) {
            opened.push(c);
        } else {
            let popped = opened.pop().unwrap();
            let oc = OPENINGS.iter().position(|&x| x == popped).unwrap();
            let ec = ENDINGS.iter().position(|&x| x == c).unwrap();
            if oc != ec {
                return 0;
            }
        }
    }
    opened.reverse();
    for c in opened {
        let e = OPENINGS.iter().position(|&x| x == c).unwrap();
        let ec = ENDINGS[e];
        sum *= 5;
        sum += match ec {
            ')' => 1,
            ']' => 2,
            '}' => 3,
            '>' => 4,
            _ => 0
        };
    }
    return sum
}

// part one
fn parse_line_one(line: &String) -> i32 {
    let mut opened : Vec<char> = Vec::new();
    let char_vec: Vec<char> = line.chars().collect();
    for i in 0..=(char_vec.len()-1) {
        let c = char_vec[i];
        if OPENINGS.contains(&c) {
            opened.push(c);
        } else {
            let popped = opened.pop().unwrap();
            let oc = OPENINGS.iter().position(|&x| x == popped).unwrap();
            let ec = ENDINGS.iter().position(|&x| x == c).unwrap();
            if oc != ec {
                return match ENDINGS[ec] {
                    ')' => 3,
                    ']' => 57,
                    '}' => 1197,
                    '>' => 25137,
                    _ => 0,
                };
            }
        }
    }

    return 0
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let lines = read_input(&args);
    let (sum1, sum2) = parse(lines);
    println!("sum1 {} sum2 {}", sum1, sum2);
}
