import java.util.ArrayList;

public class BookstoreCheck {
    // c) Creati o clasa noua "BookstoreCheck".

    // c) Creati o metoda care verifica daca o carte este in dublu exemplar.
    public boolean checkDuplicate(ArrayList<Book> books, String title) {
        int count = 0;
        for (Book book : books) {
            if (book.getTitle().equalsIgnoreCase(title)) {
                if (++count == 2) {
                    return true;
                }
            }
        }
        return false;
    }

    // c) Creati o metoda care verifica daca o carte este mai groasa decat alta, si returneaza
    // cartea mai groasa.
    public Book checkPageCount(Book b1, Book b2) {
        return (b1.getPageCount() > b2.getPageCount()) ? b1 : b2;
    }
}
