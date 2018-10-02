; this assignment focuses around binary tree manipulations. Additionally, we were tasked with evaluating an expression tree.
; In the second half of the assignment the code relates to manipulating binary search trees.

"problemSet7"

(define (make-tree value left right) (list value left right))

(define (value tree) (car tree))

(define (left tree) (cadr tree))

(define (right tree) (caddr tree))

"problem 1"

(define example (list #\+ (list #\*
                                (list 4 '() '())
                                (list 5 '() '()))
                      (list #\+
                            (list #\/ (list 6 '() '()) '()) (list 7 '() '()))))

(define example2 (list #\+ (list #\*
                                (list 2 '() '())
                                (list 3 '() '()))
                      (list #\*
                            (list #\+ (list 4 '() '()) (list #\- (list 5 '() '()) '() '()))
                            (list #\/ (list 6 '() '())))))

(define (nvalue T)
  (if (char? (value T))
      (cond
        ((char=? (value T) #\+) (+ (nvalue (left T)) (nvalue (right T))))
        ((char=? (value T) #\*) (* (nvalue (left T)) (nvalue (right T))))
        ((char=? (value T) #\/) (/ (nvalue (left T))))
        ((char=? (value T) #\-) (- (nvalue (left T)))))
      (value T)))

(nvalue example)

"problem 2"
"problem 2a"

(define (prepare x)
  (cond ((number? x) (number->string x))
        ((char? x) (string x))))

(define (prefix T)
  (cond ((null? T) "")
        ((null? (value T)) "")
        ((char? (value T))
         (cond
           ((or (char=? (value T) #\-) (char=? (value T) #\/))
            (string-append (prepare (value T)) (prefix (left T))))
           (else 
            (string-append (prepare (value T)) (prefix (left T))
                           (if (not (null? (right T))) (prefix (right T)) "")))))
        (else (prepare (value T)))))
"the if was in there originally trying to get to do - and / with + and *, ended up not\
doing that...."

"(prepare (value (left (left example))))"

(prefix example)
(prefix example2)
(prefix '())

"problem 2b"


(define (postfix T)
  (cond ((null? T) "")
        ((null? (value T)) "")
        ((char? (value T))
         (cond
           ((or (char=? (value T) #\-) (char=? (value T) #\/))
            (string-append (postfix (left T)) (prepare (value T))))
           (else 
            (string-append (postfix (left T))
                           (if (not (null? (right T))) (postfix (right T)) "")
                           (prepare (value T))))))
        (else (prepare (value T)))))

(postfix example)
(postfix example2)
(postfix '())

"(right '())"


"problem 2c"

(define (infix T)
  (cond ((null? T) "")
        ((null? (value T)) "")
        ((char? (value T))
         (cond
           ((char=? (value T) #\-)
            (string-append "(" (prepare (value T)) (infix (left T)) ")" ))
           ((char=? (value T) #\/)
            (string-append "(1" (prepare (value T)) (infix (left T)) ")" ))
           (else 
            (string-append "("
                           (infix (left T)) (prepare (value T)) (if (not (null? (right T))) (infix (right T)) "")
                            ")"))))
        (else (prepare (value T)))))

(infix example)
"infix example2"
(infix example2)
(infix '())

"problem 3"

(define example3 (list "hello" (list "how"
                                     (list "are" '() '())
                                     (list "you" (list "doing" '() '()) '()) '()) '()))

;example3 bad example, not bs-tree

"problem 3a"

(define (bst-element? x T)
  (cond ((null? T) #f)
        ((null? x) #f)
        ((string=? x (value T)) #t)
        ((string<? x (value T)) (bst-element? x (left T)))
        (else (bst-element? x (right T)))))

(bst-element? "hey" example3)

"problem 3b"

(define (bst-insert item bs-tree)
  (let ((x item)
        (T bs-tree))
  (cond ((null? T) (make-tree x '() '()))
        ((string=? x (value T)) T)
        ((string<? x (value T)) (make-tree (value T)
                                    (bst-insert x (left T))
                                    (right T)))
        (else (make-tree (value T)
                         (left T)
                         (bst-insert x (right T)))))))
  

"problem 3c"
   
(define (bst-largest bs-tree)
  (cond ((null? bs-tree) 'undefined)
        ((null? (right bs-tree)) (value bs-tree))
        (else (bst-largest (right bs-tree)))))


"problem 3d"

(define (bst-smallest bs-tree)
  (cond ((null? bs-tree) 'undefined)
        ((null? (left bs-tree)) (value bs-tree))
        (else (bst-smallest (left bs-tree)))))

"problem 3e"

(define (bst-equal? t1 t2)
  (cond ((and (null? t1) (null? t2)) #t)
        ((or (null? t1) (null? t2)) #f)
        ((and (string=? (value t1) (value t2))
          (bst-equal? (right t1) (right t2))
              (bst-equal? (left t1) (left t2))) #t)
        (else #f)))

"problem 3f"

"bst-element? and remove, jk no remove needed"
"this forces it to check the whole thing even if an element earlier on isn't in bst \
not as efficient as possible"

(define (bst-subset? bst1 bst2)
  (if (null? bst1) #t
        (and (bst-element? (value bst1) bst2) (bst-subset? (left bst1) bst2) (bst-subset? (right bst1) bst2))))

"problem 3g"

"bst-element and remove?, similar to f, jk, just check if both are subsets,\
can reuse code"

(define (bst-set-equal? bst1 bst2)
  (and (bst-subset? bst1 bst2) (bst-subset? bst2 bst1)))

"problem 4"
"problem 4a"

(define (bst-delete-min bst)
  (cond ((null? bst) '())
        ((null? (left bst)) (right bst))
        (else bst (make-tree (value bst) (bst-delete-min (left bst)) (right bst)))))



"problem 4b"

(define (bst-delete-max bst)
  (cond ((null? bst) '())
        ((null? (right bst)) (left bst))
        (else bst (make-tree (value bst) (left bst) (bst-delete-max (right bst))))))

"problem 4c"

"largest in left subtree becomes node"

(define (bst-largest-mod bs-tree)
  (cond ((null? bs-tree) '())
        ((null? (right bs-tree)) (value bs-tree))
        (else (bst-largest-mod (right bs-tree)))))

(define (bst-delete val bst)
  (cond ((null? bst) '())
        ((string=? (value bst) val)
         (cond ((null? (bst-largest-mod (left bst))) (right bst))
               (else
                (make-tree (bst-largest-mod (left bst))
                           (bst-delete-max (left bst))
                           (right bst)))))
         (else (make-tree (value bst)
                          (bst-delete val (left bst))
                          (bst-delete val (right bst))))))
  

