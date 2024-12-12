import Data.Maybe (fromJust)
import Data.List (nub)

type Nume = String
data Prop = Var Nume | F | T | Not Prop | Prop :|: Prop | Prop :&: Prop | Prop :->: Prop | Prop :<->: Prop
   deriving Eq
infixr 2 :|:
infixr 3 :&:


-- EX 1
p1 :: Prop
p1 = (Var "P" :|: Var "Q") :&: (Var "P" :&: Var "Q")

p2 :: Prop 
p2 = (Var "P" :|: Var "Q") :&: (Not (Var "P") :&: Not (Var "Q"))

p3 :: Prop 
p3 = (Var "P" :&: (Var "Q" :|: Var "R")) :&: ((Not (Var "P") :|: Not (Var "Q")) :&: (Not (Var "P") :|: Not (Var "R")))


-- EX 2
instance Show Prop where 
   show (Var p)     = p 
   show F           = "False"
   show T           = "True"
   show (Not p)     = "(~" ++ show p ++ ")"
   show (p :|: q)   = "(" ++ show p ++ " | " ++ show q ++ ")"
   show (p :&: q)   = "(" ++ show p ++ " & " ++ show q ++ ")"
   show (p :->: q)  = "(" ++ show p ++ " -> " ++ show q ++ ")"
   show (p :<->: q) = "(" ++ show p ++ " <-> " ++ show q ++ ")" 
   
test_ShowProp :: Bool
test_ShowProp = show (Not (Var "P") :&: Var "Q") == "((~P) & Q)"


-- EX 3
type Env = [(Nume, Bool)]
impureLookup :: Eq a => a -> [(a,b)] -> b
impureLookup a = fromJust . lookup a

eval :: Prop -> Env -> Bool 
eval (Var x) env     = impureLookup x env 
eval F _             = False
eval T _             = True 
eval (Not p) env     = not (eval p env)
eval (p :|: q) env   = eval p env || eval q env 
eval (p :&: q) env   = eval p env && eval q env
eval (p :->: q) env  = not (eval p env) || eval q env 
eval (p :<->: q) env = eval (p :->: q) env && eval (q :->: p) env  

test_eval = eval (Var "P" :|: Var "Q") [("P", True), ("Q", False)] == True


-- EX 4
variabile :: Prop -> [Nume]
variabile (Var p)     = [p]
variabile F           = []
variabile T           = []
variabile (Not p)     = variabile p
variabile (p :|: q)   = nub (variabile p ++ variabile q)
variabile (p :&: q)   = nub (variabile p ++ variabile q)
variabile (p :->: q)  = nub (variabile p ++ variabile q)
variabile (p :<->: q) = nub (variabile p ++ variabile q)

test_variabile = variabile (Not (Var "P") :&: Var "Q") == ["P", "Q"]


-- EX 5
envs :: [Nume] -> [Env]
envs []     = [[]]
envs (h:t) = [(h, False) : env | env <- envs t] ++ [(h, True) : env | env <- envs t]

test_envs = envs ["P", "Q"] == [[("P",False), ("Q",False)], [("P",False), ("Q",True)], [("P",True), ("Q",False)], [("P",True), ("Q",True)]]


-- EX 6
satisfiabila :: Prop -> Bool
satisfiabila p = elem True [eval p env | env <- envs (variabile p)]

test_satisfiabila1 = satisfiabila (Not (Var "P") :&: Var "Q") == True
test_satisfiabila2 = satisfiabila (Not (Var "P") :&: Not (Var "P")) == False


-- EX 7
valida :: Prop -> Bool
valida p = not . elem False $ [eval p env | env <- envs (variabile p)]

test_valida1 = valida (Not (Var "P") :&: Var "Q") == False
test_valida2 = valida (Not (Var "P") :|: Var "P") == True


-- EX 10
echivalenta :: Prop -> Prop -> Bool
echivalenta p q = not . elem False $ [eval p env == eval q env | env <- envs (variabile p ++ variabile q)]

test_echivalenta1 = True == (Var "P" :&: Var "Q") `echivalenta` (Not (Not (Var "P") :|: Not (Var "Q")))
test_echivalenta2 = False == (Var "P") `echivalenta` (Var "Q")
test_echivalenta3 = True == (Var "R" :|: Not (Var "R")) `echivalenta` (Var "Q" :|: Not (Var "Q"))
