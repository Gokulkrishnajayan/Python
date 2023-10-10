#include<stdio.h>
void merge(int a[],int b[],int c[],int m,int n);
void main()
{
 int m,n,i,a[20],b[20],c[20];
 printf("\nEnter the size of first array:");
 scanf("%d",&m);
 printf("Enter the elements of array:");
 for(i=0;i<m;i++)
     scanf("%d",&a[i]);
 printf("\nEnter the size of second array:");
 scanf("%d",&n);
 printf("Enter the elements of array:");
 for(i=0;i<n;i++)
     scanf("%d",&a[i]);  
 merge(a[],b[],c[],m,n);
}
void merge(int a[],int b[],int c[],m,n)
{
 int i=j=k=0;
 while(i<m&&j<n)
      {
       if(a[i]<b[j])
         {
          c[k]=a[j];
          k++;
          i++;
         }
       else
         {
          c[k]=b[j];
          j++;
          k++;
         }  
      }
 while(i<m)
      {
       c[k]=a[j];
       k++;
       i++;
      }    
 while(j<n)
      {
       c[k]=b[j];
       k++;
       j++;
      } 
 print("Merged array is:\n");
 for(i=0;i<k;i++)
     print("%d",&k[i]);             
}
