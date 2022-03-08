#UCF HSPT 2022 - Astronomy Rules!
#Author - Tyler Marks

#We have to see if we can get to disk1 from disk2 using two operations: rotations and flips
#For a rotation: we can perform a cyclic shift
#For a flip: we can reverse the array
#In total: the only valid ordering is if the order of the numbers is perserved either forwards or reversed
#Thus: check to see if the order of the elements is either the same or reversed

#Start by finding the index of '1' in disk1 and the index of '1' in disk2
#Then iterate over the indices to see if the order of the numbers is the same.
#Use modulus to cycle throught the array
#If our first interation is successful, then output "Saved"
#Otherwise now iterate over both arrays in opposite directions
#If this order is the same, then output "Saved"
#Otherwise print out "Doomed"

#scan in number of cases
cases = int(input())

#loop through number of cases
for case in range(cases):
    #scan in the size of the disks and each disk
    n = int(input())
    firstDisk = list(map(int, input().split()))
    secondDisk = list(map(int, input().split()))
    
    #get the index of 1 in the first and second disk
    first1Index = firstDisk.index(1)
    second1Index = secondDisk.index(1)
    
    #loop over both arrays and see if elements are in the same order
    isGood = True
    for i in range(n):
        if firstDisk[(first1Index+i)%n] != secondDisk[(second1Index+i)%n]:
            isGood = False
            break
    
    #if the disks are in the same order print out answer and continue
    if isGood:
        print("Saved")
        continue
    
    #loop over both array and see if elements are in reverse order
    isGood = True
    for i in range(n):
        if(firstDisk[(first1Index+i)%n] != secondDisk[(second1Index+n-i)%n]):
            isGood = False
            break
    
    #Print out answer
    if isGood:
        print("Saved")
    else:
        print("Doomed")
