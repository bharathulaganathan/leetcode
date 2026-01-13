use std::cmp;

impl Solution {
    pub fn min_time_to_visit_all_points(points: Vec<Vec<i32>>) -> i32 {
        let mut time = 0;
        for i in 0..points.len()-1 {
            let x_diff = (points[i][0] - points[i+1][0]).abs();
            let y_diff = (points[i][1] - points[i+1][1]).abs();
            time += cmp::max(x_diff, y_diff);
        }
        return time
    }
}

let test_cases = vec![[[1, 1], [3, 4], [-1, 0]], [[3, 2], [-2, 2]]]
for p in 0..test_cases.len() {
    
}

