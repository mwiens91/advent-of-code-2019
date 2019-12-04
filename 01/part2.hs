-- The main function
main :: IO ()
main = sum . fmap (calculateFuel 0 . read) . lines <$> getContents >>= print

calculateFuel :: Int -> Int -> Int
calculateFuel accum mass
    | extraMass <= 0 = accum
    | otherwise = calculateFuel (accum + extraMass) extraMass
    where extraMass = calculateFuelBase mass

calculateFuelBase :: Int -> Int
calculateFuelBase mass = subtract 2 $ mass `div` 3
