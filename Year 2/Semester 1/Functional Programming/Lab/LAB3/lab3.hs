import Data.Char
import Data.List


-- EX 1
verifL :: [Int] -> Bool
verifL t = even (length t)

takeFinal :: [Int] -> Int -> [Int]
takeFinal t n
   | length t <= n = t
   | otherwise     = drop (length t - n) t
   
takeFinalSiruri :: [a] -> Int -> [a]
takeFinalSiruri str n
   | length str <= n = str 
   | otherwise       = drop (length str - n) str
   
remove :: [a] -> Int -> [a]
remove t n = take (n - 1) t ++ drop n t


-- EX 2
myReplicate :: Int -> Int -> [Int]
myReplicate 0 _ = []
myReplicate n v = [v] ++ myReplicate (n - 1) v

sumImp :: [Int] -> Int 
sumImp []    = 0
sumImp (h:t) = if odd h then h + sumImp t else sumImp t

totalLen :: [String] -> Int 
totalLen []    = 0
totalLen (h:t) = if h !! 0 == 'A' then length h + totalLen t else totalLen t


-- EX 3
nrVocale' :: String -> Int 
nrVocale' ""    = 0
nrVocale' (h:t) = if elem h "aeiouAEIOU" then 1 + nrVocale' t else nrVocale' t  

nrVocale :: [String] -> Int
nrVocale []    = 0
nrVocale (h:t) = if h == reverse h then nrVocale' h + nrVocale t else nrVocale t


-- EX 4
f :: Int -> [Int] -> [Int] 
f _ []    = []
f n (h:t) = if even h then [h] ++ [n] ++ f n t else [h] ++ f n t


-- EX 5
divizori :: Int -> [Int]
divizori n = [x | x <- [1..n], mod n x == 0]


-- EX 6
listadiv :: [Int] -> [[Int]]
listadiv []    = []
listadiv (h:t) = [divizori h] ++ listadiv t


-- EX 7
inIntervalRec :: Int -> Int -> [Int] -> [Int]
inIntervalRec _ _ []        = []
inIntervalRec inf sup (h:t) = if h <= sup && h >= inf then [h] ++ inIntervalRec inf sup t else inIntervalRec inf sup t  

inIntervalComp :: Int -> Int -> [Int] -> [Int]
inIntervalComp inf sup t = [x | x <- t, x <= sup && x >= inf]


-- EX 8
pozitiveRec :: [Int] -> Int 
pozitiveRec []    = 0
pozitiveRec (h:t) = if h > 0 then 1 + pozitiveRec t else pozitiveRec t 

pozitiveComp :: [Int] -> Int 
pozitiveComp t = length [x | x <- t, x > 0]


-- EX 9
pozitiiImpareRec' :: [Int] -> Int -> [Int]
pozitiiImpareRec' [] _    = []
pozitiiImpareRec' (h:t) i = if odd h then [i] ++ pozitiiImpareRec' t (i + 1) else pozitiiImpareRec' t (i + 1)

pozitiiImpareRec :: [Int] -> [Int]
pozitiiImpareRec t = pozitiiImpareRec' t 0

pozitiiImpareComp :: [Int] -> [Int]
pozitiiImpareComp t = [y | (x, y) <- zip t [0..], odd x]


-- EX 10
multDigitsRec :: String -> Int
multDigitsRec ""    = 1
multDigitsRec (h:t) = if isDigit h then digitToInt h * multDigitsRec t else multDigitsRec t

multDigitsComp :: String -> Int
multDigitsComp str = product [digitToInt x | x <- str, isDigit x]


-- EX 11
permutari' :: [a] -> [(a, [a])]
permutari' []    = []
permutari' (h:t) = (h, t) : [(h', h:t') | (h', t') <- permutari' t]

permutari :: [a] -> [[a]]
permutari [] = [[]]
permutari t  = [x:y | (x, z) <- permutari' t, y <- permutari z ]


-- EX 12
--combinari :: [a] -> Int -> [[a]]
--combinari t k = [x | x <- subsequences t, length x == k]

combinari :: Int -> [a] -> [[a]]
combinari 0 _  = [[]]
combinari _ [] = []
combinari n (h:t)
   | n < 0     = []
   | otherwise = [h:x | x <- combinari (n - 1) t] ++ combinari n t


-- EX 13
aranjamente :: Int -> [a] -> [[a]]
aranjamente n t = [x | combinare <- combinari n t, x <- permutari combinare]
