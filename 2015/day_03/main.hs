import System.IO
import qualified Data.Set as Set

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (length (getDifferentHouses contents 0 0 Set.empty)))
  putStrLn ("Part Two: " ++ show (length (getDifferentHousesWithRoboSanta contents 0 0 0 0 Set.empty)))
  hClose fileHandle

getDifferentHouses :: String -> Int -> Int -> Set.Set (Int, Int) -> Set.Set (Int, Int)
getDifferentHouses [] _ _ houses = houses
getDifferentHouses (command:commands) x y houses = getDifferentHouses commands x' y' houses'
  where x' = x + dx
        y' = y + dy
        houses' = Set.insert (x', y') houses
        (dx, dy) = case command of
          '^' -> (0, 1)
          'v' -> (0, -1)
          '<' -> (-1, 0)
          '>' -> (1, 0)

getDifferentHousesWithRoboSanta :: String -> Int -> Int -> Int -> Int -> Set.Set (Int, Int) -> Set.Set (Int, Int)
getDifferentHousesWithRoboSanta [] _ _ _ _ houses = houses
getDifferentHousesWithRoboSanta (command:command_robo:commands) x y xr yr houses = getDifferentHousesWithRoboSanta commands x' y' xr' yr' houses'
  where x' = x + dx
        y' = y + dy
        xr' = xr + dxr
        yr' = yr + dyr
        houses' = Set.insert (x', y') (Set.insert (xr', yr') houses)
        (dx, dy) = case command of
          '^' -> (0, 1)
          'v' -> (0, -1)
          '<' -> (-1, 0)
          '>' -> (1, 0)
        (dxr, dyr) = case command_robo of
          '^' -> (0, 1)
          'v' -> (0, -1)
          '<' -> (-1, 0)
          '>' -> (1, 0)