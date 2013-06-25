(ns merge-sort)

(defn merge-sort 
  "Sorts a sequence with merge sort by the given predicate. If none is 
given, <= is used. O(n log n) performance."
  ([coll] (merge-sort coll <=))
  ([coll cmp]
  (letfn [(first-half [xs] (take (/ (count xs) 2) xs))
          (second-half [xs] (drop (/ (count xs) 2) xs))
          (merge [xs ys] (cond (not (seq xs)) ys
                               (not (seq ys)) xs
                               (cmp (first xs) (first ys)) (cons (first xs) (merge (rest xs) ys))
                               :else (cons (first ys) (merge xs (rest ys)))))]
    (if (>= 1 (count coll)) coll
        (merge (merge-sort (first-half coll) cmp) (merge-sort (second-half coll) cmp))))))
