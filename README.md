# MediaIQProblem

This is attempt to provide the solution for the following dogyard problem.

The Dogyard Book store assigns a unique code to books they stock which is ‘P’ followed by a number ­ for instance, ‘The Hitchhiker’s Guide to the Galaxy’ is listed as P42 in their price list catalog. Each book has an entry in the file as a comma­separated list ­ book­id, price, book name.
Sample of price list is located in b.txt

Dogyard gives each of their customers a card with a unique customer­id which is ‘C’ followed by a number ­ for instance ­ C45723. They record each purchase that a customer makes as a row of comma separated values ­ a customer­id followed by the book­ids of the books he/she purchased as part of that transaction. Thus, a customer may have one or more transactions in the transaction file.

sample of customer list is located in c.txt

Problem here is to -
1. Generate a report that has:
the top N frequent customers and the number of visits they made
the top N highest transactions and the corresponding customerid
the top N highest selling books and quantity sold
the N least selling books and quantity sold (this includes books that did not sell at all as well)
In each of the cases above, if there is a tie, output all eligible customers/books.

2. Also, as part of their rewards program Dogyard would like to offer a 10% discount to all customers whose sum total of purchases exceed a certain value V. Given a customer­id, your program should be able to determine if this customer is eligible for a discount or not.
 
getInputs() - Takes the input of files where the price list and customer list is present - separate files
processInputs() - This processes the input provided as files into object hiercachy to process data faster
generateReport() - This uses the processed information and generates the result.
