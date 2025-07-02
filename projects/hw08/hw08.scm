(define (ascending? s) 
    (if (or (null? s) (null? (cdr s)) )
        #t
    (if (> (car s) (car(cdr s)))
        #f
    (ascending? (cdr s))))
)

(define (my-filter pred s) 
    (if (null? s)
        (list)
    (if (pred (car s))
        (cons (car s) (my-filter pred (cdr s)))
    (my-filter pred (cdr s))))
)

(define (interleave lst1 lst2)
(cond 
    ((and (null? lst1) (null? lst2)) 
        (list))
    ((and (null? lst1) (not (null? lst2)))
        (cons (car lst2) (interleave lst1 (cdr lst2))))
    ((and (not (null? lst1)) (null? lst2))
        (cons (car lst1) (interleave (cdr lst1) lst2)))
    (else
        (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2)))))
)
)

(define (no-repeats s)    
(if (null? s) s
    (cons (car s)
        (no-repeats (filter (lambda (y) (not (= (car s) y))) (cdr s))))
)
)

