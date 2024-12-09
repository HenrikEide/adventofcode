main = do
  xs <- getContents
  let cmp = takeWhile (/= ".") $ pack $ expand 0 xs
  print $ sum $ zipWith (\i x -> i * read x) [0 ..] cmp

expand :: Int -> [Char] -> [String]
expand ind (x : y : xs) = replicate (read [x]) (show ind) ++ replicate (read [y]) "." ++ expand (ind + 1) xs
expand _ [] = []
expand ind x = replicate (read x) (show ind)

pack :: [String] -> [String]
pack (x : xs)
  | x == "." = let (n, rest) = nextBlock (reverse xs) in n : pack (reverse rest)
  | null xs = [x]
  | otherwise = x : pack xs

nextBlock :: [String] -> (String, [String])
nextBlock (x : xs)
  | x /= "." = (x, xs)
  | null xs = (".", [])
  | otherwise = nextBlock xs
