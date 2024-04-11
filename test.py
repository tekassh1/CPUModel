from preprocessor import preprocess

f = open("LispFuncs/count.lsp", 'r')
source = f.read()

res = preprocess(source)
print(res)

# (let ( (curr 0) (sum 0) ) (progn (loop (if (> curr 1000) (return) (if (or (zerop (mod curr 3) ) (zerop (mod curr 5) ) ) (progn (incf sum curr) ) ) ) (incf curr) ) (print sum) ) )