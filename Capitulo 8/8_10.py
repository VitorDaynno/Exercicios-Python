def fibonacci(n):
  a = 0
  b = 1

  while(n > 0):
    b, a = a + b, b
    n = n-1

    print(b)



fibonacci(10)