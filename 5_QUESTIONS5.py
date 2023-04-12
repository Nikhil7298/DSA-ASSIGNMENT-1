# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerHanoi(Disks, Source, Auxiliary, Target):  
    if(Disks == 1):  
        print ("Move Disk 1 from Source",Source,"To Destination",Target)
        return  
    TowerHanoi(Disks - 1, Source, Target, Auxiliary)  
    print ("Move Disk",Disks,"From Source",Source,"To Destination",Target)  
    TowerHanoi(Disks - 1, Auxiliary, Source, Target)  


Disks = int(input('Enter The Number of Disks: ')) 

TowerHanoi(Disks, 'Rod_A', 'Rod_B', 'Rod_C')