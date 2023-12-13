main = interact $ show . sum .map (solve . words) . lines

splitOn :: Char -> String -> [String]
splitOn _ [] = []
splitOn s xs = takeWhile (/= s) xs : splitOn s (drop 1 $ dropWhile (/= s) xs)

solve :: [String] -> Int
solve (x:y:_)= countCombs x (map read (splitOn ',' y)) 0

countCombs :: String -> [Int] -> Int -> Int
countCombs [] [] n = n+1
countCombs [] xs n = 0
countCombs xs [] n = n+1
countCombs (x:xs) (n:ns) c = case x of
            '.' -> countCombs xs (n:ns) c
            '?' -> countCombs ('#':xs) (n:ns) c + countCombs ('.':xs) (n:ns) c
            '#' -> if '.' `notElem` take n (x:xs)
                then countCombs (drop n xs) ns c
                else 0
            _ -> error "Not good"
