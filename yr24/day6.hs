import Data.List (nub)

main = do
  grid <- lines <$> getContents
  let test = (4, 6)
  let input = (95, 67)
  --   print $ length $ nub $ part1 grid [] input North
  let visited = part2 grid [] input North
  --   print visited
  print $ filter (checkForLoop grid visited) visited

part1 :: [String] -> [Pos] -> Pos -> Dir -> [Pos]
part1 grid visited pos dir = case get grid (move pos dir) of
  '.' -> part1 grid (pos : visited) (move pos dir) dir
  '#' -> part1 grid (pos : visited) (move pos (turn dir)) (turn dir)
  _ -> pos : visited

part2 :: [String] -> [(Pos, Dir)] -> Pos -> Dir -> [(Pos, Dir)]
part2 grid visited pos dir = case get grid (move pos dir) of
  '.' -> part2 grid ((pos, dir) : visited) (move pos dir) dir
  '#' -> part2 grid ((pos, turn dir) : visited) (move pos (turn dir)) (turn dir)
  _ -> (pos, dir) : visited

checkForLoop :: [String] -> [(Pos, Dir)] -> (Pos, Dir) -> Bool
checkForLoop grid xs (pos, dir) = any (\p -> p `elem` goLong grid (move pos (turn dir), turn dir)) xs

goLong :: [String] -> (Pos, Dir) -> [(Pos, Dir)]
goLong grid (pos, dir) = takeWhile (\(x, y) -> get grid x == '.') $ iterate (\(p, d) -> (move p d, d)) (pos, dir)

type Pos = (Int, Int)

data Dir = North | East | South | West
  deriving (Ord, Eq, Show, Enum)

turn :: Dir -> Dir
turn West = North
turn x = succ x

move :: Pos -> Dir -> Pos
move (x, y) dir = case dir of
  North -> (x, y - 1)
  East -> (x + 1, y)
  South -> (x, y + 1)
  West -> (x - 1, y)

get :: [String] -> Pos -> Char
get grid (x, y)
  | y < 0 || y >= length grid = 'e'
  | x < 0 || x >= length (head grid) = 'e'
  | otherwise = grid !! y !! x