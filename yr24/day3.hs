import Data.Char (isDigit)
import Data.List (isPrefixOf)

main = do
  x <- getContents
  print $ sum $ map (uncurry (*)) $ parse x

parse :: String -> [(Int, Int)]
parse xs
  | "mul(" `isPrefixOf` xs,
    Just tup <- getTuple (drop 4 xs) =
      tup : parse (tail xs)
  | "don't()" `isPrefixOf` xs = dont xs
  | null xs = []
  | otherwise = parse (tail xs)

dont :: String -> [(Int, Int)]
dont xs
  | "do()" `isPrefixOf` xs = parse xs
  | null xs = []
  | otherwise = dont (tail xs)

getTuple :: String -> Maybe (Int, Int)
getTuple xs =
  let (num1, rest1) = span isDigit xs
      (comma, rest2) = splitAt 1 rest1
      (num2, rest3) = span isDigit rest2
   in if comma == "," && head rest3 == ')'
        then Just (read num1, read num2)
        else Nothing