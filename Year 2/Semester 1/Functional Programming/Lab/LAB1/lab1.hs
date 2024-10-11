a = 2 + 3
b = head [4, 1, 3, 2]
c = tail [1, 2, 3]

double :: Integer -> Integer -- SIGNATURA FUNCTIEI (NU E OBLIGATORIU SA FIE INCLUSA)
double x = x + x
--double = (*2)

maxim :: Integer -> Integer -> Integer 
--maxim x y = if x > y then x else y
--maxim = \x y -> if x > y then x else y
maxim x y
   | x > y     = x
   | otherwise = y

d = double 6

main = do {
   print a;
   print b;
   print c;
   print d
}

-- :l lab1.hs INCARCA/COMPILEAZA FISIERUL
-- :r         REINCARCA/RECOMPILEAZA (DACA A FOST SCHIMBAT)
-- :t ceva    INTOARCE TIPUL DE DATE 