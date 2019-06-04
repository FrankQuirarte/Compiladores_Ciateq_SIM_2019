Imports System.IO
Module Module1

    Sub Main()
        Dim i As Integer, j As Integer, temp As Integer = 0
        Console.WriteLine("Reading a .txt file")
        ' Store the line in this String.
        Dim textFileStream As New IO.FileStream("C:\Users\zbook\Documents\Maestria CIATEQ\Materias\Compiladores\Tareas\Tarea2\3x3matrix.txt", IO.FileMode.OpenOrCreate, IO.FileAccess.ReadWrite, IO.FileShare.None)
        Dim myFileWriter As New IO.StreamWriter(textFileStream)
        Dim myFileReader As New IO.StreamReader(textFileStream)
        'Dim intCounter As Integer
        Dim strFileContents As String

        strFileContents = myFileReader.ReadToEnd()
        Console.WriteLine(strFileContents+vbCrLf)
        'Console.Write(MatrixRead)

       'Declare a 3 x 3 multidimensional array and set array element values.
        Dim MatrixRead = New Integer(2, 2) {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
        Console.Write(MatrixRead)

        Console.WriteLine("Product of MatrixRead by itself:")
        For i = 0 To 2
            For j = 0 To 2
                For k = 0 To 2
                    temp = temp + (MatrixRead(i, k) * MatrixRead(k, j))
                Next
                Console.Write(temp & "  ")
                temp = 0
            Next
            Console.WriteLine()
        Next



        ' End
        Console.WriteLine("Press any key to continue...")
        Console.ReadKey(True)
        myFileWriter.Close()
        myFileReader.Close()
        textFileStream.Close()

    End Sub

End Module


