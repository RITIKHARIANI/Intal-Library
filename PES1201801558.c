/*

DAA Mini Project Intal Library
Name : RITIK HARIANI
SRN  : PES1201801558

*/

#include "intal.h"
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

static void str_rev(char* a) //reverses the given intal
{
    int n = strlen(a);
    for(int i=0, j=n-1; i<j; ++i, --j)
    {
        a[i] = a[i] ^ a[j];
        a[j] = a[i] ^ a[j];
        a[i] = a[i] ^ a[j];
    }
}
static char* remove_leading_zeros(char* s) //removes leading zeros
{
    int len = strlen(s);
    int count = 0;
    for(int i=0 ; s[i]=='0';i++)
        count++;
    if(len==count)
    {
        free(s);
        char* zero = (char*)calloc(2,sizeof(char));
        zero[0] = '0';
        zero[1] = '\0';
        return zero;
    }        
    int result_len = len - count + 1;
    char* result = (char*)calloc(result_len,sizeof(char));
    result[result_len-1] = '\0';
    for(int i = count;i<len;++i)
    {
        result[i-count] = s[i];
    }
    free(s);
    return result;
}
static char* max_string(char* a,char* b)
{
    if(intal_compare(a,b)==1)
        return a;
    else 
        return b;
}

char* intal_add(const char* intal1, const char* intal2) //finds intal1 + intal2
{
	int len1 = strlen(intal1);
	int len2 = strlen(intal2);
	int result_len = len1 > len2 ? len1:len2;
	char* result = (char *)calloc(result_len+12,sizeof(char));
	int i = len1-1;
	int j = len2-1;
	int k = result_len;
	int carry = 0;
	int sum = 0;
	while (i>=0 || j>=0)
	{
		int element_1 = 0;
		int element_2 = 0;
		if(i >= 0)
        {
			element_1 = intal1[i]-48;
        }
        if(j >= 0)
		{
        	element_2 = intal2[j]-48;
        }
        sum = element_1 + element_2 + carry;
		result[k] = sum % 10 + 48;
		carry = sum/10;
		i--;j--;k--;
	}
	result[0] = carry + 48;
	return remove_leading_zeros(result);
}

int intal_compare(const char* intal1, const char* intal2) //compares intals
{
    int len1 = strlen(intal1);
    int len2 = strlen(intal2);
    if(len1>len2)
        return 1;
    if(len2>len1)
        return -1;
    if(len1==len2)
    {
        for(int i=0;i<len1;i++)
        {
            if(intal1[i]>intal2[i])
                return 1;
            if(intal1[i]<intal2[i])
                return -1;
        }
    }
    return 0;
}

char* intal_diff(const char* intal1, const char* intal2) //finds abs(intal1-intal2)
{
    if(intal_compare(intal1,intal2)==-1)
    {
        const char* temp = intal1;
        intal1 = intal2;
        intal2 = temp;
    }
    int len1 = strlen(intal1);
    int len2 = strlen(intal2);
    char* string1 = intal_add(intal1,"0");
    char* string2 = intal_add(intal2,"0");
    str_rev(string1);
    str_rev(string2);

    int len = len1 > len2 ?len1:len2;
    int size = len+1;
    char* result = (char*)calloc(size,sizeof(char));
    int index = 0;
    int carry = 0;
    for (int i=0; i<len2; i++) 
    { 
          
        int sub = ((string1[i]-'0')-(string2[i]-'0')-carry); 
          
        if (sub < 0) 
        { 
            sub = sub + 10; 
            carry = 1; 
        } 
        else
            carry = 0; 
  
        result[index] = sub + '0';
        index++; 
    } 
    // subtract remaining digits of larger number 
    for (int i=len2; i<len1; i++) 
    { 
        int sub = ((string1[i]-'0') - carry); 
          
        if (sub < 0) 
        { 
            sub = sub + 10; 
            carry = 1; 
        } 
        else
            carry = 0; 
              
        result[index] = sub + '0';
        index++;  
    }
    // reverse resultant string 
    str_rev(result);
    free(string1); 
    free(string2);
    return remove_leading_zeros(result); 
}
char* intal_multiply(const char* intal1, const char* intal2) //performs intal1 * intal2
{
    int len1 = strlen(intal1);
    int len2 = strlen(intal2);
    
    if(len1 == 0 || len2 == 0)
    {
        char* zero = (char*)calloc(2,sizeof(char));
        zero[0] = '0';
        zero[1] = '\0';
        return zero;
    }
    
    int result_len = len1+len2;
    int* result = (int*)calloc(result_len,sizeof(int));

    int i_n1 = 0;
    int i_n2 = 0;

    for(int i = len1-1;i>=0;i--)
    {
        int carry = 0;
        int n1 = intal1[i] - '0';

        i_n2 = 0;
        for(int j = len2-1;j>=0;j--)
        {
            int n2 = intal2[j] - '0';
            int sum = n1*n2 + (int)result[i_n1 + i_n2]  + carry;
            carry = sum/10;
            result[i_n1 + i_n2] = sum%10;
            i_n2++;
        }
        if(carry>0)
            result[i_n1+i_n2] = result[i_n1+i_n2] + carry;

        i_n1++;
    }
    int iterations = result_len-1;
    while(iterations>=0 && result[iterations] == 0)
        iterations--;

    if(iterations == -1)
    {
        free(result);
        char* zero = (char*)calloc(2,sizeof(char));
        zero[0] = '0';
        zero[1] = '\0';
        return zero;
    }
    char* answer = (char*)calloc(iterations+2,sizeof(char));
    answer[iterations+1] = '\0';

    int temp = iterations;
    while(iterations >=0)
    {
        answer[temp - iterations] = result[iterations] + '0';
        iterations--;
    }
    free(result);
    return answer;
}
char* intal_mod(const char* intal1,const char* intal2) //finds intal1 % intal2
{
    char* result = intal_add(intal2,"0"); 
    char* temp = intal_add(intal1,"0");
    char* temp1 = intal_add(intal1,"0");
    
    if(intal_compare(intal1,intal2)==-1)
    {
        free(result);
        free(temp);
        return temp1;
    }
    while(intal_compare(result,intal2)!=-1)
    {
        strcpy(result,intal2);
        while(intal_compare(result,temp1)!=1)
        {
            strcpy(temp,result);
            char *tofree = result;
            result = intal_multiply(result,"10");
            free(tofree);
        }
        char* tofree = result;
        result = intal_diff(temp1,temp);
        strcpy(temp1,result);
        free(tofree);
        
    }
    free(temp1);
    free(temp);
    return remove_leading_zeros(result);
}


