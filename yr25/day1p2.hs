main = do
  xs <- fmap lines getContents
  print $ sum . map (length . filter (== 0)) $ part2 50 [] xs

part2 n ys [] = ys
part2 n ys (x : xs) = case x of
  ('L' : dist) -> part2 p (q : ys) xs
    where
      p = mod (n - read dist) 100
      q = map (flip mod 100) [(n - read dist) .. n - 1]
  ('R' : dist) -> part2 p (q : ys) xs
    where
      p = mod (n + read dist) 100
      q = map (flip mod 100) [n + 1 .. (n + read dist)]