// Getting the particular element in fibonacci series
const fibonacci = (N) => {
  if (N === 0 || N === 1) return N

  return fibonacci(N - 2) + fibonacci(N - 1)
}

// testing
(() => {
  const number = 5
  console.log(number + 'th Fibonacci number is ' + fibonacci(number))
})()