char* intal_pow(const char* intal1, unsigned int n) //finds intal1^n
{
    char* result = (char*)calloc(2,sizeof(char));
    result[0] = '1';
    result[1] = '\0';
    char* x = intal_add(intal1,"0");
    if(n==0)
    {
        free(x);
        return result;
    }
    if(strcmp(x,"0")==0)
    {
        free(result);
        return x;
    }
    while(n>0)
    {
        if(n & 1)
        {
            char* temp = result;
            result = intal_multiply(result,x);
            free(temp);
        }
        n = n>>1;
        char* tofree = x;
        x = intal_multiply(x,x);
        free(tofree);    
    }
    free(x);
    return result;
}

char* intal_gcd(const char* intal1, const char* intal2) //finds the GCD
{   
    if(strcmp(intal1,"0")==0 && strcmp(intal2,"0")==0)
    {
        char* zero = (char*)calloc(2,sizeof(char));
        zero[0] = '0';
        zero[1] = '\0';
        return zero;
    }
    if(strcmp(intal1, "0") == 0) 
    {
        char *temp = malloc((strlen(intal2) + 1) * sizeof(char));
        strcpy(temp, intal2);
        return temp;
    }
    if(strcmp(intal2, "0") == 0) 
    {
        char *temp = malloc((strlen(intal1) + 1) * sizeof(char));
        strcpy(temp, intal1);
        return temp;
    }

    char* m = intal_add(intal1,"0");
    char* n = intal_add(intal2,"0");
    char* rem = NULL;
    while(intal_compare(n,"0")!=0)
    {
        rem = intal_mod(m,n);
        char* tofree = m;
        m = n;
        free(tofree);
        n = rem;
    }
    free(n);
    return m;
}

char* intal_fibonacci(unsigned int n) //nth fibonacci number
{
    char* f1 = (char*)calloc(2,sizeof(char));
    f1[0] = '0';
    f1[1] = '\0';
    char* f2 = (char*)calloc(2,sizeof(char));
    f2[0] = '1';
    f2[1] = '\0';
    if (n < 1)
    {
        free(f2);
        return f1;
    }
    for (int i = 1; i <= n; i++) 
    {  
        char* next = intal_add(f1,f2); 
        char* tofree = f1;
        f1 = f2; 
        free(tofree);
        f2 = next; 
    }
    free(f2);
    return f1;
}

