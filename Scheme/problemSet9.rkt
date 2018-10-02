; this assignment focuses around creating and using objects in scheme, along with practicing making a data structure, in this case a stack.

(define (make-stack)
  (let ((state-variable '()))
    (define (is-empty?)
      (null? state-variable))
    (define (push thing-to-push)
      (set! state-variable (cons thing-to-push state-variable)))
    (define (top)
      (car state-variable))
    (define (pop)
      (let ((a (car state-variable)))
        (set! state-variable (cdr state-variable))
        a))
    (lambda (meth-name)
      (cond ((eq? meth-name 'is-empty)
             is-empty?)
            ((eq? meth-name 'push)
             push)
            ((eq? meth-name 'top)
             top)
            ((eq? meth-name 'pop)
             pop )))))

"problem 1"


(define (make-checking initial-balance)
  (let* ((balance initial-balance)
        (act-string (string-append "beginning balance: " (number->string balance))))
    
    (define (deposit f)
      (set! balance (+ balance f))
      (set! act-string (string-append act-string "\n" "transaction: deposit amount: "
                                      (number->string f)))
      )
    
    (define (write-check f)
      (set! balance (- balance f))
      (set! act-string (string-append act-string "\n" "transaction: check amount: "
                                      (number->string (- f)))))

    (define (balance-check) balance)
    
    (define (print-statement) (string-append act-string "\n"
                                             "balance: " (number->string balance) "\n"))
    
    (lambda (method)
      (cond ((eq? method 'deposit) deposit)
            ((eq? method 'write-check) write-check)
            ((eq? method 'print-statement) print-statement)
            ((eq? method 'balance) balance-check)))))

(define checking (make-checking 100))

((checking 'balance))

((checking 'write-check) 10)

((checking 'print-statement))
((checking 'deposit) 10)

(display ((checking 'print-statement)))

(newline)

(define checking (make-checking 100))
((checking 'write-check) 10)
((checking 'write-check) 10)
((checking 'deposit) 100)
((checking 'write-check) 10)
(display ((checking 'print-statement)))

((checking 'balance))

;(display "test \n test")
(newline)


(define checking (make-checking 100))

"problem 2"


(define (make-clock h m)
  (let* ((test 0)
         (t (list (+ (* 60 h) m) (cons h m))))

    (define appendme "")

    (define (hour) (floor (/ (car t) 60)))

    (define (minutes) (- (car t) (* 60 (hour))))

    (define (tick)
      (cond ((= (car t) 1439) (set-car! t 0))
            ((= (car t) 1440) (set-car! t 1))
            (else (set-car! t (+ (car t) 1)))))

    (define (timekeep)
       (define (time)
         (cond
           ((>= (hour) 12) (set! appendme " PM"))
           (else (set! appendme " AM")))
         (string-append
          (number->string (cond ((> (hour) 12) (- (hour) 12))
                                ((= (hour) 0) 12)
                                (else (hour))))
          ":"
          (if (< (minutes) 10)
              (string-append "0" (number->string (minutes)))
              (number->string (minutes)))
          appendme
          
          ))

      (define (military)
        (string-append
         (cond ;((and (= (hour) 0) (= (minutes) 0)) "24")
               ((< (hour) 10) (string-append "0" (number->string (hour))))
               (else (number->string (hour))))
         ":"
         (if (< (minutes) 10)
             (string-append "0" (number->string (minutes)))
             (number->string (minutes)))
         ))
      
      (lambda (method)
        (cond ((eq? method 'tick) tick)
              ((eq? method 'time) time)
              ((eq? method 'military) military))))

    (lambda (method) ((timekeep) method))))


"test"

(define clock (make-clock 12 0))

"begin given tests"
(define get-time (clock 'time))
(define get-mil (clock 'military))


"display get-time"
(display (get-time))
"without display"
(get-time)
(get-mil)
"with display test"
((clock 'tick))
(display (get-time))
(display (get-mil))
((clock 'tick))
(display (get-time))
(display (get-mil))

;"clock tick"
;((clock 'tick))
;"end clock tick"

;(display 'test) (newline) 'hi
(newline)
    
          

"problem 3"

(define (make-book title author)
  (define (get-author) author)
  (define (get-title) title)
  (lambda (method)
    (cond ((eq? method 'get-author) get-author)
          ((eq? method 'get-title) get-title))))


"problem 4"

(define (make-library)
  (let* ((lib '()))

    (define (add f) (set! lib (cons f lib)))

    (define (f-t-h l l2 title)
      (cond ((null? l) l2)
            ((eq? (((car l) 'get-title)) title)
             (f-t-h (cdr l)
                    (cons (cons (((car l) 'get-author)) (((car l) 'get-title))) l2)
                    title))
            (else (f-t-h (cdr l) l2 title))))
    
    (define (find-title title) (f-t-h lib '() title))

     (define (f-a-h l l2 author)
      (cond ((null? l) l2)
            ((eq? (((car l) 'get-author)) author)
             (f-a-h (cdr l)
                    (cons (cons (((car l) 'get-author)) (((car l) 'get-title))) l2)
                    author))
            
            (else (f-a-h (cdr l) l2 author))))
    
    (define (find-author author) (f-a-h lib '() author))

    (lambda (method)
      (cond ((eq? method 'add) add)
            ((eq? method 'find-title) find-title)
            ((eq? method 'find-author) find-author)))))

(define mylib (make-library))
((mylib 'add) (make-book "Harry Potter and the Philosopher’s Stone" "Rowling"))
((mylib 'add) (make-book "Harry Potter and the Chamber of Secrets" "Rowling"))
((mylib 'add) (make-book "Harry Potter and the Prisoner of Azkaban" "Rowling"))
((mylib 'add) (make-book "Harry Potter and the Goblet of Fire" "Rowling"))
((mylib 'add) (make-book "Harry Potter and the Order of the Phoenix" "Rowling"))
((mylib 'add) (make-book "Harry Potter and the Half-Blood Prince" "Rowling"))
((mylib 'add) (make-book "Harry Potter and the Deathly Hallows" "Rowling"))
((mylib 'add) (make-book "The Hunger Games" "Suzanne Collins"))
((mylib 'add) (make-book "Catching Fire" "Suzanne Collins"))
((mylib 'add) (make-book "Mockingjay" "Suzanne Collins"))
((mylib 'add) (make-book "The Magician" "Michael Scott"))
((mylib 'add) (make-book "The Magician" "W. Somerset Maugham"))

"find title/author tests"
((mylib 'find-title) "The Magician")
((mylib 'find-author) "Suzanne Collins")
((mylib 'find-author) "Rowling")
((mylib 'find-author) "W. Somerset Maugham")

"problem 5"

(define (make-track title)
  (let* ((artist "unknown")
         (album "unknown"))
    
    (define (get-artist) artist)
    (define (get-title) title)
    (define (get-album) album)

    (define (set-title f) (set! title f))
    (define (set-album f) (set! album f))
    (define (set-artist f) (set! artist f))
  
  (lambda (method)
    (cond ((eq? method 'get-title) get-title)
          ((eq? method 'get-artist) get-artist)
          ((eq? method 'get-album) get-album)
          ((eq? method 'set-title) set-title)
          ((eq? method 'set-artist) set-artist)
          ((eq? method 'set-album) set-album)))))

"problem 6"

(define (make-music-library)
  (let* ((lib '()))

    ;add
    (define (add f) (set! lib (cons f lib)))

    ;find title
    (define (f-t-h l l2 title)
      (cond ((null? l) l2)
            ((eq? (((car l) 'get-title)) title)
             (f-t-h (cdr l)
                    (cons (list (((car l) 'get-title)) (((car l) 'get-artist)) (((car l) 'get-album))) l2)
                    title))
            (else (f-t-h (cdr l) l2 title))))
    
    (define (find-title title) (f-t-h lib '() title))

    ;find album
     (define (f-al-h l l2 album)
      (cond ((null? l) l2)
            ((eq? (((car l) 'get-album)) album)
             (f-al-h (cdr l)
                    (cons (list (((car l) 'get-title)) (((car l) 'get-artist)) (((car l) 'get-album))) l2)
                    album))
            (else (f-al-h (cdr l) l2 album))))
    
    (define (find-album album) (f-al-h lib '() album))
    
    ;find-artist
     (define (f-a-h l l2 artist)
      (cond ((null? l) l2)
            ((eq? (((car l) 'get-artist)) artist)
             (f-a-h (cdr l)
                    (cons (list (((car l) 'get-title)) (((car l) 'get-artist)) (((car l) 'get-album))) l2)
                    artist))
            (else (f-a-h (cdr l) l2 artist))))
    
    (define (find-artist artist) (f-a-h lib '() artist))

    (lambda (method)
      (cond ((eq? method 'add) add)
            ((eq? method 'find-by-title) find-title)
            ((eq? method 'find-by-album) find-album)
            ((eq? method 'find-by-artist) find-artist)))))
