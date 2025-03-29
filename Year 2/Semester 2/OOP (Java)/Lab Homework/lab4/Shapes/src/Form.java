// a) Definiți clasa 'Form' cu un membru 'color' de tip String, o metoda getArea() care pentru început
// va intoarce 0 și o metodă toString() care va returna culoarea (valoarea pentru 'color').
// Clasa va avea, de asemenea, un constructor fără parametri si un constructor ce va inițializa culoarea.

public abstract class Form {
    private String color;

    public Form() {
        this.color = "white";
    }

    public Form(String color) {
        this.color = color;
    }

    public float getArea() {
        return 0;
    }

    public String getColor() {
        return color;
    }

    @Override
    public String toString() {
        return color;
    }

    // f) Adaugati o implementare, astfel incat sa nu mai folositi "instanceof".
    public abstract void printDimensions();
}
