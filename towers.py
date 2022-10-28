def towers(n,sour,des,aux):
    if n==1:
        print(f"Moving disk 1 from {sour} to {des}")
        return
    towers(n-1,sour,aux,des)
    print(f"Moving disk {n} from {sour} to {des}")
    towers(n-1,aux,des,sour)

n=int(input('Enter no.of disks: '))
towers(n,'A','B','C')