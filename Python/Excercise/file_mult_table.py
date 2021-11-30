for i in range(1,11):
    n=i
    
    with open(f"mul {n}.txt","w") as f1:
        for j in range(10):
            f1.write(f"{j+1} * {n} = {(j+1)*n}\n")