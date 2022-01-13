#Christina Nguyen, 3/11/2020, reads data and gives count of sales, the total sales and commission, and the smallest and largest sales

def main():
    projSales = open('Proj8-Sales.txt','r') #File I/O
    projSummary = open('Proj8-Summary.txt','w')
    title = projSales.readline()
    saleData = projSales.readlines()
    
    minSale = 9999999999999999999999999999999999999999999999999999 #Min and Max
    maxSale = -999999999999999999999999999999999999999999999999999

    saleSum = 0 #accumaltors
    commSum = 0
    saleCount = 0
    realtor = ''
    realtorCommSum = 0
    isFirst = True
    
    for oneLine in saleData:
        saleDataElements = oneLine.split(",")
        sale = int(saleDataElements[4].strip("$"))
        comm =  int(saleDataElements[5].strip("$"))
        
        if sale > maxSale:
            maxSale = sale
        if sale < minSale:
            minSale = sale

        if isFirst == True: #detects whether program is on the first realtor or not
            realtor = saleDataElements[1]
            isFirst = False
            maxComm = 0
            minComm = comm
            
        if realtor == saleDataElements[1]: #if realtor has multiple sales this adds comm to each realtor's total comm
            realtorCommSum += comm 
        
        else:
            projSummary.write("Commission for " + format(realtor, '12s') + "$" + format(realtorCommSum, '11,.0f') + "\n") 
          
            if realtorCommSum > maxComm: #check whether this total is new min/max for all but last sale
                maxComm = realtorCommSum
                maxRealtor = realtor
            if realtorCommSum < minComm:
                minComm = realtorCommSum
                minRealtor = realtor
                
            realtor = saleDataElements[1] #if realtor has 1 sale there's no addition 
            realtorCommSum = comm

        saleSum += sale 
        commSum += comm 
        saleCount += 1
        
    if realtorCommSum > maxComm: #check whether this total is new min/max for last sale
        maxComm = realtorCommSum
        maxRealtor = realtor
    if realtorCommSum < minComm:
        minComm = realtorCommSum
        minRealtor = realtor
        
    projSummary.write("Commission for " + format(realtor, '12s') + "$" + format(realtorCommSum,'11,.0f') + "\n" * 2)      

    projSummary.write("Realtor w/max comm " + minRealtor + " with $" + str(minComm) + "\n")
    projSummary.write("Realtor w/min comm " + maxRealtor + " with $" + str(maxComm) + "\n" * 2)
    
    projSummary.write(format("Number of sales",'18s') + format(saleCount, '11,.0f') + "\n" * 2)
    projSummary.write(format("Total sales", '18s') + "$" + format(saleSum, '10,.0f') + "\n")
    projSummary.write(format("Total commission", '18s') + "$" + format(commSum, '10,.0f') + "\n" * 2)
    projSummary.write(format("Smallest sale", '18s') + "$" + format(minSale, '10,.0f') + "\n")
    projSummary.write(format("Largest sale", '18s') + "$" + format(maxSale, '10,.0f') + "\n")

    print("Processing is complete. One record was processed. Check the summary file for the complete report.") 
    projSales.close()
    projSummary.close()

main()

#I was tried to over engineer my code by reading the second line and indexing the sale to use as my min and max sale.
#I got unstuck by setting a really big number to min and a really small number to max instead.
#I also got stuck trying to use a , in .write() when I should have beeen using a +.
#I used , instead of + because I thought the two were always interchangeable.
#After I realized that concatenation create one agrument vs commas create multiple I was able to solve my problem
#I also forgot that I had to use accumaltors which a tutor and Bill pointed out. 

#Test Cases:
#I put in -1 and a non numeric symbol(I used !) for the comm, it raises an error.
#If the file is completely clear it raises an error.
#I put a non numeric symbol in all the categories in Proj8-Sales.txt and no errors occured. 
#I put a space in all the categories in Proj8-Sales.txt and no errors occured.

#Something I wish I'd done in this project is figure out how to debug them.
#From this project I learned how to do file I/O.

