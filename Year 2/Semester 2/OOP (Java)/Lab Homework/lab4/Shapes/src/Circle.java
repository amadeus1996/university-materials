public class Circle extends Form {
    // b) Clasa Circle va avea membrul "radius" de tip float.
    private float radius;

    // b) Constructor fara parametri.
    public Circle() {
        this.radius = 1;
    }

    // b) Constructor parametrizat + reutilizare cod.
    public Circle(String color) {
        super(color);
        this.radius = 1;
    }

    // b) Constructor parametrizat + reutilizare cod.
    public Circle(String color, float radius) {
        super(color);
        this.radius = radius;
    }

    // c) Suprascrieti metoda getArea() pentru a intoarce aria specifica figurii geometrice.
    @Override
    public float getArea() {
        return (float) Math.PI * radius * radius;
    }

    // d) Suprascriere toString(). "Circle: green 12.56"
    // Reutilizeaza implementarea din clasa parinte.
    @Override
    public String toString() {
        return "Circle: " + super.toString() + " " + getArea();
    }

    // g) Adaugati metoda "printCircleDimensions" care sa afiseze raza.
    public void printCircleDimensions() {
        System.out.println("Radius: " + radius);
    }

    // f) Adaugati o implementare, astfel incat sa nu mai folositi "instanceof".
    @Override
    public void printDimensions() {
        System.out.println("Radius: " + radius);
    }
}
