public class Main {
    public static void main(String[] args) {
        // c) Instantiati clasele Triangle si Circle si apelati metoda toString() pentru fiecare instanta.
        Triangle t1 = new Triangle();
        Triangle t2 = new Triangle("red");
        Triangle t3 = new Triangle("blue", 5, 3);
        System.out.println(t1);
        System.out.println(t2);
        System.out.println(t3);

        Circle c1 = new Circle();
        Circle c2 = new Circle("pink");
        Circle c3 = new Circle("yellow", 4);
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);
        System.out.println();

        // e) Metoda "equals()" din clasa Triangle
        System.out.println(t1.equals(t2));
        System.out.println(t3.equals(t2));
        Triangle t4 = new Triangle("gray", 5, 3);
        Triangle t5 = new Triangle("blue", 5, 3);
        System.out.println(t4.equals(t3));
        System.out.println(t3.equals(t5));
        System.out.println();

        // f) Creati un vector de obiecte Form si populati-l cu obiecte de tip Triangle si Circle (upcast).
        // Parcurgeti acesti vector si apelati metoda toString() pentru elementele sale. Ce observati?
        Form[] objects = {new Circle(), new Triangle(), new Circle("purple"), new Triangle("blue"),
        new Circle("cyan", 2), new Triangle("black", 4, 4)};

        for (Form obj : objects) {
            // Se observa ca se apeleaza metodele suprascrise.
            System.out.println(obj);
        }
        System.out.println();

        // g) Parcurgeti vectorul anterior si, folosind downcasting la clasa corespunzatoare, apelati
        // metodele specifice fiecarei clase. Pentru a stabili tipul obiectului curent, folositi
        // operatorul instanceof.
        for (Form obj : objects) {
            if (obj instanceof Circle) {
                ((Circle) obj).printCircleDimensions();
            }
            else if (obj instanceof Triangle) {
                ((Triangle) obj).printTriangleDimensions();
            }
        }
        System.out.println();

        // f) Adaugati o implementare, astfel incat sa nu mai folositi "instanceof".
        for (Form obj : objects) {
            obj.printDimensions();
        }
    }
}