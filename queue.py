print("QUEUE IMPLEMENTATION")

queue= []
while True:
    print("What you want to perform?\n 1.Enqueue,2.Dequeue,3.check size of queue,4.Emptiness of queue,5.EXIT")
    n=int(input())
    if n==1:
        print("Enter the element to  insert:")
        l=input()
        queue.append(l)
        print("Enter the element in the queue are:",queue)
    elif n==2:
        if queue==[]:
            print("Empty queue.You cannot delete!!")
        else:
            queue.pop(0)
            print("Elements in queue are:",queue)
    elif n==3:
            print("Size of queue is:",len(queue))
        
    elif n==4:
            if queue==[]:
             print("Your queue is empty!!")
            else:
                print("You have ",len(queue),"elements in your queue")
    elif n==5:
            print("Exit")
            break
    
    
