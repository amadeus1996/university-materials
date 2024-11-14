-- EX 1
data Fruct = Mar String Bool | Portocala String Int
cosFructe = [Mar "Ionatan" False, Portocala "Sanguinello" 10, Portocala "Valencia" 22, Mar "Golden Delicious" True, Portocala "Sanguinello" 15, Portocala "Moro" 12, Portocala "Tarocco" 3, Portocala "Moro" 12, Portocala "Valencia" 2, Mar "Golden Delicious" False, Mar "Golden" False, Mar "Golden" True]

-- a)
ePortocalaDeSicilia :: Fruct -> Bool
ePortocalaDeSicilia (Portocala s _) = if elem s ["Tarocco", "Moro", "Sanguinello"] then True else False
ePortocalaDeSicilia _ = False

-- b)
nrFeliiSicilia :: [Fruct] -> Int
nrFeliiSicilia fructe = sum [felii | Portocala s felii <- fructe, ePortocalaDeSicilia (Portocala s felii)]

-- c)
nrMereViermi :: [Fruct] -> Int
nrMereViermi fructe = length [valoare | Mar s valoare <- fructe, valoare]


-- EX 2
type NumeA  = String 
type Rasa   = String 
data Animal = Pisica NumeA | Caine NumeA Rasa
   deriving Show

-- a)
vorbeste (Pisica _) = "Meow!"
vorbeste _          = "Woof!"

-- b)
rasa :: Animal -> Maybe String
rasa (Caine _ r) = Just r
rasa _           = Nothing   


-- EX 3
data Linie = L [Int]
   deriving Show 
data Matrice = M [Linie]
   deriving Show
   
-- a)
verifica (M matr) n = foldr (\x acc -> acc && x == n) True [sumaLinie linie | linie <- matr]
   where
      sumaLinie (L t) = sum t

-- b)
doarPozN (M matr) n = foldl (\acc x -> acc && allPoz x) True [linie | linie <- matr, lungimeLinie linie == n]
   where
      lungimeLinie (L t) = length t
      allPoz (L t)       = foldl (\acc x -> acc && x > 0) True t

-- c)
corect :: Matrice -> Bool
corect (M [])   = True 
corect (M [_])  = True
corect (M (r1:r2:rows)) = if not (lungimiEgale r1 r2) then False else corect (M (r2:rows))
   where 
      lungimiEgale (L t1) (L t2) = length t1 == length t2


-- EX 4
-- a)
data Direction = N | NE | E | SE | S | SV | V | NV 
   deriving Show
data Turtle    = Turtle Int Int Direction
   deriving Show

-- b)
data Action = Step | Turn | Seq Action Action

-- c)
data Command = Do Action | Repeat Int Action | Wait

-- d)
step :: Turtle -> Turtle 
step (Turtle x y N)  = Turtle x (y + 1) N 
step (Turtle x y NE) = Turtle (x + 1) (y + 1) NE
step (Turtle x y E)  = Turtle (x + 1) y E
step (Turtle x y SE) = Turtle (x + 1) (y - 1) SE 
step (Turtle x y S)  = Turtle x (y - 1) S 
step (Turtle x y SV) = Turtle (x - 1) (y - 1) SV 
step (Turtle x y V)  = Turtle (x - 1) y V 
step (Turtle x y NV) = Turtle (x - 1) (y + 1) NV

turn :: Turtle -> Turtle 
turn (Turtle x y N)  = Turtle x y NE
turn (Turtle x y NE) = Turtle x y E 
turn (Turtle x y E)  = Turtle x y SE
turn (Turtle x y SE) = Turtle x y S 
turn (Turtle x y S)  = Turtle x y SV 
turn (Turtle x y SV) = Turtle x y V 
turn (Turtle x y V)  = Turtle x y NV 
turn (Turtle x y NV) = Turtle x y N

performAction :: Action -> Turtle -> Turtle 
performAction Step turtle = step turtle
performAction Turn turtle = turn turtle
performAction (Seq a1 a2) turtle = performAction a2 (performAction a1 turtle)

performCommand :: Command -> Turtle -> Turtle 
performCommand (Do Step) (Turtle x y dir) = step (Turtle x y dir)
performCommand (Repeat 0 _) turtle = turtle
performCommand (Repeat n Step) (Turtle x y dir) = performCommand (Repeat (n - 1) Step) (step (Turtle x y dir))
performCommand (Do Turn) (Turtle x y dir) = turn (Turtle x y dir)
performCommand (Repeat n Turn) (Turtle x y dir) = performCommand (Repeat (n - 1) Turn) (turn (Turtle x y dir))
performCommand Wait turtle = turtle

getPizza :: [Command] -> Turtle -> (Int, Int)
getPizza [] (Turtle x y dir) = (x, y)
getPizza (command:commands) turtle = getPizza commands (performCommand command turtle)

-- f)
--agregare :: [Command] -> Turtle -> Command