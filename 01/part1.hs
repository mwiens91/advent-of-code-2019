-- The main function
main :: IO ()
main = sum . fmap (calculateFuel . read) . lines <$> getContents >>= print

calculateFuel :: Int -> Int
calculateFuel mass = subtract 2 $ mass `div` 3
