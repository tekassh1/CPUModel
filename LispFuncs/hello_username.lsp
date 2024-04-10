(progn
    (print "What is your name?")
    (terpri)
    (let ((input (read-line)))
        (format t "Hello, ~a!" input)))