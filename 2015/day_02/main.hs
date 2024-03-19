import System.IO
import Data.List

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (get_total_wraping_paper (lines contents)))
  putStrLn ("Part Two: " ++ show (get_total_ribbon_length (lines contents)))
  hClose fileHandle

get_total_wraping_paper :: [String] -> Int
get_total_wraping_paper = sum . map get_wrapping_paper

get_wrapping_paper :: String -> Int
get_wrapping_paper = get_wrapping_paper' . map read . wordsWhen (== 'x')

get_wrapping_paper' :: [Int] -> Int
get_wrapping_paper' [l, w, h] = (2 * a) + (2 * b) + (2 * c) + minimum [a, b, c]
  where a = l * w
        b = w * h
        c = h * l

get_total_ribbon_length :: [String] -> Int
get_total_ribbon_length = sum . map get_ribbon_length

get_ribbon_length :: String -> Int
get_ribbon_length = get_ribbon_length' . map read . wordsWhen (== 'x')

get_ribbon_length' :: [Int] -> Int
get_ribbon_length' [l, w, h] = (2 * a) + (2 * b) + l * w * h
  where a = minimum [l, w, h]
        b = minimum (delete a [l, w, h])

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'