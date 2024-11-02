-- EX 1
-- [4, 25, 64]
-- [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), ..., (5, 5), (5, 6), (5, 7)]
-- [(1, 1), (2, 1), (2, 2), ..., (3, 8), (3, 9)]
-- "FMI"
-- [[1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [2, 3], [2, 3, 4], [2, 3, 4, 5], [3, 4], [3, 4, 5], [4, 5]]


-- EX 2
factori :: Int -> [Int]
factori n = [x | x <- [1..n], mod n x == 0]


-- EX 3
prim :: Int -> Bool
prim n = (length $ factori n) == 2


-- EX 4
numerePrime :: Int -> [Int]
numerePrime n = [x | x <- [2..n], prim x]


-- EX 5
myzip3' :: [a] -> [a] -> [a] -> Int -> Int -> Int -> [(a, a, a)]
myzip3' _ _ _ 0 _ _ = []
myzip3' _ _ _ _ 0 _ = []
myzip3' _ _ _ _ _ 0 = []
myzip3' (h1:t1) (h2:t2) (h3:t3) n1 n2 n3 = [(h1, h2, h3)] ++ myzip3' t1 t2 t3 (n1 - 1) (n2 - 1) (n3 - 1)

myzip3 :: [a] -> [a] -> [a] -> [(a, a, a)]
myzip3 a b c = myzip3' a b c (length a) (length b) (length c)


-- EX 6
firstEl :: [(a, b)] -> [a]
firstEl = map fst


-- EX 7
sumList :: [[Int]] -> [Int]
sumList = map sum


-- EX 8
prel2 :: [Int] -> [Int]
prel2 = map (\x -> if odd x then x * 2 else x `div` 2)


-- EX 9
continCaracter :: Char -> [String] -> [String]
continCaracter c = filter (elem c)


-- EX 10
patrateImpare :: [Int] -> [Int]
patrateImpare t = map (^2) $ filter (odd) t


-- EX 11
patratePozImpare :: [Int] -> [Int]
patratePozImpare t = map (\(x, _) -> x^2) $ filter (\(_, y) -> odd y) $ zip t [0..]


-- EX 12
eliminareConsoane :: [String] -> [String]
eliminareConsoane = map (\x -> filter (\y -> elem y "aeiouAEIOU") x)


-- EX 13
mymap :: (a -> a) -> [a] -> [a]
mymap f t = [f x | x <- t]

myfilter :: (a -> Bool) -> [a] -> [a]
myfilter f t = [x | x <- t, f x]