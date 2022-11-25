# Tugas Besar IF2124 Teori Bahasa Formal dan Automata
## Parser Bahasa JavaScript (Node.js)
Program ini merupakan program parser bahasa pemrograman JavaScript menggunakan metode Context Free Grammar (CFG) dan Deterministic Finite Automata (DFA) yang diimplementasikan menggunakan bahasa pemrograman python. Algoritma yang digunakan untuk Context Free Grammar adalah Algoritma Cocke Younger Kasami (CYK) Algorithm yang memanfaatkan Chomsky Normal Form (CNF) yang diperoleh dari konversi Context Free Grammar.

### Kelompok 5 - Beban Alek
1. Hosea Nathanael Abetnego - 13521057
2. Alex Sander - 13521061
3. Ariel Jovananda - 13521086

### Langkah memulai program
1. Clone repository
   ```
   git clone https://github.com/HoseaNA/Tubes-TBFO-Parser-Node.js
   ```
2. Eksekusi converter.py untuk mendapatkan cnf terbaru dengan command:
   ```
   py converter.py
   ```
3. Siapkan kode Node.js yang akan diparsing pada suatu file txt
4. Eksekusi program utama secara langsung dengan command:
   ```
   py mainCYK.py {nama file}
   ```
   atau
   ```
   py mainCYK.py
   ```
   hingga muncul tampilan:
  
   ![image](https://user-images.githubusercontent.com/110534062/203935825-2d617177-e876-4d3d-b624-2f67d32cdb4d.png)

   Kemudian input nama file di tempat yang tersedia
  
5. Program akan menampilkan pesan "Accepted" jika syntax program benar dan "Syntax Error!" jika tidak
