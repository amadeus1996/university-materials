-- EX 4
maxim :: Integer -> Integer -> Integer 
maxim x y = if x > y then x else y

maxim3 :: Integer -> Integer -> Integer -> Integer 
maxim3 x y z = if x >= y && x >= z then x else (if y >= x && y >= z then y else z)

maxim4 :: Integer -> Integer -> Integer -> Integer -> Integer
maxim4 a b c d = 
   let 
      x = maxim a b
      y = maxim c d
   in
      maxim x y
 
maxim4Verif :: Integer -> Integer -> Integer -> Integer -> Bool
maxim4Verif a b c d = 
   let 
      rez =
         if a >= b && a >= c && a >= d then a else (
            if b >= a && b >= c && b >= d then b else (
               if c >= a && c >= b && c >= d then c else d))
   in rez == maxim4 a b c d
   
   
-- EX 6
-- a)
sumaPatrate :: Integer -> Integer -> Integer 
sumaPatrate x y = x^2 + y^2

-- b)
parImpar :: Integer -> String
parImpar x
   | even x    = "par"
   | otherwise = "impar"
   
-- c)
factorial :: Integer -> Integer 
factorial 0 = 1
factorial n = n * factorial (n - 1)

-- d)
checkFst :: [Integer] -> Bool 
checkFst (h:t)
   | h > 2 * (head t) = True
   | otherwise        = False
   
-- e)
elemMaxim :: [Integer] -> Integer 
elemMaxim [] = -1
elemMaxim (h:t) = if h > elemMaxim t then h else elemMaxim t


-- EX 7
poly :: Double -> Double -> Double -> Double -> Double
poly a b c x = a * x^2 + b * x + c


-- EX 8
eeny :: Integer -> String 
eeny x
   | even x    = "eeny"
   | otherwise = "meeny"
   
  
-- EX 9
fizzbuzz :: Integer -> String 
fizzbuzz x
   | mod x 15 == 0 = "FizzBuzz"
   | mod x 3 == 0  = "Fizz"
   | mod x 5 == 0  = "Buzz"
   | otherwise     = ""
   
   
-- EX 10
tribonacciEcuational :: Integer -> Integer
tribonacciEcuational 1 = 1
tribonacciEcuational 2 = 2
tribonacciEcuational 3 = 3
tribonacciEcuational n = tribonacciEcuational (n - 1) + tribonacciEcuational (n - 2) + tribonacciEcuational ( n - 3)

tribonacciCazuri :: Integer -> Integer 
tribonacciCazuri n
   | n == 1 = 1
   | n == 2 = 2
   | n == 3 = 3
   | otherwise = tribonacciCazuri (n - 1) + tribonacciCazuri (n - 2) + tribonacciCazuri (n - 3)
   
   
-- EX 11
binomial :: Integer -> Integer -> Integer 
binomial _ 0 = 1
binomial 0 _ = 0
binomial n k = binomial (n - 1) k + binomial (n - 1) (k - 1)