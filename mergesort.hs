module MergeSort (mergeSort) where

merge :: (Ord a) => [a] -> [a] -> [a] -> [a]
merge [] [] xs = xs
merge ls [] xs = xs ++ ls
merge [] rs xs = xs ++ rs
merge (l:ls) (r:rs) xs = if l < r 
                         then merge ls (r:rs) (xs ++ [l]) 
                         else merge (l:ls) rs (xs ++ [r])

mergeSort :: (Ord a) => [a] -> [a]
mergeSort xs 
          | length xs < 2 = xs
          | otherwise = merge ls rs []
                      where n  = div (length xs) 2
                            ls = mergeSort $ take n xs
                            rs = mergeSort $ drop n xs