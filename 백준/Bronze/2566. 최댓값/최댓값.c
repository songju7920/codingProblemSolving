int main()
{
    int arr;
    int max =0;
    int n=0;
    int m=0;
   
    for(int i=0;i<9;i++){
        for(int j=0; j<9; j++){
            scanf("%d", &arr); 
            if(max < arr){
                max = arr;
                n=i;
                m=j;
            }
        }
    }
    printf("%d\n",max);
    printf("%d %d\n",n+1,m+1);
}