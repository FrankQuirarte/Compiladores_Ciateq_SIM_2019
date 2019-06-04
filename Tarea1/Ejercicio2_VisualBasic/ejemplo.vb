Imports System.Collections.Generic
Imports System.Linq
Imports System.Text
Module Module1
    Sub Main()
        Dim matrix1 As Integer(,), matrix2 As Integer(,)
        Dim row1 As Integer, col1 As Integer, row2 As Integer, col2 As Integer, i As Integer, j AsInteger, _
         k As Integer, temp As Integer = 0
        Console.WriteLine("Please insert no. of rows in matrix_1 :: ")
        row1 = Integer.Parse(Console.ReadLine())
        Console.WriteLine("Please insert no. of columns in matrix_1 :: ")
        col1 = Integer.Parse(Console.ReadLine())
        matrix1 = New Integer(row1 - 1, col1 - 1) {}
        Console.WriteLine("Please insert no. of rows in matrix_2 :: ")
        row2 = Integer.Parse(Console.ReadLine())
        Console.WriteLine("Please insert no. of columns in matrix_2 :: ")
        col2 = Integer.Parse(Console.ReadLine())
        matrix2 = New Integer(row2 - 1, col2 - 1) {}

        If col1 <> row2 Then
            Console.WriteLine("Multiplication is not applicable!!!")
            Console.WriteLine("Note : Number of columns of matrix_1 must be equal to Number of rows of matrix_2.")
        Else

            Console.WriteLine("Please Input the values for matrix_1")
            For i = 0 To row1 - 1
                For j = 0 To col1 - 1
                    matrix1(i, j) = Integer.Parse(Console.ReadLine())
                Next
            Next

            Console.WriteLine("Please Input the values for matrix_2")
            For i = 0 To row2 - 1
                For j = 0 To col2 - 1
                    matrix2(i, j) = Integer.Parse(Console.ReadLine())
                Next
            Next
            Console.Clear()
            Console.WriteLine("You have entered :: ")
            Console.WriteLine("Matrix 1 ::")
            For i = 0 To row1 - 1
                For j = 0 To col1 - 1
                    Console.Write(matrix1(i, j))
                    Console.Write("  ")
                Next
                Console.WriteLine()
            Next

            Console.WriteLine("Matrix 2 ::")
            For i = 0 To row2 - 1
                For j = 0 To col2 - 1
                    Console.Write(matrix2(i, j))
                    Console.Write("  ")
                Next
                Console.WriteLine()
            Next

            Console.WriteLine("Product of Matrix_1 & Matrix_2 is ::")
            For i = 0 To row1 - 1
                For j = 0 To col2 - 1
                    For k = 0 To row2 - 1
                        temp = temp + (matrix1(i, k) * matrix2(k, j))
                    Next
                    Console.Write(temp & "  ")
                    temp = 0
                Next
                Console.WriteLine()
            Next
        End If
        Console.Read()
    End Sub
End Module