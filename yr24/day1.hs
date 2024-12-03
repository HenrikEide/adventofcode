import Data.List (transpose, sort)

main :: IO ()
main = do
  xs <- fmap lines getContents
  let ys = map (map read . words) xs
  print $ (part1 . transpose . map sort . transpose ) ys
  print $ (part2 . transpose ) ys

part1 :: [[Int]] -> Int
part1 = sum . map (\(x:y:xs) -> abs (x-y))

part2 :: [[Int]] -> Int
part2 (ls:rs:_) = sum $ map (\x -> x * length (filter (x==) rs)) ls