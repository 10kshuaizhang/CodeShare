package ORG.FACTORY;

public class ColorFatory extends AbstractFactory {

    @Override
    public Shape getShape(String shape) {
        return null;
    }

    @Override
    public Color getColor(String color) {
        if (color == null) return null;
        if (color.equalsIgnoreCase("RED")) return new Red();
        else if (color.equalsIgnoreCase("Yellow")) return new Yellow();
        else if (color.equalsIgnoreCase("Green")) return new Green();
        return null;
    }
}
