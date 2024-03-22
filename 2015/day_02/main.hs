import System.IO
import Data.List

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (getTotalWrapingPaper (lines contents)))
  putStrLn ("Part Two: " ++ show (getTotalRibbonLength (lines contents)))
  hClose fileHandle

getTotalWrapingPaper :: [String] -> Int
getTotalWrapingPaper = sum . map getWrappingPaper

getWrappingPaper :: String -> Int
getWrappingPaper = getWrappingPaper' . map read . wordsWhen (== 'x')

getWrappingPaper' :: [Int] -> Int
getWrappingPaper' [l, w, h] = (2 * a) + (2 * b) + (2 * c) + minimum [a, b, c]
  where a = l * w
        b = w * h
        c = h * l

getTotalRibbonLength :: [String] -> Int
getTotalRibbonLength = sum . map getRibbonLength

getRibbonLength :: String -> Int
getRibbonLength = getRibbonLength' . map read . wordsWhen (== 'x')

getRibbonLength' :: [Int] -> Int
getRibbonLength' [l, w, h] = (2 * a) + (2 * b) + l * w * h
  where a = minimum [l, w, h]
        b = minimum (delete a [l, w, h])

wordsWhen :: (Char -> Bool) -> String -> [String]
wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'