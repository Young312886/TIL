// let star = "*"
// for (let i = 1; i < 6; i++) {
//     console.log(star)
//     star = star + "*"
// }
const numbers = [1,2,3,4,5]
// 1.
for (num of numbers) {
    console.log(num)
}

function palindrome(str) {
  const right = str.split('')
  const left = str.split('').reverse()
  for (let i = 0; i < str.length; i++) {
    if (right[i] != left[i]) {
      console.log(false)
      return
    }
  }
  console.log(true)
  //
}

// 출력
palindrome('level')
palindrome('hi')

function palindrome(str) {
  const left = str.split('').reverse().join('')
  if (str != left) {
    console.log(false)
  }
  else if (str === left) {
    console.log(true)

  }
  
  //
}
palindrome('level')
palindrome('hi')

function sum(x,y) {
  console.log(x+y)
}
let a = sum(1,2)
console.log(a)


function sum(x,y) {
  return x+y
}

let b = sum(3,2)

console.log(b)


const star = "*"
const space = " "
for (var i = 1; i <5;i++){
    console.log(space.repeat(5-i),star.repeat(i*2-1),space.repeat(5-i))
}