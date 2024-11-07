-- EX 1
sumaPatrateElemImpare :: [Int] -> Int
sumaPatrateElemImpare = \t -> foldl (+) 0 $ filter odd t


-- EX 2
verifTrue :: [Bool] -> Bool 
verifTrue = foldl (&&) True


-- EX 3
allVerifies :: (Int -> Bool) -> [Int] -> Bool
allVerifies = \f -> foldl (\acc x -> f x && acc) True


-- EX 4
anyVerifies :: (Int -> Bool) -> [Int] -> Bool 
anyVerifies = \f -> foldl (\acc x -> f x || acc) False


-- EX 5
mapFoldr :: (a -> a) -> [a] -> [a]
mapFoldr = \f -> foldr (\x acc -> f x : acc) []

mapFilter :: (a -> Bool) -> [a] -> [a]
mapFilter = \f -> foldr (\x acc -> if f x then x : acc else acc) []


-- EX 6
listToInt :: [Int] -> Int 
listToInt = foldl (\acc x -> x * 10 + acc) 0


-- EX 7
-- a)
rmChar :: Char -> String -> String 
rmChar = \c -> foldr (\x acc -> if x /= c then x : acc else acc) ""

-- b)
rmCharsRec :: String -> String -> String 
rmCharsRec _ ""    = ""
rmCharsRec "" s    = s
rmCharsRec (h:t) s = rmCharsRec t (rmChar h s)

-- c)
rmCharsFold :: String -> String -> String 
rmCharsFold = \sir1 sir2 -> foldr (\x aux -> if elem x aux then rmChar x aux else aux) sir2 sir1


-- EX 8
myReverse :: [Int] -> [Int]
myReverse = foldl (\acc x -> x : acc) []


-- EX 9
myElem :: Int -> [Int] -> Bool 
myElem x t = foldl (\acc y -> acc || x == y) False t


-- EX 10
myUnzip :: [(a, b)] -> ([a], [b])
myUnzip = foldr (\(x, y) (t1, t2) -> (x:t1, y:t2)) ([], [])


-- EX 11
union :: [Int] -> [Int] -> [Int]
union = \x -> foldl (\acc a -> if elem a acc then acc else a : acc) x


-- EX 12
intersect :: [Int] -> [Int] -> [Int]
intersect x y = foldl (\acc a -> if elem a x then a : acc else acc) [] y


-- EX 13
permutations' :: Int -> [Int] -> [[Int]]
permutations' x [] = [[x]]
permutations' x (h:t) = (x:h:t) : map (h:) (permutations' x t)

permutations :: [Int] -> [[Int]]
permutations t = foldr (\x acc -> concatMap (permutations' x) acc) [[]] 