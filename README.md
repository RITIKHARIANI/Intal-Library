----------------------------------------------------------------------------------------------------------------------------------------------
# DAA Mini Project Intal Library
SRN : PES1201801558
Name: Ritik Hariani
----------------------------------------------------------------------------------------------------------------------------------------------
1) Introduction

a) What is an intal?

Intal stands for Integer of arbitrary length.
In C, an intal can be considered to be a string in which the intal is
embeddded
For example,
Let the integer be 12345123451234512345.
Its respective intal is "12345123451234512345".

b) Difference between intal and int data types in C.

Intger data types can only store numbers only in the given range such as:

long int		: -2,147,483,647 to 2,147,483,647. 
unsigned long		: 0 to 4,294,967,295
long long int           : -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
unsigned long long int  : 0 to 18,446,744,073,709,551,615

Numbers beyond these ranges cannot be stored
Due to this limitation, numbers as big as 1000 digits cannot be stored using the
integer data types provided by C.
Hence this is the need for the use of intal.

Intal can store such big numbers as a string. Due to this, we would need to build
a library which would contain of the basic operations one would perform on integers.
This is similar to the Big Int datatype of C++.

c)Applications of intal

Since intal can store integers of any length it can be used in many field that would require
to store data. This can be used in database where we would require to store high resolution
timestamps, it can be used in a banking database to store amount of money. It can also be used
in store registration numbers and unique ID.

-----------------------------------------------------------------------------------------------------------------------------------------------

2) Implementation

A) Helper functions:

 static void str_rev(char* a);

	- performs string reversal of the given intal 'a' by the use of XOR operation and returns its pointer.

 static char* remove_leading_zeros(char* s);

	- strips of leading zeros present in the intal 's' and returns its pointer.

 static char* max_string(char* a,char* b);

	- returns the pointer to the larger intal.

 static int minimum(int a,int b);

	- returns the minimum between int a and int b.
 
 static void swap(char** a,char** b);

	- swap the contents of two arrays of intals

 static void bottom_up_heapify(char** arr, int n, int i) 

	- performs heapification on the array of intals. Builds a max heap by recursively calling itself
	  it performs the swap operation after comparing and looking for the largest element to be in 
	  the proper order for a max heap.

B) Functions present in "intal.h"

1. char* intal_add(const char* intal1, const char* intal2);

	It allocates memory of the size of length+12 of the larger length of the two intals.
	It is a good practice to allocate extra bytes to be on the safer side. Hence 10 extra bytes
	have been allocated. The function iterates through the intals backwards
	The function first adds the the last digit of the intal1 to the result intal.
	The function then adds the last digit of intal2 to the digit added in the result intal.
	It then decreases the length of intal1.
	It then decreases the length of intal2.
	The carry of this addition is stored and added to the next digit of the result intal.
	This process repeats until both the intals have been traversed.
	The carry of the last addition is added to the first index of the resultant intal.

2. int intal_compare(const char* intal1, const char* intal2);

	The function returns 1 if intal1 length is greater than intal2.
	The function returns -1 if intal2 length is greater than intal1.
	If the length are equal, element wise comparison takes place and
	the respective values of 1 and -1 are returned if there is a mismatch.
	Else the function returns 0 proving the intals are equal.

3. char* intal_diff(const char* intal1, const char* intal2);
	
	The function first swaps to ensure that intal1 > intal2.
	It calculates length of both strings.
	Reverses both the strings to perform normal subtraction.
	It subtracts each corresponding digits (intal1[i] - intal2[i]).
	If subtraction is less then zero then, we add 10 into sub and 
        take carry as 1 for calculating next step else carry is 0
	Remaining digits of larger intal is subtracted.
	The result intal is reversed ,leading zeros stripped and returned.

4. char* intal_multiply(const char* intal1, const char* intal2);

	The function starts the mulplication from the end of the intals. (right to left)
	Current digit of second number is multiplied with current digit of first number 
   	and then result is added to the previously stored result at current position.
	The carry is then calculated and stored. This process continues until all digits
	are multiplied.
	The resultant intal is then returned after stripping off leading zeros.

5. char* intal_mod(const char* intal1, const char* intal2);
	
	Copies of intal1 and intal2 are made.
	This function returns the remainder of intal1/intal2.
	The function multiplies intal2 by 10 only if until copy of intal2 > copy of intal1.
	The previous iteration value of intal2 is subtracted from intal1.
	Intal2 value is reset to the original value.
	This process is continued and stopped when copy of intal1 < copy of intal2.
	The process produces the remainder intal required.
	Eg: 45 % 2.
	2 -> 20, 45-20 = 25.
	2 -> 20, 25-20 = 5.
	5-2 = 3
	5-2 = 1.
	1 is the required result intal which is returned.

6. char* intal_pow(const char* intal1, unsigned int n);
	
	If n==0, function returns "1"
	If intal is "0", function returns "0".
	Otherwise, If n is odd multiply it with result and intal1.
	then right shift n by 1 to get n/2.
	change the intal1 to intal1^2 by multiplying by itself.
	Continue process until n>0.
	Function returns the result which is intal1^n.


