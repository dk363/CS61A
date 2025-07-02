#lang racket

(define(square x)(* x x))


(define (average x y)(/ (+ x y) 2))
;(average 1 3)

(define (abs x)
    (if (< x 0)
        (- x)
        x))

(define (sqrt x)
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0))
;(sqrt 9)

(define x (cons 1 2 3))
#|
x
(car x)
(cdr x)
|#

(define one-through-four (list 1 2 3 4))

(car one-through-four)
(cdr one-through-four)
(car(cdr one-through-four))
(cons 10 one-through-four)
