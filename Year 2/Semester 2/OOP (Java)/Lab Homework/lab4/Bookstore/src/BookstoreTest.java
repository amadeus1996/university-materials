import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class BookstoreTest {
    // a) Creati clasa "BookstoreTest" pentru a testa viitoarele functionalitati ale bibliotecii.
    // Completati clasa cu metode CRUD pentru a simula functionalitatile.
    private ArrayList<Book> books;
    Scanner scanner;

    public BookstoreTest() {
        books = new ArrayList<>();
        scanner = new Scanner(System.in);
    }

    public ArrayList<Book> getBooks() {
        return books;
    }

    // a) CREATE
    public void createBook() {
        System.out.print("Title: ");
        String title = scanner.nextLine();
        System.out.print("Author: ");
        String author = scanner.nextLine();
        System.out.print("Publisher: ");
        String publisher = scanner.nextLine();
        int pageCount;
        try {
            do {
                System.out.print("Page count: ");
                pageCount = scanner.nextInt();
                scanner.nextLine();
            } while (pageCount < 1);
            Book book = new Book(title, author, publisher, pageCount);
            books.add(book);
        } catch (InputMismatchException e) {
            scanner.nextLine();
            System.out.println("Invalid page count; operation cancelled.");
        }
    }

    // a) READ 1
    public void printBook(String title) {
        for (Book book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                System.out.println(book);
                break;
            }
        }
        System.out.println("Couldn't find the book to print.");
    }

    // a) READ 2
    public void printBooks() {
        for (Book book : books) {
            System.out.println(book + "\n");
        }
    }

    // a) UPDATE
    public void updateBook(String title) {
        for (Book book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                if (confirmUpdate("Change title? (Y/N)")) {
                    System.out.print("New title: ");
                    String newTitle = scanner.nextLine();
                    book.setTitle(newTitle);
                }
                if (confirmUpdate("Change author? (Y/N)")) {
                    System.out.print("New author: ");
                    String newAuthor = scanner.nextLine();
                    book.setAuthor(newAuthor);
                }
                if (confirmUpdate("Change publisher? (Y/N)")) {
                    System.out.print("New publisher: ");
                    String newPublisher = scanner.nextLine();
                    book.setPublisher(newPublisher);
                }
                if (confirmUpdate("Change page count? (Y/N)")) {
                    try {
                        System.out.print("New page count: ");
                        int newPageCount = scanner.nextInt();
                        book.setPageCount(newPageCount);
                    } catch (InputMismatchException e) {
                        System.out.println("Invalid page count");
                    }
                }
                System.out.println("Saved changes!\n");
                break;
            }
            System.out.println("Couldn't find the book to update.\n");
        }
    }

    // a) DELETE
    public void deleteBook(String title) {
        books.removeIf(book -> book.getTitle().equalsIgnoreCase(title));
        System.out.println("Deleted the book!");
    }

    private boolean confirmUpdate(String message) {
        System.out.println(message);
        String aux = scanner.nextLine();
        while (!aux.equalsIgnoreCase("Y") && !aux.equalsIgnoreCase(("N"))) {
            System.out.println("Enter \"Y\" or \"N\".");
            aux = scanner.nextLine();
        }
        return aux.equalsIgnoreCase("Y");
    }
}
