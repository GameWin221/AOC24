module Main where
    
-- https://stackoverflow.com/questions/4503958/what-is-the-best-way-to-split-a-string-by-a-delimiter-functionally
splitBy :: (Foldable t, Eq a) => a -> t a -> [[a]]
splitBy delimiter = foldr f [[]] 
        where f c l@(x:xs) | c == delimiter = []:l
                           | otherwise = (c:x):xs

checkNumbers :: [Int] -> Int -> Int -> Int -> Bool
checkNumbers ns a b d = and [(abs (y - x) `elem` [a..b]) && signum (y - x) == d | (x, y) <- zip ns (tail ns)]

isSafe :: [Int] -> Bool
isSafe ns = checkNumbers ns 1 3 $ signum (ns !! 1 - ns !! 0)

main :: IO ()
main = do
    fileContents <- readFile "input.txt"
    let allNumbers = [[read x :: Int | x <- splitBy ' ' line] | line <- lines fileContents]
    print $ sum [1 | nums <- allNumbers, isSafe nums]