{-# LANGUAGE OverloadedStrings #-}

import Data.Text (pack, splitOn, unpack)

main = do
  xs <- map pack . lines <$> getContents
  let eqs = map ((\(x : y : _) -> (x, words y)) . map unpack . splitOn ": ") xs :: [(String, [String])]
  print $ map parseTree $ genEqs (snd (last eqs)) [""]
  print $ filter (\(x, y) -> x `elem` map (eval . parseTree) (genEqs y [""])) eqs

genEqs :: [String] -> [String] -> [String]
genEqs [x] eqs = map (++ x) eqs :: [String]
genEqs (x : xs) eqs = genEqs xs (map (\e -> e ++ x ++ "+") eqs) ++ genEqs xs (map (\e -> e ++ x ++ "*") eqs)

eval :: Ast -> String
eval (Num x) = show x
eval (Add x y) = show $ read (eval x) + read (eval y)
eval (Mul x y) = show $ read (eval x) * read (eval y)

parseTree :: String -> Ast
parseTree xs =
  let (a, b) = break (== '+') xs
   in if null b
        then
          let (c, d) = break (== '*') xs
           in if null d
                then Num (read c)
                else Mul (Num (read c)) (parseTree $ tail d)
        else Add (parseTree a) (parseTree $ tail b)

data Ast = Add Ast Ast | Mul Ast Ast | Num Int
  deriving (Show)
