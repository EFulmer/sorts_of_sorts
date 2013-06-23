
(ns merge-sort)

(defn merge-sort [coll] 
  (let [first-half (take (/ (count coll) 2) coll)
        second-half (drop (/ (count coll) 2) coll)]
    (if (>= 1 (count coll)) coll
        (let [merge-first (merge-sort first-half)
              merge-second (merge-sort second-half)]
          (mergefn merge-first merge-second)))))

(defn mergefn [x y] 
  (cond (not (seq x)) y
        (not (seq y)) x
        (> (first x) (first y)) (cons (first y) (mergefn x (rest y)))
        :else (cons (first x) (mergefn (rest x) y))))
