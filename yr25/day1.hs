main = do
  xs <- fmap lines getContents
  print $ length $ filter (== 0) $ part1 50 [] xs

part1 n yx [] = yx
part1 n yx (x : xs) = case x of
  ('L' : d) -> part1 p (p : yx) xs
    where
      p = mod (n - read d) 100
  ('R' : d) -> part1 p (p : yx) xs
    where
      p = mod (n + read d) 100