main = do
  xs <- fmap lines getContents
  print $ part1 (0, 0) xs
  print $ part2 (1, 1) xs

part1 :: (Int, Int) -> [String] -> Int
part1 (x, y) xs
  | y >= length xs = 0
  | x >= length (head xs) = part1 (0, y + 1) xs
  | xs !! y !! x == 'X' =
      part1 (x + 1, y) xs
        + sum (map (getXMAS (x, y) xs) [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)])
  | otherwise = part1 (x + 1, y) xs

getXMAS :: (Int, Int) -> [String] -> (Int, Int) -> Int
getXMAS (x, y) xs (dx, dy) =
  let m = tryGet (x + dx, y + dy) xs
      a = tryGet (x + 2 * dx, y + 2 * dy) xs
      s = tryGet (x + 3 * dx, y + 3 * dy) xs
   in case (m, a, s) of
        (Just 'M', Just 'A', Just 'S') -> 1
        _ -> 0

part2 :: (Int, Int) -> [String] -> Int
part2 (x, y) xs
  | y >= length xs = 0
  | x >= length (head xs) = part2 (0, y + 1) xs
  | xs !! y !! x == 'A' =
      part2 (x + 1, y) xs + getMAS (x, y) xs 1 * getMAS (x, y) xs (-1)
  | otherwise = part2 (x + 1, y) xs

getMAS :: (Int, Int) -> [String] -> Int -> Int
getMAS (x, y) xs d
  | tryGet (x + d, y + d) xs == Just 'M' = if tryGet (x - d, y - d) xs == Just 'S' then 1 else 0
  | tryGet (x + d, y + d) xs == Just 'S' = if tryGet (x - d, y - d) xs == Just 'M' then 1 else 0
  | otherwise = 0

tryGet :: (Int, Int) -> [String] -> Maybe Char
tryGet (x, y) xs
  | y < 0 || y >= length xs = Nothing
  | x < 0 || x >= length (head xs) = Nothing
  | otherwise = Just $ xs !! y !! x
