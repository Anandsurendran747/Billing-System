import subprocess
class Market:

    def __init__(self, count, li, sum):
        self.count = count
        self.li = li
        self.sum = sum

    def enter(self):
        print("Hai welcome to Billing system.Enter q to quit")
        while(True):
            productName = input("Enter the product name:")

            if(productName!= 'q'):
                try:
                    productRate = int(input("Enter the product rate:"))
                    self.count += 1
                    self.li.append(f"{productName} - Rs{productRate}")
                    self.sum = self.sum+productRate
                except:
                    print("Enter correct value or enter q to exit ")
            else:
                break
        with open('PROJECT1/Bill.txt','w') as f:
            f.write(f'Total number of Items = {self.count} \n')
            for index, item in enumerate(self.li):
                f.write(f"{index+1} -> {item} \n")
            f.write(f'Total Amount Payable = Rs{self.sum} ')
            
            

    
M=Market(count=0,li=[],sum=0)
M.enter()


