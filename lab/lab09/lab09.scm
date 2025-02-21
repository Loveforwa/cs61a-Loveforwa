(define (over-or-under num1 num2) 
(cond 
  ((< num1 num2) -1)
  ((= num1 num2) 0)
  (else 1))
)

(define (make-adder num) 
  (lambda (inc) (+ inc num))
)

(define (composed f g)
  (lambda (x) (f(g x)))
)

(define (repeat f n) 
  (if(< n 1)
    (lambda (x) x)
    (composed f (repeat f (- n 1))))
)


(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 'YOUR-CODE-HERE)

(define (duplicate lst) 'YOUR-CODE-HERE)

(expect (duplicate '(1 2 3)) (1 1 2 2 3 3))

(expect (duplicate '(1 1)) (1 1 1 1))

(define (deep-map fn s) 'YOUR-CODE-HERE)
