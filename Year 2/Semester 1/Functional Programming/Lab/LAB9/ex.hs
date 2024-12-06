data Tree = Empty | Node Int Tree Tree Tree 

extree :: Tree
extree = Node 4 (Node 5 Empty Empty Empty) (Node 3 Empty Empty (Node 1 Empty Empty Empty)) Empty


-- EX 1
class ArbInfo t where
   level    :: t -> Int 
   sumval   :: t -> Int 
   nrFrunze :: t -> Int
   
instance ArbInfo Tree where 
   level Empty = 0
   level (Node _ left mid right) = let x = level left; y = level mid; z = level right in 1 + maxVal x y z where maxVal a b c = max a . max b $ c
   
   sumval Empty = 0
   sumval (Node x left mid right) = x + sumval left + sumval mid + sumval right
   
   nrFrunze Empty = 0
   nrFrunze (Node _ Empty Empty Empty) = 1
   nrFrunze (Node _ left mid right) = nrFrunze left + nrFrunze mid + nrFrunze right
   

-- EX 2
class Scalar a where
   zero    :: a
   one     :: a
   adds    :: a -> a -> a
   mult    :: a -> a -> a
   negates :: a -> a
   recips  :: a -> a

instance Scalar Integer where 
   zero = 0
   one  = 1
   adds = (+)
   mult = (*)
   negates = negate
   recips = \x -> 1 `div` x

x :: Integer 
x = 5 
y :: Integer 
y = -3

-- EX 3
class (Scalar a) => Vector v a where
   zerov   :: v a
   onev    :: v a
   addv    :: v a -> v a -> v a
   smult   :: a -> v a -> v a
   negatev :: v a -> v a

data Vector2D a = Vector2D a a
   deriving (Show)

v1 = Vector2D 3 4
v2 = Vector2D 5 5

instance (Scalar a) => Vector Vector2D a where 
   zerov = Vector2D zero zero
   onev  = Vector2D one one 
   addv (Vector2D x1 y1) (Vector2D x2 y2) = Vector2D (adds x1 x2) (adds y1 y2)
   smult scalar (Vector2D x y) = Vector2D (mult scalar x) (mult scalar y)
   negatev (Vector2D x y) = Vector2D (negates x) (negates y)
   
data Vector3D a = Vector3D a a a 
   deriving (Show)
   
v3 = Vector3D 2 6 0
v4 = Vector3D (-1) 1 2
   
instance (Scalar a) => Vector Vector3D a where 
   zerov = Vector3D zero zero zero 
   onev  = Vector3D one one one 
   addv (Vector3D x1 y1 z1) (Vector3D x2 y2 z2) = Vector3D (adds x1 x2) (adds y1 y2) (adds z1 z2)
   smult scalar (Vector3D x y z) = Vector3D (mult scalar x) (mult scalar y) (mult scalar z)
   negatev (Vector3D x y z) = Vector3D (negates x) (negates y) (negates z)