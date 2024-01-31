import logging

logging.basicConfig(filename=r'C:\Users\avoit\OneDrive\Documents\Programmation\pythonbeginner\example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

v_tableau=[19,17,15,13,10,5,3,1]

def sorting_loop(v_tableau):
    logging.debug(f"Initial list: {v_tableau}")
    for i in range (0, 8):
        for j in range(i+1, 8):
            if v_tableau[i]>v_tableau[j]:
                v_tableau[i], v_tableau[j]=v_tableau[j], v_tableau[i]   
                logging.debug(f"Swapped {v_tableau[j]} with {v_tableau[i]}")
    logging.debug(f"Sorted list: {v_tableau}")
    return v_tableau

def main():
    sorting_loop(v_tableau)
    print(v_tableau)

if __name__=="__main__":
    main()