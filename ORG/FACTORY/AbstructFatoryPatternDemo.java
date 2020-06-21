package ORG.FACTORY;

public class AbstructFatoryPatternDemo {
    public static void main(String[] args) {
        AbstractFactory fatory = FactoryPrducer.getAbstructFactory("color");
        Color color = fatory.getColor("red");
        color.fill();

        AbstractFactory factory = FactoryPrducer.getAbstructFactory("shape");
        Shape shape = factory.getShape("square");
        shape.draw();
    }
}
