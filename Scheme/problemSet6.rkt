; this assignment focuses on list manipulations, including, removing, searching and replacing, and merging lists.


(define (better-equal? a b)
  (cond
    ((and (null? a) (null? b)) #t)
    ((or (null? a) (null? b)) #f)
    ((and (symbol? a) (symbol? b)) (eq? a b))
    ((and (number? a) (number? b)) (= a b))
    ((and (list? a) (list? b)) (and
          (better-equal? (car a) (car b))
          (better-equal? (cdr a) (cdr b))))
    (else #f)))


"problem 1"
"problem 1a"

(define (rm-help f l l2)
  (cond
    ((null? l) l2)
    ((f (car l)) (rm-help f (cdr l) l2))
    (else (rm-help f (cdr l) (cons (car l) l2)))))

(define (remove-if f elements)
  (reverse (rm-help f elements '())))

(define (rm-help-once f l l2)
  (cond
    ((null? l) l2)
    ((f (car l)) (rm-help f (cdr l) l2))
    (else (rm-help-once f (cdr l) (cons (car l) l2)))))

(define (remove-if-once f elements)
  (reverse (rm-help f elements '())))


"problem 1b"

(define (nrmh v l l2)
  (cond
    ((null? l) (reverse l2))
    ((and (null? (car l)) (null? v)) (nrmh v (cdr l) l2))
    ((better-equal? v (car l)) (nrmh v (cdr l) l2))
    ((and (list? (car l)) (not (null? l))) (nrmh v (cdr l) (cons (nrmh v (car l) '()) l2)))
    (else (nrmh v (cdr l) (cons (car l) l2)))))

(define (nested-remove v elements)
  (nrmh v elements '()))

(nested-remove '() '(b 2 (()) (a b ())))
(nested-remove '(a) '((( a (a) () () )) () () ))
(nested-remove '() '((( a (a) () () )) () () ))

"problem 2"
"problem 2a"
(define (expnt-help x n tot)
  (if (<= n 0) tot
      (expnt-help x (- n 1) (* x tot))))
  

(define (expnt x n)
  (if (<= n 0) 1
      (expnt-help x n 1)))

(define (eh2 x n)
  (if (< x (expnt 10 n)) (- n 1)
      (eh2 x (+ n 1))))

(define (eh x n l)
  (let ((y (floor (/ x (expnt 10 n)))))
    (if (= n -1) l
        (eh (- x (* y (expnt 10 n))) (- n 1) (cons y l)))))

(define (reverse-new-help l l2)
  (if (null? l) l2
      (reverse-new-help (cdr l) (cons (car l) l2))))

(define (reverse-new l)
  (reverse-new-help l '()))


(define (explode-help a)
  (cond ((= a 0) '())
        ((< a 10) (cons (floor a) (explode-help (* (- a (floor a)) 10))))
        ((>= a 10) (explode-help (/ a 10)))))

(define (explode x)
  (if (= x 0) '(0)
      (explode-help x)))

(define (length-new-help l n)
  (if (null? l) n
      (length-new-help (cdr l) (+ n 1))))

(define (length-new l)
  (length-new-help l 0))


; "explode test"
; (explode 298273489234567890)


"problem 2b"
(define (i-h l n x)
  (if (= n 0) x
      (i-h (cdr l) (- n 1) (+ x (* (car l) (expnt 10 (- n 1)))))))

(define (implode l)
  (i-h l (length-new l) 0))
  
(implode '(1 2 3 4 5))

"problem 2c"

(define (s-h l s)
  (if (null? l) s (s-h (cdr l) (+ (car l) s))))

(define (sum l)
  (s-h l 0))

(define (has-property x)
  (if (= (* (sum (explode x))
            (implode (reverse (explode (sum (explode x))))))
         x)
      #t #f))

"problem 2d"

(define (find-help sequence test n a)
  (if (= n 0) (sequence (- a 1))
      (if (test (sequence a))
          (find-help sequence test (- n 1) (+ a 1))
          (find-help sequence test n (+ a 1)))))

(define (n a)
  a)

(define (find sequence test n)
  (find-help sequence test n 1))

"problem 3"
(define (search l n)
  (cond
    ((null? l) #f)
    ((better-equal? (car l) n) #t)
    (else (search (cdr l) n))))


(define (r-help l a)
  (cond
    ((null? l) #f)
    ((search a (car l)) #t)
    (else (r-help (cdr l) (cons (car l) a)))))
  
(define (r-duplicates l)
    (r-help l '()))

(define (has-duplicates? l)
  (r-duplicates l))

"problem 3a"
(define (search-no-replace l n)
  (cond
    ((null? l) #f)
    ((better-equal? (car l) n) #t)
    (else (search-no-replace (cdr l) n))))

(define (search-list a b)
  (cond
    ((null? a) #t)
    ((search b (car a)) (search-list (cdr a) b))
    (else #f)))

(define (search-no-replace a b)
  (cond
    ((null? a) #t)
    ((search b (car a)) (search-list (cdr a) b))
    (else #f)))

(define (superset-help a b a2 b2)
  
  (cond ((and (null? b) (null? a2) (null? a)) #t)
        
        ((and (null? b) (not (null? a))) #f)
        
        ((null? b) (superset-help (car a2) b2 (cdr a2) b))
        
        ((null? a) (superset-help a (cdr b) a2 (cons (car b) b2)))
        
        ((better-equal? a (car b)) (superset-help '() (cdr b) a2 b2))
        
        (else (superset-help a (cdr b) a2 (cons (car b) b2)))))


(define (superset? a b)
  (superset-help (car b) a (cdr b) '()))


(superset? '(1 2 3 4 5 6) '(1 2 3 4 5 6))


"problem 3b"
(define (sdh a b l)
  (cond ((null? a) l)
        ((search b (car a)) (sdh (cdr a) b l))
        (else (sdh (cdr a) b (cons (car a ) l)))))

(define (set-difference a b)
  (reverse (sdh a b '())))

"problem 3c"
(define (cph a b b2 l)
  (cond ((null? a) l)
        ((null? b) (cph (cdr a) b2 b2 l))
        (else (cph a (cdr b) b2 (cons (list (car a) (car b)) l)))))
  

(define (cross-product a b)
  (reverse (cph a b b '())))


"problem 4"


(define (nest-h lst a)
  (cond
    ((null? lst) a)
    ((and (not (null? (car lst))) (list? (car lst)))
     (nest-h (cdr lst) (append (nest-h (car lst) '()) a)))
    (else (nest-h (cdr lst) (cons (car lst) a)))))


(define (nestless lst)
  (reverse (nest-h lst '())))


"problem 5"
(define (merge-h l1 l2 a)
  (cond ((and (null? l1) (null? l2)) a)
        ((or (null? l1) (null? l2))
         (if (null? l1)
             (merge-h l1 (cdr l2) (cons (car l2) a))
             (merge-h (cdr l1) l2 (cons (car l1) a))))
        (else (if (< (car l1) (car l2))
                  (merge-h (cdr l1) l2 (cons (car l1) a))
                  (merge-h l1 (cdr l2) (cons (car l2) a))))))

(define (merge l1 l2)
  (reverse (merge-h l1 l2 '())))
  