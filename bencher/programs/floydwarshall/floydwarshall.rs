use std::io;

fn floydwarshall(graph: &mut Vec<Vec<i32>>, vertex_num: usize) {
    for k in 0..vertex_num {
        for i in 0..vertex_num {
            for j in 0..vertex_num {
                if graph[i][j] > graph[i][k] + graph[k][j] {
                    graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }
}

fn main() {
    let mut graph: Vec<Vec<i32>> = Vec::<Vec<i32>>::new();

    let mut buf = String::new();
    io::stdin().read_line(&mut buf).ok();
    let vertex_num: usize = match buf.trim().parse::<usize>() {
        Ok(a) => a,
        Err(_) => 0
    };

    for _ in 0..vertex_num {
        buf.clear();
        io::stdin().read_line(&mut buf).ok();
        graph.push(
            buf.split_whitespace().map(|s| s.parse().expect("parse error")).collect()
        );
    }

    floydwarshall(&mut graph, vertex_num);

    // for i in 0..10 {
    //     print!("{} ", graph[0][i]);
    // }
    println!();
}