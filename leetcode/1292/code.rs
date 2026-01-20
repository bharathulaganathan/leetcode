impl Solution {
    pub fn max_side_length(mat: Vec<Vec<i32>>, threshold: i32) -> i32 {
        let mut side: i32 = 1;
        let mut max_side: i32 = 0;
        let mut i: i32 = 0;
        let mut j: i32 = 0;
        let i_len = mat.len();
        let j_len = mat[i as usize].len();
        while i + side <= i_len as i32 && j + side <= j_len as i32 {
            let mut sum = 0;
            for k in (i..i+side) {
                for l in (j..j+side) {
                    sum += mat[k as usize][l as usize];
                }
            }
            if sum <= threshold {
                max_side = side;
                side += 1;
                continue
            }
            if j+side >= j_len as i32{
                j = 0;
                i +=1;
            } else {
                j +=1;
            }
        }
        return max_side
    }
}
