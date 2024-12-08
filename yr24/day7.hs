{-# LANGUAGE OverloadedStrings #-}

import Data.Char (isDigit)
import Data.Text (pack, splitOn, unpack)

main = do
  xs <- map pack . lines <$> getContents
  let eqs = map ((\(x : y : _) -> (read x, map read (words y))) . map unpack . splitOn ": ") xs
  print $ sum $ map fst $ filter (\(x, y) -> x `elem` genEqs (tail y) [head y]) eqs

genEqs :: [Int] -> [Int] -> [Int]
genEqs [x] eqs = map (+ x) eqs ++ map (* x) eqs
genEqs (x : xs) eqs = genEqs xs $ map (+ x) eqs ++ map (* x) eqs
