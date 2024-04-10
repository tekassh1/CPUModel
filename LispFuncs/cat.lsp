(loop
    (handler-case
        (let ((input (read-line)))
        (if (null input)
            (return)
            (progn 
                (format t input)
                (terpri))))
        (end-of-file ()
            (return))))