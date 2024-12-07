{-# LANGUAGE OverloadedStrings #-}

import Control.Monad (ap)
import Data.Map (Map, empty, findWithDefault, fromList, insertWith, keys)
import Data.Maybe (fromMaybe)
import Data.Text (lines, pack, splitOn, unpack)

main = do
  [xs, ys] <- fmap (map Data.Text.lines . splitOn "\n\n" . pack) getContents
  let rules = map (map (read . unpack) . reverse . splitOn "|") xs
  let rulesM = fromList $ map ((\k -> (k, [head (tail x) | x <- rules, head x == k])) . head) rules :: Map Int [Int]
  print $ sum $ map (ap (!!) ((`div` 2) . length)) (filter (checkOrdering rulesM) (map (map (read . unpack) . splitOn ",") ys))

checkOrdering :: Map Int [Int] -> [Int] -> Bool
checkOrdering rulesM (x : xs)
  | null xs = True
  | any (`elem` xs) (findWithDefault [] x rulesM) = False
  | otherwise = checkOrdering rulesM xs
