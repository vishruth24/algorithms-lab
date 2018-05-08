#include<stdio.h>
int main()
{
    int i,j,n,k,a[20][20];
    printf("Enter the number of vertices\n");
    scanf("%d",&n);
    printf("Enter the matrix\n" );
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    scanf("%d",&a[i][j]);
    for(k=1;k<=n;k++)
    for(i=1;i<=n;i++)
    for(j=1;j<=n;j++)
    a[i][j]=a[i][j]||a[i][k]&&a[k][j];
    for(i=1;i<=n;i++)
    {for(j=1;j<=n;j++)
    printf("%d",a[i][j] );
    printf("\n" );
    }
return 0;
}
