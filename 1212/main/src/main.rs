use std::fs::File;
use std::io::{BufRead, BufReader};
use std::env;
use std::collections::HashMap;
use regex::Regex;



fn read_input(args: &Vec<String>) -> HashMap<String, Vec<String>>{
    let filename = &args[1];
    println!("filename {}", filename);
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file);
    let mut coords : HashMap<String, Vec<String>> = HashMap::new();


    for line in reader.lines() {
        let line_content = line.unwrap();
        let pairs : Vec<&str> = line_content.split("-").collect();

        if coords.contains_key(pairs[0]) {
            let vec = coords.get_mut(pairs[0]).unwrap();
            vec.push(pairs[1].to_owned());
        } else {
            let mut vec : Vec<String> = Vec::new();
            vec.push(pairs[1].to_owned());
            coords.insert(pairs[0].to_owned(), vec.to_owned());
        }
    }

    println!("{:?}", coords);
    return coords;
}

fn iter(coords: &HashMap<String, Vec<String>>, node: &String, call_node: &String, mut seen: Vec<String>, mut way: Vec<String>) {
    let re = Regex::new(r"^[A-Z]$").unwrap();


    if !re.is_match(node) && node != "start" {
        if !seen.contains(node) {
            seen.push(node.clone());
        } else {
            return;
        }
    }

    way.push(node.clone());

    if node == "end" {
        println!("end {:?}", way);
        way.pop();
    }

    println!("way {:?} seen {:?}", way, seen);

    if coords.contains_key(node) {
        for a in coords.get(node).unwrap() {
            //if !seen.contains(a) {
                iter(coords, a, node, seen.clone(), way.clone());
        
            //} else {
                // iter(coords, node, node, seen.clone(), way.clone());
            //}
        }
    } else {
        if !seen.contains(call_node){
            iter(coords, call_node, node, seen.clone(), way.clone());
        }
    }
}

fn find_ways(coords: HashMap<String, Vec<String>>) {
    let seen : Vec<String> = Vec::new();
    let way: Vec<String> = Vec::new();
    iter(&coords, &String::from("start"), &String::from(""), seen, way);
}


fn main() {
    let args: Vec<String> = env::args().collect();
    let coords = read_input(&args);
    find_ways(coords);
    
}