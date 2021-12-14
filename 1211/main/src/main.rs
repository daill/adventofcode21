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

fn read_input(args: &Vec<String>) -> (Vec<u32>, u32) {
    let filename = &args[1];
    println!("filename {}", filename);
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    let mut lines : Vec<u32> = Vec::new();
    let mut length : u32 = 0;

    for line in reader.lines() {
        let line_content = line.unwrap();
        let char_vec : Vec<u32> = line_content.trim_end().to_string().chars().flat_map(|ch| ch.to_digit(10)).collect();
        length = char_vec.len() as u32;
        lines.extend(char_vec);
    }

    print_vec(&lines, length);
    return (lines, length);
}

fn print_vec(octs: &Vec<u32>, length: u32) {
    for y in 0..=(octs.len()-1) as u32 {
        if y%length == 0 && y != 0 {
            print!("\n");
        }
        print!("{}", octs[y as usize]);   
    }
    print!("\n\n");
}

fn blink(octs: &mut Vec<u32>, length: u32) {
    let mut sum = 0;
    let mut big_flash = false;
    let mut cntr = 0;
    while !big_flash {
        let mut seen : Vec<u32> = Vec::new();
        
        for i in 0..=octs.len()-1 {
            if !seen.contains(&(i as u32)) {
                //print!("before {} ", octs[i]);
                octs[i] += 1;
                //println!("after {}", octs[i]);
                if octs[i] > 9 {
                    octs[i] = 0;
                    // check surroundings
                    surroundings(octs, length, i as u32, &mut seen);
                }
            }
        }
        print_vec(&octs, length);
        if seen.len() == 100 {
            big_flash = true;
            print!("big flash at {}", cntr+1);
        }
        

        println!("next run");

        sum += seen.len();
        cntr += 1;
    }
    println!("sum {}", sum);
    
}

fn surroundings(octs: &mut Vec<u32>, length: u32, index: u32, seen: &mut Vec<u32>) {
    let norm = index%length;
    // top
    if !seen.contains(&index) {
        seen.push(index);
    }
    // println!("{:?}", seen);

    if index >= length {
        let top = index-length;

        if !seen.contains(&top) {
            octs[top as usize] += 1;
            if octs[top as usize] > 9 {
                octs[top as usize] = 0;
                seen.push(top);
                surroundings(octs, length, top, seen);
            }
        }
        // top left
        if (top%length) > 0 {
            let top_left = top-1;
            if !seen.contains(&top_left) {
                octs[top_left as usize] += 1;
                if octs[top_left as usize] > 9 {
                    seen.push(top_left);
                    octs[top_left as usize] = 0;
                    surroundings(octs, length, top_left, seen);
                }
            }
        }
        
        // top right
        if (top%length)+1 < length {
            let top_right = top+1;
            if !seen.contains(&top_right) {
                octs[top_right as usize] += 1;
                if octs[top_right as usize] > 9 {
                    seen.push(top_right);
                    octs[top_right as usize] = 0;
                    surroundings(octs, length, top_right, seen);
                }
            }
            
        }
        
    }

    // down
    let down = index+length;
    if down < octs.len() as u32 {
        if !seen.contains(&down) {
            octs[down as usize] += 1;
            if octs[down as usize] > 9 {
                seen.push(down);
                octs[down as usize] = 0;
                surroundings(octs, length, down, seen);
            }
        }
        
        // down left
        if (down%length) > 0 {
            let down_left = down-1;
            if !seen.contains(&down_left) {
                octs[down_left as usize] += 1;
                if octs[down_left as usize] > 9 {
                    octs[down_left as usize] = 0;
                    seen.push(down_left);
                    surroundings(octs, length, down_left, seen);
                }
            }
        }
            
        
        // down right
        if (down%length)+1 < length {
            let down_right = down+1;
            if !seen.contains(&down_right) {
                octs[down_right as usize] += 1;
                if octs[down_right as usize] > 9 {
                    octs[down_right as usize] = 0;
                    seen.push(down_right);
                    surroundings(octs, length, down_right, seen);
                }
            }
            
        }
    }
    // left
    if norm > 0 {
        let left = index-1;
        if !seen.contains(&left) {
            octs[left as usize] += 1;
            if octs[left as usize] > 9 {
                seen.push(left);
                octs[left as usize] = 0;
                surroundings(octs, length, left, seen);
            }
        }
    }

    // right
    if norm+1 < length {
        let right = index+1;
        if !seen.contains(&right) {
            octs[right as usize] += 1;
            if octs[right as usize] > 9 {
                octs[right as usize] = 0;
                seen.push(right);
                surroundings(octs, length, right, seen);
            }
        }
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let (mut lines, length) = read_input(&args);
    blink(&mut lines, length);
}