import System.IO
import qualified Data.Set as Set

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (length (get_different_houses contents 0 0 Set.empty)))
  putStrLn ("Part Two: " ++ show (length (get_different_houses_with_robo_santa contents 0 0 0 0 Set.empty)))
  hClose fileHandle

get_different_houses :: String -> Int -> Int -> Set.Set (Int, Int) -> Set.Set (Int, Int)
get_different_houses [] _ _ houses = houses
get_different_houses (command:commands) x y houses = get_different_houses commands x' y' houses'
  where x' = x + dx
        y' = y + dy
        houses' = Set.insert (x', y') houses
        (dx, dy) = case command of
          '^' -> (0, 1)
          'v' -> (0, -1)
          '<' -> (-1, 0)
          '>' -> (1, 0)

get_different_houses_with_robo_santa :: String -> Int -> Int -> Int -> Int -> Set.Set (Int, Int) -> Set.Set (Int, Int)
get_different_houses_with_robo_santa [] _ _ _ _ houses = houses
get_different_houses_with_robo_santa (command:command_robo:commands) x y xr yr houses = get_different_houses_with_robo_santa commands x' y' xr' yr' houses'
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