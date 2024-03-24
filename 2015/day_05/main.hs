import System.IO

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (countNiceStrings (lines contents)))
  putStrLn ("Part Two: " ++ show (countNiceStringsPart2 (lines contents)))
  hClose fileHandle

countNiceStrings :: [String] -> Int
countNiceStrings [] = 0
countNiceStrings (x:xs) = if atLeast3Vowels x && hasDoubleLetter x && doesNotContain x 
  then countNiceStrings xs + 1 
  else countNiceStrings xs

atLeast3Vowels :: String -> Bool
atLeast3Vowels input = (length . filter (`elem` "aeiou")) input >= 3

hasDoubleLetter :: String -> Bool
hasDoubleLetter [] = False
hasDoubleLetter [_] = False
hasDoubleLetter (x1:x2:xs) = x1 == x2 || hasDoubleLetter (x2:xs)

doesNotContain :: String -> Bool
doesNotContain [] = True
doesNotContain [_] = True
doesNotContain ('a':'b':_) = False
doesNotContain ('c':'d':_) = False
doesNotContain ('p':'q':_) = False
doesNotContain ('x':'y':_) = False
doesNotContain (_:xs) = doesNotContain xs

countNiceStringsPart2 :: [String] -> Int
countNiceStringsPart2 [] = 0
countNiceStringsPart2 (x:xs) = if containsTwoPairs x && containRepeatedLetter x 
  then countNiceStringsPart2 xs + 1 
  else countNiceStringsPart2 xs

containsTwoPairs :: String -> Bool
containsTwoPairs [] = False
containsTwoPairs [_] = False
containsTwoPairs (x1:x2:xs) = containsPair x1 x2 xs || containsTwoPairs (x2:xs)

containsPair :: Char -> Char -> String -> Bool
containsPair _ _ [] = False
containsPair _ _ [_] = False
containsPair a b (x1:x2:xs) = (a == x1 && b == x2) || containsPair a b (x2:xs)

containRepeatedLetter :: String -> Bool
containRepeatedLetter [] = False
containRepeatedLetter [_] = False
containRepeatedLetter [_,_] = False
containRepeatedLetter (x1:x2:x3:xs) = x1 == x3 || containRepeatedLetter (x2:x3:xs)
