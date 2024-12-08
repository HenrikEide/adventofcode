{-# LANGUAGE OverloadedStrings #-}

import Data.Char (isDigit)
import Data.Text (pack, splitOn, unpack)

main = do
  xs <- map pack . lines <$> getContents
  let eqs = map ((\(x : y : _) -> (read x, map read (words y))) . map unpack . splitOn ": ") xs
  print $ tot eqs genEqs
  print $ tot eqs part2

tot xs g = sum $ map fst $ filter (\(x, y) -> x `elem` g (tail y) [head y]) xs

genEqs :: [Int] -> [Int] -> [Int]
genEqs [x] eqs = map (+ x) eqs ++ map (* x) eqs
genEqs (x : xs) eqs = genEqs xs $ map (+ x) eqs ++ map (* x) eqs

part2 :: [Int] -> [Int] -> [Int]
part2 [x] eqs = map (+ x) eqs ++ map (* x) eqs ++ map (read . (++ show x) . show) eqs
part2 (x : xs) eqs = part2 xs $ map (+ x) eqs ++ map (* x) eqs ++ map (read . (++ show x) . show) eqs