char* intal_factorial(unsigned int n) //finds n! = 1*2*3*...*n
{
    char* result = (char*)calloc(2,sizeof(char));
    result[0] = '1';
    result[1] = '\0';
    char* iteration = (char*)calloc(2,sizeof(char));
    iteration[0] = '1';
    iteration[1] = '\0';
    if(n==0 || n==1)
    {
        free(iteration);
        return result;
    }
    for(unsigned int i = 2; i<=n;i++)
    {
        char* temp1 = iteration;
        iteration = intal_add(iteration,"1");
        free(temp1);
        char* temp = result;
        result = intal_multiply(result,iteration);
        free(temp);
    }
    free(iteration);
    return result;
}
static int minimum(int a,int b) //returns the minimum integer
{
    return a < b ? a : b ;
}
char* intal_bincoeff(unsigned int n, unsigned int k) //finds binomial coefficient
{
    if(n-k<k) //to make C(1000,900) faster than C(1000,500)
    {
        k=n-k;
    }
    char** C = (char**)malloc(sizeof(char*)*(k+1));
    for(int i=1;i<=k;i++)
    {
        char* zero=(char*)malloc(sizeof(char)*2);
        zero[0] = '0';
        zero[1] = '\0';
        C[i] = zero;
    }
    char* one =(char*)malloc(sizeof(char)*2);
    one[0] = '1';
    one[1] = '\0';
    C[0] = one;
    for(int i=1;i<=n;i++)
    {
        for(int j=minimum(i,k);j>0;j--)
        {
            char* temp1 = intal_add(C[j],C[j-1]);
            char* temp2 = C[j];
            C[j] = temp1;
            free(temp2);
        }
    }
    char* result = intal_add(C[k],"0");
    for(int i=0;i<=k;i++)
    {
        free(C[i]);
    }
    free(C);
    return result;
}

int intal_max(char **arr, int n) //finds the maximum intal in the array
{
    int offset = 0;
    for(int i=1;i<n;i++)
    {
        if(intal_compare(arr[offset],arr[i])==-1)
            offset = i;
    }
    return offset;
}
int intal_min(char **arr, int n) //finds the minimum intal in the array
{
    int offset = 0;
    for(int i=1;i<n;i++)
    {
        if(intal_compare(arr[offset],arr[i])==1)
            offset = i;
    }
    return offset;
}
int intal_search(char **arr, int n, const char* key) //linear search
{
    int offset = -1;
    for(int i=0;i<n;i++)
    {
        if(intal_compare(arr[i],key)==0)
        {
            offset = i;
            break;
        }
    }
    return offset;
}
int intal_binsearch(char **arr, int n, const char* key) //binary search
{
    int u = n-1;
    int l=0;
    while(l<=u)
    {
        int mid = l + (u-l)/2;
        
        if((mid == 0 || intal_compare(key,arr[mid-1])==1) && intal_compare(arr[mid],key)==0)
        {
            return mid;
        }
        else if(intal_compare(arr[mid],key)==-1)
            l = mid + 1;
        else
            u = mid -1;
        
    }
    return -1;
}

static void swap(char** a,char** b) //swap function
{
    char* temp = *a;
    *a = *b;
    *b = temp;
}
static void bottom_up_heapify(char** arr, int n, int i) 
{ 
    int largest = i; // Initialize largest as root 
    int left = 2*i + 1; // left = 2*i + 1 
    int right = 2*i + 2; // right = 2*i + 2 
  
    // If left child is larger than root 
    if (left < n && intal_compare(arr[left],arr[largest])==1) 
        largest = left; 
  
    // If right child is larger than largest so far 
    if (right < n && intal_compare(arr[right],arr[largest])==1) 
        largest = right; 
  
    // If largest is not root 
    if (largest != i) 
    { 
        swap(&arr[i], &arr[largest]); 
  
        // Recursively heapify the affected sub-tree 
        bottom_up_heapify(arr, n, largest); 
    } 
}

void intal_sort(char **arr, int n)
{
    // Building the heap (rearrange array) 
    for (int i = n / 2 - 1; i >= 0; i--) 
        bottom_up_heapify(arr, n, i); 
  
    // One by one extract an element from heap 
    for (int i=n-1; i>0; i--) 
    { 
        // Move current root to end 
        swap(&arr[0], &arr[i]); 

        // call max heapify on the reduced heap by bottom up technique
        bottom_up_heapify(arr, i, 0); 
    }     
}

char* coin_row_problem(char **arr, int n) //coin row problem
{
    char* prev = intal_add("0","0");
    char* current = intal_add(arr[0],"0");
    if(n==0)
    {
        free(current);
        return prev;
    }
    for(int i = 2;i<=n;i++) 
    {
        char* sum = intal_add(arr[i-1],prev);
        char* next = max_string(sum, current);
        if(next!=sum)
        {
            free(sum);
            next = intal_add(current,"0");
        }
        char* tofree = prev;
        prev = current;
        free(tofree);
        current = next;
    }
    free(prev);
    return current;
}

