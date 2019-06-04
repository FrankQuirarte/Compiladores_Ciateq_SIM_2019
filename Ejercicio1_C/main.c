// C program to Open a File, 
// Read from it, And Close the File 

# include <stdio.h> 
# include <string.h> 
# include <math.h>
# define ROW (3)
# define COLUMN (3)

int main(void) 
{ 
	int i,j,k;
	float sum = 0;
	// Declare the file pointer 
	FILE *filePointer ; 
	
	// Declare the variable for the data to be read from file 
	float dataToBeRead[3][3] = {{0,0,0},{0,0,0},{0,0,0}}; 
	float resultMatrix[3][3] = {{0,0,0},{0,0,0},{0,0,0}};

	// Open the existing file GfgTest.c using fopen() 
	// in read mode using "r" attribute 
	filePointer = fopen("3x3matrix.txt", "r") ; 
	
	// Check if this filePointer is null 
	// which maybe if the file does not exist 
	if ( filePointer == NULL ) 
	{ 
		printf( "3x3matrix.txt was not found." ) ; 
	} 
	else
	{ 
		
		printf("File 3x3matrix.txt is now opened.\n") ; 
		
		// Read the dataToBeRead from the file 
		// using fgets() method 
		//while( !feof(filePointer)){
			
			
			//save the matrix 
			for (i=0; i<ROW ; i++){
				for (j=0; j<COLUMN; j++){ 
				fscanf(filePointer,"%f",&dataToBeRead[i][j]);
				}
			}
			//cast char to float
			for (i=0; i<ROW ; i++){
				for (j=0; j<COLUMN; j++){ 
				(float)dataToBeRead[i][j];
				}
			}


		//}
			// Print the original matrix read
			printf("Matrix read from file:\n"); 
			for (i=0; i<ROW ; i++){
				for (j=0; j<COLUMN; j++){ 
					printf("%.2f	",dataToBeRead[i][j]);
				}
				printf("\n");
			}
		 
		
			//multiply the matrix by itself
			for (i=0; i<ROW ; i++) {
	  		    for (j=0; j<COLUMN; j++) {
	    		    for (k=0; k<ROW; k++) {
	      			    sum = sum + dataToBeRead[i][k]*dataToBeRead[k][j];
	        		}
	        		resultMatrix[i][j] = sum;
	        		sum = 0;
				}
			}
	 
			//print the result
			printf("\nThe result matrix:\n"); 
			for (i=0; i<ROW ; i++){
				for (j=0; j<COLUMN; j++){ 
					printf("%.2f	",resultMatrix[i][j]);
				}
				printf("\n");
			}
		

		// Closing the file using fclose() 
		fclose(filePointer) ; 
		
		printf("\n"); 
	} 
	return 0;		 
} 
