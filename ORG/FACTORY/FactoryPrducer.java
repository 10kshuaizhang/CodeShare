package ORG.FACTORY;

public class FactoryPrducer {
    public static AbstractFactory getAbstructFactory(String factory) {
        if (factory == null) return null;
        else if (factory.equalsIgnoreCase("Color")) return new ColorFatory();
        else if (factory.equalsIgnoreCase("Shape")) return new ShapeFatory();
        return null;
    }

}
