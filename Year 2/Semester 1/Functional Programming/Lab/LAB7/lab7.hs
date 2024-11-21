data Expr = Const Int -- integer constant
   | Expr :+: Expr -- addition
   | Expr :*: Expr -- multiplication
   deriving Eq

data Operation = Add | Mult deriving (Eq, Show)

data Tree = Lf Int -- leaf
   | Node Operation Tree Tree -- branch
   deriving (Eq, Show)
   
instance Show Expr where
   show (Const x) = show x
   show (e1 :+: e2) = "(" ++ show e1 ++ " + "++ show e2 ++ ")"
   show (e1 :*: e2) = "(" ++ show e1 ++ " * "++ show e2 ++ ")"
   
   
-- EX 1
evalExp :: Expr -> Int 
evalExp (Const x) = x
evalExp (x :+: y) = evalExp x + evalExp y 
evalExp (x :*:y)  = evalExp x * evalExp y

exp1 = ((Const 2 :*: Const 3) :+: (Const 0 :*: Const 5))
exp2 = (Const 2 :*: (Const 3 :+: Const 4))
exp3 = (Const 4 :+: (Const 3 :*: Const 3))
exp4 = (((Const 1 :*: Const 2) :*: (Const 3 :+: Const 1)) :*: Const 2)
test11 = evalExp exp1 == 6
test12 = evalExp exp2 == 14
test13 = evalExp exp3 == 13
test14 = evalExp exp4 == 16


-- EX 2
evalArb :: Tree -> Int 
evalArb (Lf x)          = x 
evalArb (Node Add x y)  = evalArb x + evalArb y 
evalArb (Node Mult x y) = evalArb x * evalArb y

arb1 = Node Add (Node Mult (Lf 2) (Lf 3)) (Node Mult (Lf 0)(Lf 5))
arb2 = Node Mult (Lf 2) (Node Add (Lf 3)(Lf 4))
arb3 = Node Add (Lf 4) (Node Mult (Lf 3)(Lf 3))
arb4 = Node Mult (Node Mult (Node Mult (Lf 1) (Lf 2)) (Node Add (Lf 3)(Lf 1))) (Lf 2)
test21 = evalArb arb1 == 6
test22 = evalArb arb2 == 14
test23 = evalArb arb3 == 13
test24 = evalArb arb4 == 16


-- EX 3
expToArb :: Expr -> Tree 
expToArb (Const x) = Lf x
expToArb (x :+: y) = Node Add (expToArb x) (expToArb y)
expToArb (x :*: y) = Node Mult (expToArb x) (expToArb y)


-- EX 4
data IntSearchTree value
   = Empty
   | BNode
      (IntSearchTree value) -- elemente cu cheia mai mica
      Int -- cheia elementului
      (Maybe value) -- valoarea elementului
      (IntSearchTree value) -- elemente cu cheia mai mare
      deriving Show

tree1 :: IntSearchTree String
tree1 = BNode
   (Empty) 
   1 (Just "One") 
   (Empty)
tree2 :: IntSearchTree Int 
tree2 = BNode
   (BNode (Empty) 1 (Just 100) (Empty))
   2 (Just 200)
   (BNode (Empty) 3 (Just 300) (Empty))


lookup' :: Int -> IntSearchTree value -> Maybe value 
lookup' _ (Empty) = Nothing 
lookup' x (BNode left key val right)
   | x == key  = val
   | x < key   = lookup' x left 
   | otherwise = lookup' x right


-- EX 5
keys :: IntSearchTree value -> [Int]
keys Empty = []
keys (BNode left key val right) = [key] ++ keys left ++ keys right


-- EX 6
values :: IntSearchTree value -> [value]
values Empty = []
values (BNode left key val right) = [maybeToVal val] ++ values left ++ values right
   where
      maybeToVal (Just x) = x
      maybeToVal Nothing = []


-- EX 7
insert :: Int -> value -> IntSearchTree value -> IntSearchTree value 
insert k v (Empty) = BNode (Empty) k (Just v) (Empty)
insert k v (BNode left key val right)
   | k == key  = BNode left key (Just v) right
   | k < key   = BNode (insert k v left) key val right
   | otherwise = BNode left key val (insert k v right)


-- EX 8
delete :: Int -> IntSearchTree value -> IntSearchTree value 
delete _ (Empty) = Empty
delete k (BNode left key val right)
   | k == key  = BNode left key (Nothing) right 
   | k < key   = BNode (delete k left) key val right 
   | otherwise = BNode left key val (delete k right)


-- EX 9
toList :: IntSearchTree value -> [(Int, value)]
toList (Empty) = []
toList (BNode left key val right) = [(key, maybeToVal val)] ++ toList left ++ toList right
   where
      maybeToVal (Just x) = x


-- EX 10
insertPair :: (Int, value) -> IntSearchTree value -> IntSearchTree value
insertPair (k, v) Empty = BNode Empty k (Just v) Empty 
insertPair (k, v) (BNode left key val right)
   | k == key    = BNode left key (Just v) right
   | k < key     = BNode (insertPair (k, v) left) key val right
   | otherwise   = BNode left key val (insertPair (k, v) right) 

fromList :: [(Int, value)] -> IntSearchTree value 
fromList = foldr insertPair Empty