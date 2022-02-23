use std::fmt::Debug;
use std::cmp::PartialOrd;

fn binary_search<T>(target: T, arr: &[T]) -> Option<usize> 
where 
    T: PartialEq + PartialOrd + Debug
{
    if arr.is_empty() { return None }

    let mid: usize = arr.len() / 2;
    if arr[mid] == target { return Some(mid) }

    if target < arr[mid] {
        return binary_search(target, &arr[0..mid]);
    } else {
        return binary_search(target, &arr[mid..arr.len()]);
    }
}

fn qsort<T>(arr: &Vec<T>) -> Vec<T>
where 
    T: PartialEq + PartialOrd + Debug + Clone
{
    // base case
    if arr.len() < 2 {
        return arr.clone()
    } else if arr.len() == 2 {
        if arr[0] < arr[1] {
            return arr.clone()
        } else {
            return vec![arr[1].clone(), arr[0].clone()]
        }
    }
    let mut left: Vec<T> = vec![];
    let mut right: Vec<T> = vec![];
    for i in 0..arr.len() {
        if arr[i] < arr[0] {
            left.push(arr[i].clone());
        } else {
            right.push(arr[i].clone())
        }
    }
    left.push(arr[0].clone());
    left.extend(right);
    return qsort(&left)
}

fn main() {
    let v_ = vec![1, 3, 5, 6, 8, 9, 13, 15];
    println!("{:?} is at index: {:?}", 3, binary_search(3, &v_));

    let v_2 = vec![7, 1, 5, 3, 6, 9, 2];
    println!("Sorted: {:?}", qsort(&v_2));
}
