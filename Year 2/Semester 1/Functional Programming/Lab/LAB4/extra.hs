-- functia step 
step :: Char -> [Char] -> [String]
step p c = [take i c ++ [p] ++ drop (i + 1) c | (celula, i) <- zip c [0..], celula == ' '] 

-- functia next 
next :: Char -> [[Char]] -> [String]
next p cs = concatMap (step p) cs

-- functia win 
allLines :: [Char] -> [[Char]]
allLines t = [[t !! i | i <- line] | line <- [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]]

winningLine :: Char -> [Char] -> Bool
winningLine p t = any (all (==p)) (allLines t)

win :: Char -> [[Char]] -> [[Char]]
win c t = filter (winningLine c) t