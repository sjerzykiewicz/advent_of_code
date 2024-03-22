import System.IO
import qualified Data.ByteString.Lazy.Char8 as LB
import Crypto.Hash

md5 :: String -> Digest MD5
md5 = hashlazy . LB.pack    

main :: IO ()
main = do
  fileHandle <- openFile "input.txt" ReadMode
  contents <- hGetContents fileHandle
  putStrLn ("Part One: " ++ show (findLowestNumber contents 5 0))
  putStrLn ("Part Two: " ++ show (findLowestNumber contents 6 0))
  hClose fileHandle

findLowestNumber :: String -> Int -> Int -> Int
findLowestNumber input numberOf0 number 
  | take numberOf0 (show (md5 (input ++ show number))) == concat (replicate numberOf0 "0") = number
  | otherwise = findLowestNumber input numberOf0 (number + 1)