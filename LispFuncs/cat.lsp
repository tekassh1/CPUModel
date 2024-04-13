(loop
    (let ((input (read-line)))
        (if (null input)
            (return)
            (progn
                (format t input)
                (terpri)))))