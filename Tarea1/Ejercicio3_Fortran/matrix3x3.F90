! Assigment 1 Ejercicio 2: Fortran
! Equipo 1: Francisco Quirarte y Luis Hernández
program Matrix3x3

real, dimension(3, 3) :: matrix
integer :: x, y

! reading matrix from file
open(1, file='3x3matrix.txt')
do x = 1, 3
	do y = 1, 3
		read(1, *) matrix(x, y)
	end do
end do
close(1)

! print matrix
print *, 'Matrix 3x3 Initial:'
do x = 1, 3
	do y = 1, 3
		print *, matrix(x, y)
	end do
end do

! multiply matrix
matrix = matmul(matrix, matrix)

! print matrix
print *, 'Results:'
do x = 1, 3
	do y = 1, 3
		print *, matrix(x, y)
	end do
end do

end program Matrix3x3
