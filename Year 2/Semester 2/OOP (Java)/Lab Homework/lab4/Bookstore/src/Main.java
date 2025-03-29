import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // b) Creati obiecte de tip "Book" si setati atributele, introducand date de la tastatura.
        // Verificati ca numarul de pagini introdus sa fie difeirt de zero.
        // +TESTARE CRUD
        // CREATE
        BookstoreTest bookstore = new BookstoreTest();
        bookstore.createBook(); // T1 A1 P1 150
        bookstore.createBook(); // T2 A2 P2 110
        bookstore.createBook(); // T1 A1 P1 150 (pentru dublu exemplar)
        bookstore.createBook(); // T3 A2 P3 200
        System.out.println();
        // READ 1
        bookstore.printBook("test");
        bookstore.printBook("T3");
        System.out.println();
        // UPDATE
        bookstore.updateBook("T2");
        // DELETE
        bookstore.deleteBook("T3");
        System.out.println();
        // READ 2
        bookstore.printBooks();

        // c) Testarea metodelor din clasa "BookstoreCheck".
        BookstoreCheck bookstoreCheck = new BookstoreCheck();
        ArrayList<Book> books = bookstore.getBooks();
        System.out.println(bookstoreCheck.checkDuplicate(books, "T2"));
        System.out.println(bookstoreCheck.checkDuplicate(books, "T1"));
        System.out.println();
        System.out.println(bookstoreCheck.checkPageCount(books.get(0), books.get(1)));
    }
}