use std::{time::Instant, env::args};

fn fib(num: i32) -> i32 {
    if num == 0 {
        return 0;
    }
    else if num == 1 {
        return 1;
    }
    else {
        return fib(num-1) + fib(num-2);
    }
}

fn main() {
    let start_time = Instant::now();

    let args: Vec<String> = args().collect();
    let args_1 = args.get(1);

    let num: i32 = match args_1 {
        Some(size_str) => {
            match size_str.parse::<i32>() {
                Ok(num) => num,
                Err(_) => 45
            }
        },
        None => 45
    };

    // let mut buf = String::new();
    // io::stdin().read_line(buf);
    // let num: i32 = match buf.trim().parse() {
    //     Ok(num) => num,
    //     Err => 45   // by cpp, calculating 45th fibonacci number takes about 4.6 sec
    // };

    let result: i32 = fib(num);
    let elapsed = start_time.elapsed();

    // println!("{}th fibonacci number: {}", num, result);
    println!("running time: {} ms", elapsed.as_millis());

}