main = do
  xs <- getContents
  print $ sum . map sum . map (map read) . part1 [] $ xs
  print $ sum . map sum . map (map read) . part2 [] $ xs

part1 xs [] = xs
part1 xs ys = part1 (x : xs) rest
  where
    x = filter invalidId $ range $ takeWhile (/= ',') ys
    rest = drop 1 $ dropWhile (/= ',') ys

part2 xs [] = xs
part2 xs ys = part2 (x : xs) rest
  where
    x = filter invalidId2 $ range $ takeWhile (/= ',') ys
    rest = drop 1 $ dropWhile (/= ',') ys

invalidId :: (Eq a) => [a] -> Bool
invalidId x = even (length x) && (take (div (length x) 2) x == (drop (div (length x) 2) x))

invalidId2 :: String -> Bool
invalidId2 x = any isRepeat [1 .. (length x `div` 2)]
  where
    isRepeat n =
      let (q, r) = length x `divMod` n
          pat = take n x
       in q >= 2 && r == 0 && concat (replicate q pat) == x

chunksOf :: Int -> [a] -> [[a]]
chunksOf n [] = []
chunksOf n xs = take n xs : chunksOf n (drop n xs)

range :: [Char] -> [String]
range xs = map show [a .. b]
  where
    a = read $ takeWhile (/= '-') xs :: Int
    b = read $ drop 1 $ dropWhile (/= '-') xs
