import java.util.Objects;

public class Triangle extends Form {
    // b) Clasa Triangle va avea 2 membri "height" si" "base" de tip float.
    private float height;
    private float base;

    // b) Constructor fara parametri.
    public Triangle() {
        this.height = 1;
        this.base = 1;
    }

    // b) Constructor parametrizat + reutilizare cod.
    public Triangle(String color) {
        super(color);
        this.height = 1;
        this.base = 1;
    }

    // b) Constructor parametrizat + reutilizare cod.
    public Triangle(String color, float height, float base) {
        super(color);
        this.height = height;
        this.base = base;
    }

    // c) Suprascrieti metoda getArea() pentru a intoarce aria specifica figurii geometrice.
    @Override
    public float getArea() {
        return height * base / 2;
    }

    // d) Suprascriere toString(). "Triangle: red 10"
    // Reutilizeaza implementarea din clasa parinte.
    @Override
    public String toString() {
        return "Triangle: " + super.toString() + " " + getArea();
    }

    // e) Adaugati o metoda "equals()" in clasa Triangle. Justificati criterul de echivalenta ales.
    // Am considerat ca 2 triunghuri sunt echivalente daca au aceeasi culoare, baza si inaltime.
    public boolean equals(Triangle otherTriangle) {
        return getColor().equalsIgnoreCase(otherTriangle.getColor()) &&
                base == otherTriangle.base &&
                height == otherTriangle.height;
    }

    // g) Adaugati metoda "printTriangleDimensions()" care sa afiseze baza si inaltimea.
    public void printTriangleDimensions() {
        System.out.println("Height: " + height + ", base: " + base);
    }

    // f) Adaugati o implementare, astfel incat sa nu mai folositi "instanceof".
    @Override
    public void printDimensions() {
        System.out.println("Height: " + height + ", base: " + base);
    }
}
