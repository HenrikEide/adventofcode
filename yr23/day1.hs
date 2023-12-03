import Data.Char (isNumber)
import Data.Text (pack, unpack, replace)
import Data.Bifunctor (bimap)
main = do
    input <- map pack . lines <$> readFile "input.txt"
    let names = map (bimap pack pack) 
                    [
                    ("oneight", "18"), 
                    ("threeight", "38"), 
                    ("sevenine", "79"), 
                    ("eighthree", "83"), 
                    ("twone", "21"),
                    ("fiveight", "58"), 
                    ("eightwo", "82"), 
                    ("one", "1"), 
                    ("two", "2"), 
                    ("three", "3"), 
                    ("four", "4"),
                    ("five", "5"),
                    ("six", "6"),
                    ("seven", "7"),
                    ("eight", "8"), 
                    ("nine", "9")
                    ]
    let input' = map (\x -> foldl (\x (a, b) -> replace a b x) x names) input
    let numbers = map (read . (\x -> [head x, last x]) . filter isNumber . unpack) input'
    print $ sum numbers
