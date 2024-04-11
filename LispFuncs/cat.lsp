(loop
    (handler-case
        (let ((input (read-line)))
        (if (= null input)
            (return)
            (progn 
                (format t input)
                (terpri))))
        (end-of-file ()
            (return))))

{Opcode: loop,
    args: [
    {Opcode: handler-case,
        args: [{Opcode: let,
                args: [{Opcode: ,
                    args: [{Opcode: input, args: ['read-line']}]},
                           {Opcode: if, args: [
                                {Opcode: =, args: ['null', 'input']},
                                {Opcode: return, args: None},
                                {Opcode: progn,
                                    args: [
                                        {Opcode: format, args: ['t', 'input']},
                                        {Opcode: terpri, args: None}]}]}]},
               {Opcode: end-of-file,
                args: [{Opcode: , args: None},
                       {Opcode: return, args: None}]}]}
]}