v_tableau=[19,17,15,13,10,5,3,1]

def sorting_loop(v_tableau):
    for i in range (0, 8):
        print(f"i={i},{v_tableau[i]}")
        for j in range(i+1, 8):
            print (v_tableau[i])
            print (v_tableau[j])
            print ("")
            if v_tableau[i]>v_tableau[j]:
                v_tableau[i], v_tableau[j]=v_tableau[j], v_tableau[i]
                print(v_tableau)            

def main():
    sorting_loop(v_tableau)

if __name__=="__main__":
    main()