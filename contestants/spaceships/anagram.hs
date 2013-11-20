import System.IO
import Data.List
import Control.Monad
import qualified Data.Map as M
import Control.Monad.State
import Data.Maybe
import Data.Ord
import System.Environment

main = do
    args <- getArgs
    contents <- readFile $ head args
    let ws = words contents
        m  = execState (mapM_ addWord ws) M.empty
        res = map (\k -> fromJust $ M.lookup k m) (M.keys m)
    print $ length . last $ sortBy (comparing length) res

isAnagramOf :: String -> String -> Bool
isAnagramOf a b = a `elem` perms b

perms [] = [[]]
perms xs = [ x:ps | x <- xs, ps <- perms (delete x xs) ]

addWord :: String -> State (M.Map String [String]) ()
addWord w = do
    m <- get
    let ks = M.keys m
        anagrams = filter (isAnagramOf w) ks
    if length anagrams > 0 then
        forM_ anagrams $ \k ->
            modify $ M.insert k (w : fromJust (M.lookup k m))
    else  
        modify $ M.insert w [w]
