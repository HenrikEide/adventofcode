main = do
    xs <- fmap lines getContents
    print $ length $ filter (==0) $ part1 50 [] xs
    print $ sum $ part2 50 [] xs

part1 n yx [] = yx
part1 n yx (x:xs) = case x of
    ('L':d) -> part1 p (p:yx) xs
            where p = mod (n - read d) 100
    ('R':d) -> part1 p (p:yx) xs
            where p = mod (n + read d) 100

part2 n yx [] = yx
part2 n yx (x:xs) = case x of
    ('L':dist) -> part2 p (q:yx) xs
            where
                l = n - read dist
                p = mod l 100
                q = if l==0 then 1 else abs $ div (if n==0 then abs l else l) 100 
    ('R':dist) -> part2 p (q:yx) xs
            where
                l = n + read dist
                p = mod l 100
                q = div l 100