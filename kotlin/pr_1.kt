/**
Complete the function solveMeFirst to compute the sum of two integers.

Example


Return .

Function Description

Complete the solveMeFirst function in the editor below.

solveMeFirst has the following parameters:

int a: the first value
int b: the second value
Returns
- int: the sum of  and 

Constraints
1<=a,b<=1000

Sample Input
a = 2
b = 3

Sample Output
5

Explanation
2+3=5
 */

import java.util.*

fun solveMeFirst(a: Int, b: Int): Int {
    return a + b
}

fun main(args: Array<String>) {
    val sc = Scanner(System.`in`)
    val num1 = sc.nextInt()
    val num2 = sc.nextInt()
    val sum = solveMeFirst(num1, num2)
    println(sum)
}