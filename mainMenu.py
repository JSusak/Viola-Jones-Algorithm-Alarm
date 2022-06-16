import algo

#Main terminal screen, allows users to choose between choosing a webcam and phone alongside some further confirmations.
def main():
    while True:
        #Turns input into lowercase + removes whitespace to increase consistency.
        algorithmMode = input("Would you like to start the algorithm on your computer webcam or your phone? 'webcam'/'phone'").strip().lower()
        if(algorithmMode == "webcam"):
            while True:
                webcam = input("Do you have a webcam plugged into your computer? 'y'/'n'")
                if(webcam=="y"):
                    print("SUCCESS: Beginning webcam transmission...")
                    algo.start(False)
                    break
                elif(webcam=="n"):
                    print("ERROR: Stopping program...")
                    return
                else:
                    print("Invalid input...")
        elif(algorithmMode == "phone"):
            while True:
                phone = input("Have you added your phone to CONSTANTS.py? 'y'/'n'")
                if(phone=="y"):
                    while True:
                        comment = input("Have you uncommented the corresponding line in algo.py AND set up your 'IP Webcam' site as outlined in the README? 'y'/'n'")
                        if(comment == "y"):
                            print("SUCCESS: Beginning webcam transmission...")
                            algo.start(True)
                        elif(comment=="n"):
                            print("ERROR: Stopping program...")
                            return
                        else:
                            print("Invalid input...")
                            break
                elif(phone=="n"):
                    print("ERROR: Stopping program...")
                    return
                else:
                    print("Invalid input...")
        else:
            print("Invalid input...")

if __name__ == "__main__":
    main()


