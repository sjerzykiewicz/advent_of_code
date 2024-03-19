import System.IO

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (find_floor contents))
  putStrLn ("Part Two: " ++ show (find_basement contents 0 1))
  hClose fileHandle

find_floor :: [Char] -> Int
find_floor [] = 0
find_floor ('(':xs) = find_floor xs + 1
find_floor (')':xs) = find_floor xs - 1

find_basement :: [Char] -> Int -> Int -> Int
find_basement [] _ _ = 0
find_basement ('(':xs) floor position = find_basement xs (floor + 1) (position + 1)
find_basement (')':xs) floor position
  | floor == 0 = position
  | otherwise = find_basement xs (floor - 1) (position + 1)
