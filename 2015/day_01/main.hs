import System.IO

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (findFloor contents))
  putStrLn ("Part Two: " ++ show (findBasement contents 0 1))
  hClose fileHandle

findFloor :: [Char] -> Int
findFloor [] = 0
findFloor ('(':xs) = findFloor xs + 1
findFloor (')':xs) = findFloor xs - 1

findBasement :: [Char] -> Int -> Int -> Int
findBasement [] _ _ = 0
findBasement ('(':xs) floor position = findBasement xs (floor + 1) (position + 1)
findBasement (')':xs) floor position
  | floor == 0 = position
  | otherwise = findBasement xs (floor - 1) (position + 1)