7. char* intal_gcd(const char* intal1, const char* intal2);
	
	If intal1 and intal2 is "0", function returns "0".
	If intal1 is "0", function returns intal2.
	If intal2 is "0", function returns intal1.
	Else
	Function performs Euclidian GCD.
	While intal2 is not "0", the function updates intal1 with intal2
	and intal2 with intal1 % intal2.
	The function then returns the intal1 which is now the Greatest common divisor.
	Euclid Gcd is:
	while b:
		rem = a%b;
		a = b;
		b = rem;
	return a;

8. char* intal_fibonacci(unsigned int n);
	
	If n is 0, returns "0"
	If n is 1, returns "1"
	Function calculates nth fibonacci number by adding
	the current and previous intals from 1 to n.

9. char* intal_factorial(unsigned int n);
	
	Function returns the factorial of n which 1*2*3*...*n.
	If n is 0 or 1, function returns "1".
	This is performed by multiplying the intal from 2 to n.

10. char* intal_bincoeff(unsigned int n, unsigned int k);

	First we need to check if ((n-k) < k ) then make k=n-k
	This provides the speed up to take care that C(1000,900) is faster than C(1000,500)
	We then create an array of pointers of size k+1 and allocate it memory and initialize it to zero.
	Make C[0] = "1". Using DP, we then calculate the next row of the pascal triangle by using the previous rows.
	followed by the relation C[j] = C[j] + C[j-1] where j is the minimum(i,k) where i is the row number
	For i = 1:
	C[1] = C[1] + C[0] = 0 + 1 = 1 --> C(1,1) = 1
	For i = 2:
	C[2] = C[2] + C[1] = 0 + 1 = 1 ==>> C(2,2) = 1
	C[1] = C[1] + C[0] = 1 + 1 = 2 ==>> C(2,2) = 2
	and so on.
	The function then returns C[k] which will contain the required intal value.
	This ensures the time complexity of O(n*k) and space complexity of O(k).

11. int intal_max(char **arr, int n);
	
	This function returns the max intal present in the given array.
	It compares the the current maximum element with the other elements.
	Once a larger intal element is found, the offset is set to the index
	of that intal element.
	Once the array is traversed, the offset is returned.

12. int intal_min(char **arr, int n);

	This function returns the min intal present in the given array.
	It compares the the current minimum element with the other elements.
	Once a smaller intal element is found, the offset is set to the index
	of that intal element.
	Once the array is traversed, the offset is returned.

13. int intal_search(char **arr, int n, const char* key);

	This function traverses through the given array of intals and once the first
	occurence of the key is matched, the offset is stored and it is return.
	The function returns -1 if they key is not found in the given array of intals.

14. int intal_binsearch(char **arr, int n, const char* key);

	The function first sets the lower bound to 0 and the upper bound to n-1
	The function then traverses through the sorted array and calculates the index of the
	middle element of the array range in use. The element at this position is compared with
	the given key. If it is matched and if the key is greater than(arr[mid-1]) or mid ==0, 
	the index is returned, else lower and upper bound are reset accordingly.
	(l = mid+1 or u = mid-1).
	If the elements is not found, the function then returns -1.	

15. void intal_sort(char **arr, int n);
	
	The in-place sort algorithm of time complexity O(n logn) is Heap Sort.
	This function performs the heap sort by first building a max heap by calling
	heapify n/2 -1 times. Then the heapsort it performed by swapping of the ith element
	and the root element and calling of the heapify function which inserts the elements
	in the non decreasing order.

16. char* coin_row_problem(char **arr, int n);

	The function uses Dynamic Programming to solve the problem. The recurrence relation used here is:
	
	Let F[n] is the array which will contain the maximum sum at n for any given n. The recurrence relation will be.

	F(n) = max{Coins[n] + F[n − 2], F[n − 1]} for n > 1,
	F(0) = 0, F(1) = Coins[1].

	While calculating F[n] we are taking maximum of coins[n]+the previous of preceding element and the previous element.
	For example F[2] = max{coins[0]+ F[2-2], F[2-1]}.
	To solve this using O(1) space we shall use two variables to store the previous and current values of F[i].
	Using this the function traverses through the array and stores the result in F[n], which is the same as the 
	"current" variable.
	The function then returns this current intal value as the maximum amount of money.	

------------------------------------------------------------------------------------------------------------------------------------------------
3) Future Work

a) More functionalities

	Functionalities such as various sorts and other mathematical functions such as square root can be built.
	This would help in use of the intals more frequently. The intal library can also be extended to negative numbers
	in the future which would also help industries such as the business (stock market). This will help in keeping track
	of decreases and increase of stocks. Banks will also find it easily useable to indicate negative values for transactions
	and loans.
	Such libraries can also be built and kept ready for competitive coding.

b) If you had no restrictions, how would you implement a library to handle integers of arbitrary length

	If there were no restrictions, i would use few in built C functions such as qsort() and bsearch(),etc which already optimized to 
	implement sorting algorithms. If there was no programming language restrictions, one can build this library using C++
	which has a more simpler flexibility in modifying strings and use of various data types.
	One can also use operator overloading and other features of C++ to make the library more efficient.
