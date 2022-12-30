#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
  char word[200] = "input";
  char out[200] = "";
  int i;
  int j=0;
  printf("input string: \n");
  scanf("%si\n",word);
  for (i=strlen(word)-1;i>=0;i--){
     strncat(out,(word+i),1);
     //printf("%s\n",out);
//    printf("char input=%c at %d char output=%c\n",word[i],i,out[3]);
    //out[j]=*(word+i);
 //   printf("char input=%c char output=%c\n",word[i],out[j]);
    //kj++;
  }
  printf("output string: %s\n",out);
/*  
  printf("input string: %s\n", word);
  for (i=3;i>=0;i--){
      if ( isprint(*(word+i)) != 0 ) {
      printf("%c\n", *(word+i));
      }
   }i*/
}
